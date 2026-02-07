import os
import shutil
from pathlib import Path

def organize_downloads(path=None):
    # Path to your downloads folder
    if path is None:
        download_path = Path.home() / "Downloads"
    else:
        download_path = Path(path)
    
    # Define mapping of file types to folder names
    file_types = {
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg"],
        "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".pptx", ".csv"],
        "Audio": [".mp3", ".wav", ".aac", ".flac"],
        "Video": [".mp4", ".mov", ".avi", ".mkv"],
        "Archives": [".zip", ".rar", ".7z", ".tar"],
        "Executables": [".exe", ".msi"],
    }

    for file_path in download_path.iterdir():
        # Skip directories and the script itself
        if file_path.is_dir() or file_path.name == "organizer.exe":
            continue
            
        file_ext = file_path.suffix.lower()
        moved = False

        for category, extensions in file_types.items():
            if file_ext in extensions:
                dest_dir = download_path / category
                dest_dir.mkdir(exist_ok=True)
                
                dest_path = dest_dir / file_path.name
                if dest_path.exists():
                    base = dest_path.stem
                    suffix = dest_path.suffix
                    counter = 1
                    while dest_path.exists():
                        dest_path = dest_dir / f"{base} ({counter}){suffix}"
                        counter += 1
                
                shutil.move(str(file_path), str(dest_path))
                print(f"Moved: {file_path.name} -> {dest_path.name}")
                moved = True
                break
        
        # Optional: Move unknown types to an 'Others' folder
        # Optional: Move unknown types to an 'Others' folder
        if not moved:
            others_dir = download_path / "Others"
            others_dir.mkdir(exist_ok=True)
            
            dest_path = others_dir / file_path.name
            if dest_path.exists():
                base = dest_path.stem
                suffix = dest_path.suffix
                counter = 1
                while dest_path.exists():
                    dest_path = others_dir / f"{base} ({counter}){suffix}"
                    counter += 1
                    
            shutil.move(str(file_path), str(dest_path))
            print(f"Moved: {file_path.name} -> Others/{dest_path.name}")

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Organize files in a directory based on their extensions.")
    parser.add_argument("directory", nargs="?", help="The directory to organize. Defaults to the Downloads folder.")
    args = parser.parse_args()
    
    organize_downloads(args.directory)
    print("Cleanup complete!")