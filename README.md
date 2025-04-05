# TransferUIE
This is the github repository for the paper **A Regularization-based Transfer Learning Method for Information Extraction via Instructed Graph Decoder** (COLING2024).
This repository is merged from the master branch.

[[Paper Homepage]](https://aclanthology.org/2024.lrec-main.131/) [[Arxiv]](https://arxiv.org/pdf/2403.00891) 

In this paper, we propose a transfer learning method to unify four IE subtasks, including named entity recognition (NER), relation extraction (RE), event extraction (EE), and aspect-based sentiment analysis (ABSA). The whole framework can be called **TransferUIE**. It contains two main parts:  Instructed Graph Decode and Task-Specific Regularization.

Our TransferUIE is developed based on the [FastNLP](https://github.com/fastnlp/fastNLP), and the training and evaluating code is adapted from [utc-ie](https://github.com/yhcc/utcie).

We provide `task_specific_regularazation.py` as an essential component of transfer learning on top of utc-ie, and supplement it with `conll04`, `casie`, `16res`, `15res`, `14res` and `14lap` data processing.

Welcome any issue and email contact.


# Citation
If you think this paper helps, welcome to cite our paper.
```
@inproceedings{DBLP:conf/coling/Chen0C0024,
  author       = {Kedi Chen and
                  Jie Zhou and
                  Qin Chen and
                  Shunyu Liu and
                  Liang He},
  editor       = {Nicoletta Calzolari and
                  Min{-}Yen Kan and
                  V{\'{e}}ronique Hoste and
                  Alessandro Lenci and
                  Sakriani Sakti and
                  Nianwen Xue},
  title        = {A Regularization-based Transfer Learning Method for Information Extraction
                  via Instructed Graph Decoder},
  booktitle    = {Proceedings of the 2024 Joint International Conference on Computational
                  Linguistics, Language Resources and Evaluation, {LREC/COLING} 2024,
                  20-25 May, 2024, Torino, Italy},
  pages        = {1472--1485},
  publisher    = {{ELRA} and {ICCL}},
  year         = {2024},
  url          = {https://aclanthology.org/2024.lrec-main.131},
  timestamp    = {Thu, 23 May 2024 16:47:05 +0200},
  biburl       = {https://dblp.org/rec/conf/coling/Chen0C0024.bib},
  bibsource    = {dblp computer science bibliography, https://dblp.org}
}
```
