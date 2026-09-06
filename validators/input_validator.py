import os

def validate_file(file_path):
    if not os.path.exists(file_path):
        return False,"File does not exist"

    if not os.path.isfile(file_path):
        return False,"The given path is not a file"

    extention=os.path.splitext(file_path)[1].lower()

    if extention not in[".csv",".json"]:
        return False,"Unsupported file type.Only CSV and JSON are supported."

    if os.path.getsize(file_path)==0:
        return False,"File is empty."

    return True,"File is valid."