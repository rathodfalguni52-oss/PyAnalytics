from PyAnalytics.parsers.csv_parser import read_csv
from PyAnalytics.parsers.json_parser import read_json
from PyAnalytics.validators.input_validator import validate_file
from cli.interface import get_argument

def main():
    args=get_argument()

    file_path=args.file

    if file_path.endswith(".csv"):
        data=read_csv(file_path)

    elif file_path.endswith(".json"):
        data=read_json(file_path)

    else:
        print("Unsupported file format")
        return

    print("\nData loaded successfully")
    print(data)

if __name__=="__main__":
    main()









# csv_data=read_csv("sample_data/students.csv")
# print(csv_data)

# json_data=read_json("sample_data/students.json")
# print(json_data)

# file_path="sample_data/students.json"
# valid,msg=validate_file(file_path)
# print(valid,"\n",msg)