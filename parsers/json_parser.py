import json

def read_json(file_path:str)->list:
    print(f"Reading file:{file_path}")
    print(f"File:{file_path}")
    print("Format:JSON")

    try:
        with open(file_path,"r",newline="")as f:
            reader=json.load(f)
            data=list(reader)
        return [data]
    except FileNotFoundError:
        print("Error:JSON file not found")

    except json.JSONDecodeError:
        print("Error:Invalid JSON format")

    except PermissionError:
        print("Error:Permission denied")

    except Exception as e:
        print(f"Error reading JSON file:{e}")

    return []
