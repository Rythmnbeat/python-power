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

def movefile(srcPath, dest_folder):
    try:
        os.makedirs(dest_folder, exist_ok=True) #make path incase not already present
        shutil.move(srcPath, dest_folder)
    except Exception as e:
        print("Error moving file: {e}")


def logging(logged):
    try:
        with open("log.txt", "a") as log:
            log.write(logged + "\n")
    except Exception as e:
        print(f"Failed logging: {e}")

def main():
    
    folder_path = input("Enter folder path: ")

    if os.path.isdir(folder_path):
        print("Valid path!")
    else: 
        print("That folder does not exist.")
        return
    try:
        files = directory_scan(folder_path)
    except Exception as e:
        print(f"Error scanning directory: {e}")
    
    for file in files:
        full_path = os.path.join(folder_path, file)

        try:
            if os.path.isfile(full_path):
                categorize = filter_file(file)
                destination = os.path.join(folder_path, categorize)
                movefile(full_path, destination)
                logging(f"{file} moved to {categorize}")

        except PermissionError:
            print("Permission Denied")
            logging(f"failed to move {file}: Permission Denied")
        except FileNotFoundError:
            print(f"File: {file} cannot be found anymore")
            logging(f"failed to move {file}: File not found")
        except Exception as e:
            print(f"Unexpected error with {file}: {e}")
            logging(f"failed to move: {file} because {e}")

    print("Organizing completed")

if __name__ == "__main__":
    main()

