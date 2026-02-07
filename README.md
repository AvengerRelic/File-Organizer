# File Organizer

A simple Python script to keep your **Downloads** folder organized by automatically moving files into categorized subfolders based on their extensions.

## Features

The script organizes files into the following categories:

*   **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.svg`
*   **Documents**: `.pdf`, `.docx`, `.doc`, `.txt`, `.xlsx`, `.pptx`, `.csv`
*   **Audio**: `.mp3`, `.wav`, `.aac`, `.flac`
*   **Video**: `.mp4`, `.mov`, `.avi`, `.mkv`
*   **Archives**: `.zip`, `.rar`, `.7z`, `.tar`
*   **Executables**: `.exe`, `.msi`
*   **Others**: All other file types

## Requirements

*   Python 3.x

## Usage

1.  Clone the repository:
    ```bash
    git clone https://github.com/AvengerRelic/File-Organizer.git
    cd File-Organizer
    ```

2.  Run the script:
    ```bash
    python File_Organizer.py
    ```

The script will scan your `Downloads` directory and move files into their respective folders.

## Customization

You can modify the `file_types` dictionary in `File_Organizer.py` to add more categories or file extensions.
