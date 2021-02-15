# Hand Printed Names Recognition
## Using Convolutional Neural Networks to convert handwritten names images into machine-encoded text
Author: [Edward De Jesus](https://github.com/edejesus196)

## Repository Structure
    
    ├── images                            Images
    ├── presentation                      Final PowerPoint presentation slideshows
    ├── main_notebook.ipynb               Final notebook 
    ├── pneumoniaCDC2010.csv              CDC data used for timeseries chart of pnuemoia cases
    └── README.md                         ReadMe

## Overview

Recognizing hand printed text has been a challenge for Optical Character Recognition (OCR) because of its many variations. With the rise of machine learning and higher processing power, however, modern OCR technology is now better at recognizing more subtle patterns in text, and, thus, although not perfect, better at recognizing hand handwritten text. 

The ability to automate the process of converting handwriting text to machine-encoded text with the aid of machine learning has a lot of potential as a business application. The U.S. LIbrary of Congress, for example, holds approximately sixty million manuscripts, which are documents written by hand rather than typed or printed. Improving handwritten text recognition using machine learning can be of tremendous help with improving searchability, readability and accessibility of these documents, many of which are of historical significance.

## Approach

In this case study I will demonstrate how to convert images of handwritten names into machine-encoded text using machine learning and computer vision techniques.

### Data and model preparation process
1. **Acquire datasets**
2. **Create Models to predict characters**
3. **Perform character segmentation and names tranciptions**

#### Datasets
Two datasets, both obtained from Kaggle.com, were used to train the models and to test the model that performed best on the validation set.

The first dataset is called the Handwritten Characters dataset. This dataset was used to train the models to recognize the different characters. It contains 39 classes in total. This includes all lowercase and uppercase English alphabet character, digits from 0 -9, and some special characters, which include @, #, $, &. Also, the dataset is divided into  834,036 training samples and 22,524 validation samples.





## Results

## Next Steps