#The start of project
import os
import shutil


def directory_scan(folder_path):
    print(f"scanning {folder_path}")
    return os.listdr(folder_path)

def filter_file(filename):
    extention = filename.split(".")[-1].lower() #pull file extention part/making them lower case
    if extention in ["jpeg", "jpg", "png", "gif"]:
        return "images"
    elif extention in ["pdf", "docx", "txt"]:
        return "documents"
    elif extention in ["mp3", "wav", "AIFF", "AAC"]:
        return "audio"
    else:
        return "other"

def movefile(srcPath, dest_folder):
    os.makedirs(dest_folder, exist_ok=True) #make path incase not already present
    shutil.move(srcPath, dest_folder)

def logging(logger)
    with open("log.txt", "a") as log:
        log.write(logger, + "\n")

def main():
    
    folder_path = input("Enter folder path: ")

    if os.path.isdir(folder_path):
        print("Valid path!")
    else: 
        print("That folder does not exist.")
    
    files = directory_scan(folder_path)

    for file in files:
        full_path = os.path.join(folder_path, file)

        if os.path.isfile(full_path):
            categorize = filter_file(file)
            destination = os.path.join(folder_path, categorize)
            movefile(full_path, destination)
            logging(f"{file} moved to {categorize}")

    print("Organizing complete")

if __name__ == "__main__":
    main()

