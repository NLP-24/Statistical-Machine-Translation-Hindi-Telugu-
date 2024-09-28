import re
import csv
import os

def parse_srt(srt_file):
    if not os.path.exists(srt_file):
        raise FileNotFoundError(f"The file {srt_file} does not exist.")
    
    with open(srt_file, 'r', encoding='utf-8') as file:
        content = file.read()

    pattern = re.compile(
        r'(\d+)\n(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})\n(.*?)(?=\n\n|\Z)', re.DOTALL
    )
    matches = pattern.findall(content)

    subtitles = []
    for match in matches:
        index, start_time, end_time, sentence = match

        sentence_clean = re.sub(r'{.*?}|<.*?>', '', sentence).replace('\n', ' ').strip()

        if sentence_clean:
            subtitles.append({
                'start_time': start_time,
                'end_time': end_time,
                'sentence': sentence_clean
            })

    return subtitles

def align_subtitles(hindi_subs, telugu_subs):
    aligned_sentences = []
    
    # Aligning based on the order of subtitles in both lists
    for hin_sub, tel_sub in zip(hindi_subs, telugu_subs):
        aligned_sentences.append((hin_sub['sentence'], tel_sub['sentence']))
    
    return aligned_sentences

def save_to_tsv(aligned_sentences, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as tsvfile:
        writer = csv.writer(tsvfile, delimiter='\t')
        for hindi_sentence, telugu_sentence in aligned_sentences:
            writer.writerow([hindi_sentence, telugu_sentence])

# Define the base path for the SRT files
base_path = 'D:/Assignments/NLP project/web scrapper/'

# Collect all aligned sentences
all_aligned_sentences = []

# Loop through the files from 1 to 10
for i in range(1, 11):
    hindi_srt_file = os.path.join(base_path, f'hin-{i}.srt')
    telugu_srt_file = os.path.join(base_path, f'tel-{i}.srt')

    try:
        hindi_subs = parse_srt(hindi_srt_file)
        telugu_subs = parse_srt(telugu_srt_file)

        # Align the subtitles for this pair
        aligned_sentences = align_subtitles(hindi_subs, telugu_subs)

        # Extend the master list of aligned sentences
        all_aligned_sentences.extend(aligned_sentences)

    except FileNotFoundError as e:
        print(e)

# Save all aligned sentences to a single TSV file
output_tsv_file = 'parallel_corpus.tsv'
save_to_tsv(all_aligned_sentences, output_tsv_file)

print(f"Successfully created parallel corpus: {output_tsv_file}")
