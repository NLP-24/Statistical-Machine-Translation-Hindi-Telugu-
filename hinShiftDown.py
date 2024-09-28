import pandas as pd

# Load your TSV file 
df = pd.read_csv('D:\\Assignments\\NLP project\\web scrapper\\new.tsv', sep='\t', header=None)

# Shift the Hindi column down by 1
df[0] = df[0].shift(1)

# Save the updated DataFrame back to a TSV file
df.to_csv('your_updated_file.tsv', sep='\t', index=False, header=False)
