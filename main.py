from parsers.csv_parser import read_csv
from parsers.json_parser import read_json
from validators.input_validator import validate_file
from cli.interface import get_argument
from cleaners.data_cleaner import clean_data

def main():
    print("=========================")
    print("        PyAnalytics      ")
    print("=========================")
    args=get_argument()
    file_path=args.file

    is_valid,msg=validate_file(file_path)
    if not is_valid:
        print(f"Error:{msg}")

    else:
        if file_path.endswith(".csv"):
            data=read_csv(file_path)
            print("\nData loaded successfully")
            print("Original Data:")
            for row in data:
                print(row)

            data=clean_data(data)
            print("\nCleaned Data:")
            for row in data:
                print(row)

        elif file_path.endswith(".json"):
            data=read_json(file_path)
            print("\nData loaded successfully")
            for row in data:
                print(row)
                print()

        else:
            print("Unsupported file format")
            return




if __name__=="__main__":
    main()









# csv_data=read_csv("sample_data/students.csv")
# print(csv_data)

# json_data=read_json("sample_data/students.json")
# print(json_data)

# file_path="sample_data/students.json"
# valid,msg=validate_file(file_path)
# print(valid,"\n",msg)