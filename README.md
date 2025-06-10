# Abnormal Human Behaviour Detection using Normalising Flows and Attention Mechanisms
**Authors:** Ana Filipa Rodrigues Nogueira, Hélder P. Oliveira, and Luís F. Teixeira

**Main Contributions:**
<i>Improve the state-of-the-art result for the UBnormal dataset by 3.4 pp, for the Avenue by 4.7 pp and for the Avenue-HR by 3.2 pp</i>
<i>Exploration of the influence of the different parameters on the STG-NF model</i>
<i>Exploration of the combination of attention mechanisms with STG-NF model</i>

<!-- The aim of this work is to explore normalising flows to detect anomalous behaviours which is an essential task mainly for surveillance systems-related applications. To accomplish that, a series of ablation studies were performed by varying the parameters of the \gls{stg-nf} model \cite{Hirschorn_normalisingFlows} and combining it with attention mechanisms. Out of all these experiments, it was only possible to improve the state-of-the-art result for the UBnormal dataset by 3.4 \gls{pp}, for the Avenue by 4.7 \gls{pp} and for the Avenue-HR by 3.2 \gls{pp}. However, further research remains urgent to find a model that can give the best performance across different scenarios. -->


## Architecture
<p align="center">
  <img src="https://github.com/AnaFilipaNogueira/Abnormal-Human-Behaviour-Detection-using-Normalising-Flows-and-Attention-Mechanisms/blob/main/images/Picture3.png" />
</p></br>
<em>Fig.1 - Overview of the whole model pipeline (Image adapted from [1])</em><br/><br/>

<p align="center">
  <img src="https://github.com/AnaFilipaNogueira/Abnormal-Human-Behaviour-Detection-using-Normalising-Flows-and-Attention-Mechanisms/blob/main/images/stg-nf2.png" width=80%/>
</p></br>
<em>Fig.2 - Architecture of one flow step which is constituted by ActNorm, permutation and spatio-temporal affine coupling layers (Image adapted from [1])</em><br/><br/>

## Atention Mechanisms
Dual Attention Mechanism (DAM)
<p align="center">
  <img src="https://github.com/AnaFilipaNogueira/Abnormal-Human-Behaviour-Detection-using-Normalising-Flows-and-Attention-Mechanisms/blob/main/images/DAM.png" width=90%/>
</p></br>
<em>Fig.3 - Dual Attention Mechanism (DAM)</em><br/><br/>

Triplet
<p align="center">
  <img src="https://github.com/AnaFilipaNogueira/Abnormal-Human-Behaviour-Detection-using-Normalising-Flows-and-Attention-Mechanisms/blob/main/images/Triplet.png" width=90%/>
</p></br>
<em>Fig.4 - Triplet</em><br/><br/>

<p align="center">
  <img src="https://github.com/AnaFilipaNogueira/Abnormal-Human-Behaviour-Detection-using-Normalising-Flows-and-Attention-Mechanisms/blob/main/images/image.png" width=90%/>
</p></br>
<em>Fig.5 - Results of the best run after optimising the network parameters (STG-NF optimised) and the best run combining the STG-NF model and the attention mechanisms (STG-NF + attention) compared to the state-of-the-art results.</em><br/><br/>


## Acknowledgments
Our code is based on code from:
[Normalizing Flows for Human Pose Anomaly Detection](https://github.com/orhir/STG-NF)

Also, takes inspiration from the work presented in the paper: [DA-Flow](https://arxiv.org/abs/2406.02976)

## :closed_lock_with_key: License
This code is distributed under a Creative Commons LICENSE - Attribution-NonCommercial 4.0 International.
