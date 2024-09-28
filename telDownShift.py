import pandas as pd

# Load your TSV file into a DataFrame
df = pd.read_csv('D:\\Assignments\\NLP project\\web scrapper\\new.tsv', sep='\t', header=None)

# Assuming Hindi is column 0 and Telugu is column 1
# Shift the Telugu column down by 1
df[1] = df[1].shift(1)

# Save the updated DataFrame back to a TSV file
df.to_csv('your_updated_file.tsv', sep='\t', index=False, header=False)
