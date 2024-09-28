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
    
    for hin_sub, tel_sub in zip(hindi_subs, telugu_subs):
        aligned_sentences.append((hin_sub['sentence'], tel_sub['sentence']))
    
    return aligned_sentences

def save_to_tsv(aligned_sentences, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as tsvfile:
        writer = csv.writer(tsvfile, delimiter='\t')
        for hindi_sentence, telugu_sentence in aligned_sentences:
            writer.writerow([hindi_sentence, telugu_sentence])

hindi_srt_file = 'D:\\Assignments\\NLP project\\web scrapper\\hin-5.srt'
telugu_srt_file = 'D:\\Assignments\\NLP project\\web scrapper\\tel-5.srt'

try:
    hindi_subs = parse_srt(hindi_srt_file)
    telugu_subs = parse_srt(telugu_srt_file)

    aligned_sentences = align_subtitles(hindi_subs, telugu_subs)

    output_tsv_file = 'parallel_corpus.tsv'
    save_to_tsv(aligned_sentences, output_tsv_file)

    print(f"Successfully created parallel corpus: {output_tsv_file}")

except FileNotFoundError as e:
    print(e)
