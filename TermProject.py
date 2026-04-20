#The start of project
import os
import shutil


def directory_scan(folder_path):
    try:
        print(f"scanning {folder_path}")
        return os.listdir(folder_path)
    except Exception as e:
        raise e


def filter_file(filename):
    extention = filename.split(".")[-1].lower() #pull file extention part/making them lower case
    if extention in ["jpeg", "jpg", "png", "gif"]:
        return "images"
    elif extention in ["pdf", "docx", "txt"]:
        return "documents"
    elif extention in ["mp3", "wav", "aiff", "aac"]:
        return "audio"
    else:
        return "other"

def move_file(srcPath, dest_folder):
    try:
        os.makedirs(dest_folder, exist_ok=True) #make path incase not already present
        shutil.move(srcPath, dest_folder)
    except Exception as e:
        print(f"Error moving file: {e}")
        raise e


def log_Action(logged):
    try:
        with open("log.txt", "a") as log:
            log.write(logged + "\n")
    except Exception as e:
        print(f"Failed logging: {e}")

def main():
    
    folder_path = input("Enter folder path: ")
    folder_path = folder_path.strip().replace("\\", "/")
    print(folder_path)
    if os.path.isdir(folder_path):
        print("Valid path!")
    else: 
        print("That folder does not exist.")
        return
    try:
        files = directory_scan(folder_path)
    except Exception as e:
        print(f"Error scanning directory: {e}")
        return 
    
    for file in files:
        full_path = os.path.join(folder_path, file)

        if os.path.isfile(full_path):
            try:
                categorize = filter_file(file)
                destination = os.path.join(folder_path, categorize)
                move_file(full_path, destination)
                log_Action(f"{file} moved to {categorize}")

            except PermissionError:
                print("Permission Denied")
                log_Action(f"failed to move {file}: Permission Denied")
            except FileNotFoundError:
                print(f"File: {file} cannot be found anymore")
                log_Action(f"failed to move {file}: File not found")
            except Exception as e:
                print(f"Unexpected error with {file}: {e}")
                log_Action(f"failed to move: {file} because {e}")

    print("Organizing completed")

if __name__ == "__main__":
    main()

