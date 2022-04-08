# NukeBERT

## Introduction

![alt text](https://github.com/ayushjain1144/NukeBERT/blob/master/Images/NUKE_BERT.png)

Significant advances have been made in recent years on Natural Language Processing with machines surpassing human performance in many tasks, including but not limited to Question Answering. The majority of deep learning methods for Question Answering targets domains with large datasets and highly matured literature. The area of Nuclear and Atomic energy has largely remained unexplored in exploiting available unannotated data for driving industry viable applications. To tackle this issue of lack of quality dataset, this paper intriduces two datasets: NText, a eight million words dataset extracted and preprocessed from nuclear research papers and thesis; and NQuAD, a Nuclear Question Answering Dataset, which contains 700+ nuclear Question Answer pairs developed and verified by expert nuclear researchers. This paper further propose a data efficient technique based on BERT, which improves performance significantly as compared to original BERT baseline on above datasets. Both the datasets, code and pretrained weights will be made publically available, which would hopefully attract more research attraction towards the nuclear domain. Please read the [paper](https://arxiv.org/abs/2003.13821) for more details.

## Documentation

The most important files are in models folder

- `bert_pretrained.ipynb`: This contains the code for pretraining NukeBERT
- `bert_qa.ipynb`: This file is used for question answering on NQuAD

*Note*: These files require that you already have access to the dataset. You can upload those dataset to your google drive and replace the corresponding data paths in the notebooks

## Dataset

If you want access to the datasets, please fill this [form](https://forms.gle/1pkiP9qPjqG9GsMC6). If your request is approved, you will be able to access this [link] (https://drive.google.com/drive/folders/1-O8Q2IQ9oB7cWkxqkQQR_9xPNo4lXGoQ?usp=sharing) for the datasets. If I do not receive reply within a week, please feel free to drop an [email](mailto:ayushjain1144@gmail.com).

## Citation

If you find our work useful, please consider citing us at 

```
@misc{jain2020nukebert,
    title={NukeBERT: A Pre-trained language model for Low Resource Nuclear Domain},
    author={Ayush Jain and Dr. N. M. Meenachi and Dr. B. Venkatraman},
    year={2020},
    eprint={2003.13821},
    archivePrefix={arXiv},
    primaryClass={cs.LG}
}
```
