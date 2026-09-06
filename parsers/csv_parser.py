import csv

def read_csv(file_path:str)->list:
    print(f"Reading file:{file_path}")
    print(f"File:{file_path}")
    print("Format:CSV")
    try:
        with open(file_path,"r",newline="") as f:
            reader=csv.DictReader(f)
            data=list(reader)
        return data

    except FileNotFoundError:
        print("Error:CSV file not found.")

    except PermissionError:
        print("Error:Permission denied.")

    except Exception as e:
        print(f"Error reading CSV file:{e}")
        
    return []

