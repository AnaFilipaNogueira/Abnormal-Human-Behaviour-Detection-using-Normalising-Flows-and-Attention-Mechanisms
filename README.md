# Abnormal Human Behaviour Detection using Normalising Flows and Attention Mechanisms
**Authors:** Ana Filipa Rodrigues Nogueira, Hélder P. Oliveira, and Luís F. Teixeira <br/><br/>

<!-- ## 📚 Table of Contents
- [:dart: Main Contributions](#main-contributions)
- [🏗️ Architecture](#architecture)
- [🧠 Attention Mechanisms](#attention-mechanisms)
- [⚙️ Train](#train)
- [🧪 Test](#test)
- [📈 Results](#results)
- [:handshake: Acknowledgments](#acknowledgments)
- [🔗 References](#references)
- [🔐 License](#license)
-->

## :dart: Main Contributions
* Exploration of Normalising Flows to detect Anomalous Human Behaviours - an essential task mainly for surveillance systems-related applications
* Analysis of the influence of the different parameters on the STG-NF model
* Study of the integration of attention mechanisms with STG-NF model
* Improve the state-of-the-art result for the UBnormal dataset by 3.4 pp (77.7%), for the Avenue by 4.7 pp (65.6%) and for the Avenue-HR by 3.2 pp (67.1%)
<br/>

<!-- The aim of this work is to explore normalising flows to detect anomalous behaviours which is an essential task mainly for surveillance systems-related applications. To accomplish that, a series of ablation studies were performed by varying the parameters of the \gls{stg-nf} model \cite{Hirschorn_normalisingFlows} and combining it with attention mechanisms. Out of all these experiments, it was only possible to improve the state-of-the-art result for the UBnormal dataset by 3.4 \gls{pp}, for the Avenue by 4.7 \gls{pp} and for the Avenue-HR by 3.2 \gls{pp}. However, further research remains urgent to find a model that can give the best performance across different scenarios. -->


## 🏗️ Architecture
<p align="center">
  <img src="https://github.com/AnaFilipaNogueira/Abnormal-Human-Behaviour-Detection-using-Normalising-Flows-and-Attention-Mechanisms/blob/main/images/overall_architecture.png" />
</p></br>
<em>Fig.1 - Overview of the whole model pipeline (Image adapted from [1])</em><br/><br/>

<p align="center">
  <img src="https://github.com/AnaFilipaNogueira/Abnormal-Human-Behaviour-Detection-using-Normalising-Flows-and-Attention-Mechanisms/blob/main/images/stg-nf2.png" width=70%/>
</p></br>
<em>Fig.2 - Architecture of one flow step which is constituted by ActNorm, permutation and spatio-temporal affine coupling layers (Image adapted from [1])</em><br/><br/>

### Atention Mechanisms
Dual Attention Mechanism (DAM)
<p align="center">
  <img src="https://github.com/AnaFilipaNogueira/Abnormal-Human-Behaviour-Detection-using-Normalising-Flows-and-Attention-Mechanisms/blob/main/images/DAM.png" width=80%/>
</p></br>
<em>Fig.3 - Dual Attention Mechanism (DAM) [2]</em><br/><br/>

Triplet
<p align="center">
  <img src="https://github.com/AnaFilipaNogueira/Abnormal-Human-Behaviour-Detection-using-Normalising-Flows-and-Attention-Mechanisms/blob/main/images/Triplet.png" width=80%/>
</p></br>
<em>Fig.4 - Triplet [3]</em><br/><br/>

## :gear: Train
Setup conda environment:
```
conda conda env create -f environment.yml
conda activate mediapipe_venv
```

## :test_tube: Test


## :chart_with_upwards_trend: Results
<div align="justify"><em>Table 1 - Results of the best run after optimising the network parameters (STG-NF optimised) and the best run combining the STG-NF model and the attention mechanisms (STG-NF + attention) compared to the state-of-the-art results.</em></div>  

|  | ShanghaiTech | ShanghaiTech-HR | UBnormal | Avenue | Avenue-HR |
| :---- | :----: | :----: | :----: | :----: | :----: |
| [STG-NF](https://doi.org/10.1109/ICCV51070.2023.01246) | 85.9 | 87.4 | 71.8 | - | - |
| [DA-Flow](https://arxiv.org/abs/2406.02976) | 86.5 | **87.8** | 74.1 | - | - |
| [MGENet](https://doi.org/10.1145/3664647.3680592) | **86.9** | - | 74.3 | - | - |
| [STG-NF + Jigsaw](https://doi.org/10.1109/CAC59555.2023.10451821) | **86.9** | 87.7 | 70.0 | 60.9 | 63.9 |
| **STG-NF optimised (ours)** | 86.3 | 87.2 | **77.7** | 62.2 | **67.1** |
| **STG-NF + attention (ours)** | 86.0 | 87.7 | 76.0 | **65.6** | 63.9 |


## :handshake: Acknowledgments 
Our code is based on code from:
[Normalizing Flows for Human Pose Anomaly Detection](https://github.com/orhir/STG-NF)
<!-- Also, takes inspiration from the work presented in the paper: [DA-Flow](https://arxiv.org/abs/2406.02976) and [Rotate to Attend: Convolutional Triplet Attention Module](https://openaccess.thecvf.com/content/WACV2021/papers/Misra_Rotate_to_Attend_Convolutional_Triplet_Attention_Module_WACV_2021_paper.pdf) -->

## 🔗 References
[1] Hirschorn, O., Avidan, S.: Normalizing flows for human pose anomaly detection. In: 2023 IEEE/CVF International Conference on Computer Vision (ICCV). pp. 13499–13508. IEEE Computer Society, Los Alamitos, CA, USA (oct 2023). [https://doi.org/10.1109/ICCV51070.2023.01246](https://doi.org/10.1109/ICCV51070.2023.01246)

[2] Wu, R., Chen, Y., Xiao, J., Li, B., Fan, J., Dufaux, F., Zhu, C., Liu, Y.: Da-flow: Dual attention normalizing flow for skeleton-based video anomaly detection (2024). [https://arxiv.org/abs/2406.02976](https://arxiv.org/abs/2406.02976)

[3] Misra, D., Nalamada, T., Arasanipalai, A.U., Hou, Q.: Rotate to attend: Convolutional triplet attention module. In: 2021 IEEE Winter Conference on Applications of Computer Vision (WACV). pp. 3138–3147 (2021). [https://doi.org/10.1109/WACV48630.2021.00318](https://doi.org/10.1109/WACV48630.2021.00318)

## :closed_lock_with_key: License
This code is distributed under a Creative Commons LICENSE - Attribution-NonCommercial 4.0 International.
