# Natural Language Processing Dataset Preprocessing

This project consists of various pre-processing steps applied to a dataset in the context of Natural Language Processing (NLP). Each step is organized into a sequence to clean, standardize, and align the dataset for further processing or analysis.

## Team
- Parth Vijay (S20220010166)
- AJ Harshavardhan (S20220010011)
- Srikar Chaturvedula (S20220010207)
- Sushant Kuril (S20220010214)

## Project Structure

The project contains several directories, each representing a different version of the dataset after applying one of the pre-processing steps. These steps are applied in sequence as follows:

1. **data** - Original dataset.
2. **data-encoded** - Dataset after encoding to a standard format.
3. **data-bg-cleaned** - Dataset after background noise cleaning.
4. **data-punctuation-standardized** - Dataset after punctuation standardization.
5. **data-number-standardized** - Dataset after standardizing number formats.
6. **data-lang-cleaned** - Dataset after cleaning language inconsistencies.
7. **data-html-cleaned** - Dataset after HTML tags and related artifacts are removed.
8. **data-unprintable-cleaned** - Dataset after removing unprintable characters.
9. **data-invalid-lang-range-cleaned** - Dataset after cleaning invalid characters outside the language range.
10. **data-deaccented** - Dataset after removing accents and diacritics.
11. **data-aligned** - Final version of the dataset, aligned for analysis.

## Preprocessing Workflow

The pre-processing pipeline follows a sequential flow to ensure the dataset is properly cleaned and prepared for NLP tasks. Below is the overall flow of the process:

```
data -> data-encoded -> data-bg-cleaned -> data-punctuation-standardized -> 
data-number-standardized -> data-lang-cleaned -> data-html-cleaned -> 
data-unprintable-cleaned -> data-invalid-lang-range-cleaned -> data-deaccented -> data-aligned
```

## How to Use

Each pre-processing step is automated using Python scripts located in the `scripts/` folder. These scripts generate the corresponding versions of the dataset in the appropriate folders.

1. **Run individual scripts**: 
   - To run any specific pre-processing step, navigate to the `scripts/` directory and run the Python script for that step.
   - Example:
     ```bash
     python3 encode_data.py
     ```
   
2. **Automated pipeline**: 
   - You can also run the entire preprocessing pipeline by executing the main pipeline script:
     ```bash
     python3 run_pipeline.py
     ```

## Dataset Description

The dataset used in this project is a collection of text in multiple languages, where the following tasks are performed:

- **Encoding**: Converts the dataset into a uniform character encoding format (e.g., UTF-8).
- **Background Cleaning**: Removes unnecessary background text or noise present in the dataset.
- **Punctuation Standardization**: Standardizes punctuation to ensure consistency.
- **Number Standardization**: Ensures numbers are presented in a uniform format.
- **Language Cleaning**: Corrects or removes language-based inconsistencies.
- **HTML Cleaning**: Strips away HTML tags and other unnecessary HTML artifacts.
- **Unprintable Character Removal**: Removes unprintable and invalid characters from the dataset.
- **Invalid Language Range Cleaning**: Filters out any characters that fall outside the acceptable language range.
- **Deaccenting**: Removes accents and diacritics for better normalization.
- **Alignment**: Aligns text for parallel language processing tasks.
