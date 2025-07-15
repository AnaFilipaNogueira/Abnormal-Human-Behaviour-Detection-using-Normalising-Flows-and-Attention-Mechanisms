import torch
import torch.nn as nn
import numpy as np
from args import init_parser, init_sub_args

parser = init_parser()
args = parser.parse_args()

import torch
import torch.nn as nn

class MultiHeadAttention(nn.Module):
    def __init__(self, x_input, in_channels, out_channels, num_heads=args.n_heads, attention_type='skeleton', opt='maxpool'):
        super(MultiHeadAttention, self).__init__()
        self.num_heads = num_heads
        self.attention_type = attention_type
        self.opt = opt

        # Create a set of convolutions for each head
        self.convs = nn.ModuleList([
            nn.Conv2d(in_channels, out_channels, kernel_size=(3, 7), padding='same', bias=True)
            for _ in range(num_heads)]).to('cuda:0')
        self.batch_norms = nn.ModuleList([nn.BatchNorm2d(out_channels) for _ in range(num_heads)]).to('cuda:0')
        self.sigmoid = nn.Sigmoid().to('cuda:0')

        # Linear layer to project concatenated output
        B, C, T, V = x_input.shape
        self.projection = nn.Linear(num_heads * C * T * V, C * T * V).to('cuda:0')

    def forward(self, x):
        for _ in range(args.n_mecatt_inside):
            # Prepare attention features for all heads
            head_outputs = []
            for conv, batch_norm in zip(self.convs, self.batch_norms):
                if self.attention_type =='skeleton':
                    x_permuted = x.permute(0, 2, 1, 3)  # Adjust shape for skeleton attention
                elif self.attention_type =='frame':
                    x_permuted = x.permute(0, 3, 2, 1)
                elif self.attention_type =='channel':
                    x_permuted = x
                
                
                if self.opt == 'maxpool':
                    x_max, _ = x_permuted.max(dim=1, keepdim=True)
                    x_conv = conv(x_max)
                elif self.opt == 'zpool':
                    x_zpool = torch.cat((torch.max(x, 1)[0].unsqueeze(1), torch.mean(x, 1).unsqueeze(1)), dim=1)
                    x_conv = conv(x_zpool)

                x_final = self.sigmoid(batch_norm(x_conv))

                # Multiply with input for attention
                x_mul = torch.mul(x_final, x_permuted)
                head_outputs.append(x_mul)

            concatenated = torch.cat(head_outputs, dim=1)
            projected = self.projection(concatenated.reshape(concatenated.size(0), -1))
            x = projected.view_as(x)

        return x  # Reshape to match input


def DAM(x):
    in_channels, out_channels = 1, 1
    att_skl = MultiHeadAttention(x, in_channels, out_channels, num_heads=args.n_heads, attention_type='skeleton')
    att_frame = MultiHeadAttention(x, in_channels, out_channels, num_heads=args.n_heads, attention_type='frame')
    y_skl = att_skl(x)
    y_frame = att_frame(x)
    x_DAM = 1/2*(y_skl + y_frame) + x

    return x_DAM


def triplet(x):
    in_channels, out_channels = 2, 1
    att_skl = MultiHeadAttention(x, in_channels, out_channels, num_heads=args.n_heads, attention_type='skeleton', opt='zpool')
    att_frame = MultiHeadAttention(x, in_channels, out_channels, num_heads=args.n_heads, attention_type='frame', opt='zpool')
    att_identity = MultiHeadAttention(x, in_channels, out_channels, num_heads=args.n_heads, attention_type='channel', opt='zpool')
    y_skl = att_skl(x)
    y_frame = att_frame(x)
    y_identity = att_identity(x)
    x_triplet = 1/3*(y_skl + y_frame + y_identity) + x

    return x_triplet


def skeleton_attention(x):
    in_channels, out_channels = 1, 1
    att_skl = MultiHeadAttention(x, in_channels, out_channels, num_heads=args.n_heads, attention_type='skeleton')
    y_skl = att_skl(x)

    return y_skl

def frame_attention(x):
    in_channels, out_channels = 1, 1
    att_frame = MultiHeadAttention(x, in_channels, out_channels, num_heads=args.n_heads, attention_type='frame')
    y_frame = att_frame(x)

    return y_frame

