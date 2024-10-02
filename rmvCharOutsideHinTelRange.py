import os
import re

# Function to remove characters outside Hindi and Telugu language ranges
def remove_non_hindi_telugu(text):
    # Define a regex pattern that keeps only Hindi (Devanagari) and Telugu characters, numbers, punctuation, and spaces
    cleaned_text = re.sub(r'[^\u0900-\u097F\u0C00-\u0C7F\u0964\u0965\u0020-\u007F]', '', text)
    return cleaned_text.strip()

# Define the base directories
source_directory = r"D:\Assignments\NLP project\Statistical-Machine-Translation-Hindi-Telugu-\data-bg-cleaned"  # Replace with the path to the 'data-bg-cleaned' folder
destination_directory = r"D:\Assignments\NLP project\Statistical-Machine-Translation-Hindi-Telugu-\data-langChars-cleaned"  # Replace with the path to the 'data-lang-cleaned' folder


# Create destination folder if it doesn't exist
os.makedirs(destination_directory, exist_ok=True)

# Track if any changes were made
changes_made = False

# Iterate over all directories and files inside the source directory
for root, dirs, files in os.walk(source_directory):
    for file in files:
        # Process only .srt files
        if file.endswith(".srt"):
            # Construct the full source path to the current .srt file
            source_file_path = os.path.join(root, file)
            print(f"\nProcessing file: {source_file_path}")
            
            # Create the corresponding folder structure in the destination directory
            relative_path = os.path.relpath(root, source_directory)
            dest_folder = os.path.join(destination_directory, relative_path)
            os.makedirs(dest_folder, exist_ok=True)

            # Prepare the output file path in the destination folder
            output_file_path = os.path.join(dest_folder, file)
            
            # Open the source .srt file for reading
            with open(source_file_path, 'r', encoding='utf-8') as srt_file:
                lines = srt_file.readlines()

            # Open the destination .srt file for writing the cleaned content
            with open(output_file_path, 'w', encoding='utf-8') as output_file:
                for line in lines:
                    # Process only non-empty lines that don't contain timestamps
                    if '-->' not in line and line.strip():
                        # Remove characters outside Hindi and Telugu
                        cleaned_line = remove_non_hindi_telugu(line)
                        
                        # If the line was changed, print it and set the flag
                        if line.strip() != cleaned_line:
                            changes_made = True
                            print(f"Changed line:\nOriginal: {line.strip()}\nCleaned: {cleaned_line}\n")

                        # Write the cleaned line to the output file
                        output_file.write(cleaned_line + '\n')
                    else:
                        # Write timestamps or empty lines unchanged
                        output_file.write(line)

            # Log message if no changes were made to this file
            if not changes_made:
                print(f"No changes made in {source_file_path}.")
            else:
                print(f"Cleaned file saved at: {output_file_path}")

            # Reset changes_made flag for the next file
            changes_made = False

print("All files have been processed and saved to 'data-lang-cleaned'.")
