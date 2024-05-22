import os
import glob

def delete_json_files(directory):

    json_files = glob.glob(os.path.join(directory, '**', '*.json'), recursive=True)


    if not json_files:
        print("No .json files found.")
        return


    for json_file in json_files:
        try:
            os.remove(json_file)
            print(f"Deleted: {json_file}")
        except Exception as e:
            print(f"Error deleting {json_file}: {e}")

if __name__ == "__main__":
   
    current_directory = os.getcwd()
    
    delete_json_files(current_directory)
