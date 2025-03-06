import os


def readFiles(directory: str = "/tmp/files") -> str:
    """
    Reads all .html files from a directory, concatenates their contents,
    and returns a single string.
    """
    dir_path = os.path.abspath(directory)
    combined_html = ""

    if not os.path.isdir(dir_path):
        return combined_html

    for file_name in os.listdir(dir_path):
        if file_name.lower().endswith(".html"):
            file_path = os.path.join(dir_path, file_name)
            if os.path.isfile(file_path):
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                combined_html += content + "\n\n"
    return combined_html
