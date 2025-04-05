# TransferUIE
This is the github repository for the paper **A Regularization-based Transfer Learning Method for Information Extraction via Instructed Graph Decoder** (COLING2024).
This repository is merged from the master branch.

[[Paper Homepage]](https://aclanthology.org/2024.lrec-main.131/) [[Arxiv]](https://arxiv.org/pdf/2403.00891) 

In this paper, we propose a transfer learning method to unify four IE subtasks, including named entity recognition (NER), relation extraction (RE), event extraction (EE), and aspect-based sentiment analysis (ABSA). The whole framework can be called **TransferUIE**. It contains two main parts:  Instructed Graph Decode and Task-Specific Regularization.

Our TransferUIE is developed based on the [[FastNLP]](https://github.com/fastnlp/fastNLP), and the training and evaluating code is adapted from [[utc-ie]](https://github.com/yhcc/utcie).

We provide `task_specific_regularazation.py` as an essential component of transfer learning on top of utcie, and supplemented it with `conll04`, `casie`, `16res`, `15res`, `14res` and `14lap` data processing.
