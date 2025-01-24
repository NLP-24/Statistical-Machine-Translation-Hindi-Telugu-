## Table of Contents
- [Project Overview](#project-overview)
- [Folder Structure](#folder-structure)
- [Requirements](#requirements)
- [Installation](#installation)
- [Dataset Preparation](#dataset-preparation)
- [How to Run](#how-to-run)
- [Training the Model](#training-the-model)
- [Translating New Sentences](#translating-new-sentences)
- [Acknowledgments](#acknowledgments)

## Project Overview
The goal of this project is to translate sentences from Hindi to Telugu using a Transformer-based model. The model is built from scratch using PyTorch and includes various text preprocessing and feature extraction techniques to enhance translation quality.


## Folder Descriptions
- **data_model_input/**: Contains the dataset file in a tab-separated format with Hindi and Telugu sentence pairs.
- **models/**: Contains the Transformer model definition and trained model weights.
- **vocab/**: Stores the vocabulary files generated during preprocessing for Hindi (source) and Telugu (target).

- **utils.py**: Provides helper functions like data loading, tokenization, and encoding.
- **train.py**: Main script to perform data preprocessing, training, and saving the model.
- **translate.py**: Script to translate input sentences from Hindi to Telugu using the trained model.
- **requirements.txt**: Lists all the Python packages required to run the project.
- **README.md**: Documentation on how to use the project, including installation and usage instructions.

- ** additional nlp techniques folders## Step 2: Training the Model


# Step - 1: To train the Transformer model, run:

```bash
python train.py
```

The script will initialize the model, train it on the dataset, and save the weights to models/model_weights.pth.

# Step - 2: Translating New Sentences
To translate new sentences from Hindi to Telugu, use:
```
python translate.py --input "आपका स्वागत है"

```
This will generate the Telugu translation for the given Hindi sentence.


## Machine translation model is in folder machine-translation

- pre process flow:
```
data -> data-encoded -> data-bg-cleaned -> data-punctuation-standardized ->
data-number-standardized -> data-lang-cleaned -> data-Html-cleaned ->
data-unprintable-cleaned -> data-invalid-lang-range-cleaned -> data-deaccented -> data-aligned ->
data-tokenized -> data-similarity-score
```

## Data Set
We will be building a hybrid data set (movie subtitle from [OpenSubtitles.org](https://opensubtitles.org) + OPUS)

### Data Collecion
- [x] Selection of movies 
- [x] Downloading the subtitles 
- [x] Making different files (hindi.txt telugu.txt)

## Process (Data Alignment / Data Pre-processing) 

### Description 
1. Individual Pre-Processing (for each language file separately)
2. Initial Data Alignment
3. Post-Alignment Processing and Quality Control
4. Corpus Creation and Final Pre-Processing

### Individual Pre-Processing
- [x] Subtitle format detection and conversion(Usage of only one source (.srt file)) ( AJ Harsh Vardhan ) 
- [x] Character encoding conversion (Convert all files to UTF-8 for consistency Using **chardet**) ( AJ Harsh Vardhan ) 
- [x] Language checking (languageDetection Using langDetect) ( Sushant )
- [x] Removing background noise. ( AJ Harsh Vardhan ) 
- [x] Removing html tags (eg., ```<i></i>`& [U+202B] and [U+202C]```) ( AJ Harsh Vardhan ) 
- [x] Tokenization and sentence splitting ( Sushant ) 
- [x] Removing unprintable characters ( Srikar )
- [x] Removing characters outside the language pair ( AJ Harsh Vardhan ) 
- [x] Normalizing whitespace (Removal of extra space) ( Srikar )
- [x] Deaccenting accented characters (Converting the accented to their base form) ( Parth )
- [x] Standardizing punctuation ( Parth )
- [x] Standardizing numbers ( Parth )

### Initial Data Alignment 
- [x] Length-Based Sentence Alignment. ( Parth ) 
- [x] Alignment with Time Overlaps. ( Parth ) 
- [x] Combining Length and Time-Based Approaches. ( Parth ) [Actually Above Three steps is just one step we are using hybrid of two algorithm (Using some assumption and Tradeoffs)]
- [x] Handling Misalignments. ( AJ Harsh Vardhan )  
- [x] Similarity Scoring. ( Sushant )

### Post-Alignment Processing and Quality Control
- [x] File Format ( AJ Harsh Vardhan ) 
- [x] Sentence Pair Shuffling ( Sushant )
- [x] Versioning (AJ Harsh Vardhan)

### How to find Current Output (last done/completed is the current output) [Check readme.md for continuation]
- Encoding 
- Bg-Removal
- Punctuation Standardize
- Number Standardize


# Hindi-to-Telugu Translation Model

This project implements a Hindi-to-Telugu translation model using a Transformer architecture developed from scratch. It involves various NLP preprocessing tasks like POS tagging, TF-IDF vectorization, stop-word removal, transliteration, and more.

# Individual Contribution
- S20220010011 (Alagadapa Jaya Harsh Vardhan):

    Parts of speech tagging (POS tagging), N-grams ( N = 2), Transliterator, Integrated Transformer model by adjusting hyperparameters.
    Translate Script to utilize model.

- S20220010166 (Parth Vijay): 
    One hot encoding, Label encoding, FastText, Bag of words,
    train.py functions

- S20220010219 (Sushant Kuril): 
    NEL, Gensim word vector, Dependency parse, Vocab script,
    Model optimization

- S20220010207  (Srikar Chaturvedula): 
    Term frequency-Inverse document frequency (tf-idf), 
    Stop-Words removal, Named entity recognization (NER), 
    Model optimization
