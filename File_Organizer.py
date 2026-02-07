import os
import shutil
from pathlib import Path

def organize_downloads():
    # Path to your downloads folder
    download_path = Path.home() / "Downloads"
    
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
                shutil.move(str(file_path), str(dest_dir / file_path.name))
                print(f"Moved: {file_path.name} -> {category}")
                moved = True
                break
        
        # Optional: Move unknown types to an 'Others' folder
        if not moved:
            others_dir = download_path / "Others"
            others_dir.mkdir(exist_ok=True)
            shutil.move(str(file_path), str(others_dir / file_path.name))

if __name__ == "__main__":
    organize_downloads()
    print("Cleanup complete!")