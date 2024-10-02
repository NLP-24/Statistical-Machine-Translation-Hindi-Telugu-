import os

base_dir = 'Statistical-Machine-Translation-Hindi-Telugu-\data'  # Replace with your base directory path

# Get a list of all folders starting with 'data-'
folders = [f for f in os.listdir(base_dir) if os.path.isdir(os.path.join(base_dir, f)) and f.startswith('data-')]

# Function to check if a file follows the required pattern
def check_srt_files_in_folder(folder_name, hin_file, tel_file):
    errors = []
    
    # Check if hin-x.srt exists
    if not hin_file.endswith('.srt'):
        errors.append(f"ERROR: {hin_file} is not an .srt file.")
    if not tel_file.endswith('.srt'):
        errors.append(f"ERROR: {tel_file} is not an .srt file.")
        
    return errors

for folder in folders:
    folder_path = os.path.join(base_dir, folder)
    
    # Extract 'x' from folder name 'data-x'
    folder_number = folder.split('-')[-1]

    expected_hin_file = f"hin-{folder_number}.srt"
    expected_tel_file = f"tel-{folder_number}.srt"
    
    folder_files = os.listdir(folder_path)
    
    hin_file = os.path.join(folder_path, expected_hin_file)
    tel_file = os.path.join(folder_path, expected_tel_file)
    
    errors = []
    
    if expected_hin_file not in folder_files:
        errors.append(f"ERROR: Missing file {expected_hin_file} in {folder}.")
    if expected_tel_file not in folder_files:
        errors.append(f"ERROR: Missing file {expected_tel_file} in {folder}.")
    
    if expected_hin_file in folder_files and expected_tel_file in folder_files:
        errors += check_srt_files_in_folder(folder, expected_hin_file, expected_tel_file)

    if errors:
        print(f"Issues in folder '{folder}':")
        for error in errors:
            print(f"  - {error}")
    else:
        print(f"Folder '{folder}' is valid.")

print("File format checking completed.")
