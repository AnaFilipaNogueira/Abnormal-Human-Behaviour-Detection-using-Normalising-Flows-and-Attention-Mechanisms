import os

path = '/nas-ctm01/datasets/public/AvenueDataset/pose/test/'
orig = os.listdir(path)
masks = os.listdir('/nas-ctm01/datasets/public/AvenueDataset/gt/test_frame_mask/')

#print(orig)
#for value in orig:
#    if value[:2] == '01':
#        os.rename(path + value, path + '01_' + value[2:])

for ind, value in enumerate(orig):
    if '_alphapose-results.json' not in value:
        orig[ind]=''
    else:
        orig[ind]=value.replace('_alphapose-results.json', '')

orig_list = list(filter(None, orig))

for ind, value in enumerate(masks):
    masks[ind]=value.replace('.npy', '')


print(sorted(orig_list))
print(sorted(masks))
print(len(orig_list), len(masks))

missing_clip = []
for i in orig_list:
    #print(i)
    if i not in masks:
        missing_clip.append(i)

print(missing_clip)
print(len(missing_clip))

