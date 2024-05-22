import glob
import shutil
import os

def move_all(destination_dir, format):
    current_dir = os.getcwd()
    destination_dir_log = os.path.join(current_dir, destination_dir)
    os.makedirs(destination_dir_log, exist_ok=True)
    json_files = glob.glob(os.path.join(current_dir, format))
    for file_path in json_files:
        shutil.move(file_path, destination_dir)

    print(f"All .json files moved to {destination_dir}")

#move_all('api-log', '*.json')
#move_all('json-base', '*.json')
