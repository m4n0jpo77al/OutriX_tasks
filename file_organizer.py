import os
import shutil

# Define the path to organize (use absolute path or '.' for current directory)
TARGET_DIRECTORY = input("Enter the path to organise:") 
TARGET_DIRECTORY = TARGET_DIRECTORY.strip() if TARGET_DIRECTORY else "."

# Define file type categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".odt", ".rtf"],
    "Spreadsheets": [".xls", ".xlsx", ".csv"],
    "Presentations": [".ppt", ".pptx"],
    "Audio": [".mp3", ".wav", ".aac", ".ogg", ".flac"],
    "Videos": [".mp4", ".avi", ".mov", ".mkv", ".wmv"],
    "Archives": [".zip", ".rar", ".tar", ".gz", ".7z"],
    "Scripts": [".py", ".js", ".html", ".css", ".php"],
    "Executables": [".exe", ".msi", ".bat", ".sh"],
    "Others": []
}

def create_folder(folder_name):
    """Creates a folder if it doesn't exist"""
    folder_path = os.path.join(TARGET_DIRECTORY, folder_name)
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    return folder_path

def get_category(file_ext):
    """Returns the folder category for a given file extension"""
    for category, extensions in FILE_TYPES.items():
        if file_ext.lower() in extensions:
            return category
    return "Others"

def organize_files():
    """Organizes files into folders based on their file type"""
    for file in os.listdir(TARGET_DIRECTORY):
        file_path = os.path.join(TARGET_DIRECTORY, file)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file)
            category = get_category(ext)
            destination_folder = create_folder(category)

            try:
                shutil.move(file_path, os.path.join(destination_folder, file))
                print(f"Moved: {file} → {category}/")
            except Exception as e:
                print(f"Failed to move {file}: {e}")

if __name__ == "__main__":
    print("Organizing files...")
    organize_files()
    print("Done!")
