# Abnormal Human Behaviour Detection using Normalising Flows and Attention Mechanisms
**Authors:** Ana Filipa Rodrigues Nogueira, Hélder P. Oliveira, and Luís F. Teixeira

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

## Acknowledgments
Our code is based on code from:
[Normalizing Flows for Human Pose Anomaly Detection](https://github.com/orhir/STG-NF)
