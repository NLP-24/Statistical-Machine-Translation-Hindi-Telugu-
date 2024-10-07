- pre process flow:
```
data -> data-encoded -> data-bg-cleaned -> data-punctuation-standardized ->
data-number-standardized -> data-lang-cleaned -> data-Html-cleaned ->
data-unprintable-cleaned -> data-invalid-lang-range-cleaned -> data-deaccented -> data-aligned ->
data-tokenized -> data-similarity-score

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
