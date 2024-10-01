import os
import chardet

source_base_dir = r'D:\Assignments\NLP project\Statistical-Machine-Translation-Hindi-Telugu-\data'  # Replace with your source folder path
destination_base_dir = r'D:\Assignments\NLP project\Statistical-Machine-Translation-Hindi-Telugu-\data-encoded'  

os.makedirs(destination_base_dir, exist_ok=True)

for folder_name in os.listdir(source_base_dir):
    folder_path = os.path.join(source_base_dir, folder_name)
    
    if os.path.isdir(folder_path) and folder_name.startswith('data-'):
        print(f"\nProcessing folder: {folder_name}")
        
        dest_folder_path = os.path.join(destination_base_dir, folder_name)
        os.makedirs(dest_folder_path, exist_ok=True)
        print(f"Created destination folder: {dest_folder_path}")
        
        for file_name in os.listdir(folder_path):
            if file_name.endswith('.srt'):
                file_path = os.path.join(folder_path, file_name)
                print(f"\nProcessing file: {file_name}")
                
                with open(file_path, 'rb') as f:
                    raw_data = f.read()
                    result = chardet.detect(raw_data)
                    file_encoding = result['encoding']
                    print(f"Detected encoding: {file_encoding}, changing...")
                
                try:
                    with open(file_path, 'r', encoding=file_encoding) as f:
                        content = f.read()
                    print(f"Successfully changed (to UTF-8) file: {file_name}")
                except Exception as e:
                    print(f"Error reading {file_name} with encoding {file_encoding}: {e}")
                    continue  
                
                dest_file_path = os.path.join(dest_folder_path, file_name)
                with open(dest_file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"File saved as UTF-8 in: {dest_file_path}")

print("\nAll .srt files have been converted to UTF-8 and saved in 'data-encoded'.")
