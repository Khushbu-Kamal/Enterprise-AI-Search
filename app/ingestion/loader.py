from pathlib import Path

SUPPORTED_EXTENSIONS = [".pdf", ".md", ".txt"]

def scan_documents(folder_path):

    files = []

    for file in Path(folder_path).rglob("*"):

        if file.suffix.lower() in SUPPORTED_EXTENSIONS:
            files.append(str(file))

    return files