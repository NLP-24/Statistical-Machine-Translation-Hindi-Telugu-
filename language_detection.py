import os
from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

# Set seed for consistent language detection results
DetectorFactory.seed = 0

# Path to the main data folder
data_folder = "data"

# List to hold the folders where files were modified
modified_folders = []

# Iterate through the index folders inside the data folder
folders = sorted(os.listdir(data_folder))

# Iterate through the index folders inside the data folder
for folder_name in folders:
    folder_path = os.path.join(data_folder, folder_name)

    # Check if it's a directory
    if os.path.isdir(folder_path):
        # Construct file paths for Hindi and Telugu files
        hindi_file = os.path.join(folder_path, f"hin-{folder_name}.srt")
        telugu_file = os.path.join(folder_path, f"tel-{folder_name}.srt")

        try:
            # Read and detect the language of the Hindi file
            with open(hindi_file, 'r', encoding='utf-8') as h_file:
                hindi_text = h_file.read()
                try:
                    detected_hindi_lang = detect(hindi_text)
                except LangDetectException:
                    detected_hindi_lang = None  # Handle cases with empty or undetectable content

            # Read and detect the language of the Telugu file
            with open(telugu_file, 'r', encoding='utf-8') as t_file:
                telugu_text = t_file.read()
                try:
                    detected_telugu_lang = detect(telugu_text)
                except LangDetectException:
                    detected_telugu_lang = None  # Handle cases with empty or undetectable content

            # If either the Hindi file is not detected as 'hi' or the Telugu file is not detected as 'te'
            if detected_hindi_lang != 'hi' or detected_telugu_lang != 'te':
                # Empty both files if one of them is incorrect
                open(hindi_file, 'w').close()
                open(telugu_file, 'w').close()
                modified_folders.append(folder_name)

        except Exception as e:
            print(f"Error processing folder {folder_name}: {e}")

# Print the folders where the files were emptied
if modified_folders:
    print(f"Cleared content of the following folders due to incorrect language detection: {', '.join(modified_folders)}")
else:
    print("No files were modified.")
