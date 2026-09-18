from parsers.csv_parser import read_csv
from parsers.json_parser import read_json
from validators.input_validator import validate_file
from cli.interface import get_argument
from cleaners.data_cleaner import clean_data
from transformers.data_transformer import(select_columns,rename_columns,filter_rows)
from analytics.statistics import calculation,group_by_mean
from exporters.markdown_exporter import export_to_markdown
from exporters.csv_exporter import export_to_csv


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
        if file_path.lower().endswith(".csv"):
            data=read_csv(file_path)
            print("Original Data:")
            for row in data:
                print(row)
                

        elif file_path.lower().endswith(".json"):
            data=read_json(file_path)

        else:
            print("Error:Unsupported file format")
            return
        print("\nData loaded successfully")

        #Clean data
        data=clean_data(data)
        print("\nData cleaned Successfully!")
        print("\nCleaned Data:")
        for row in data:
            print(row)

        
        summary=calculation(data,"Marks")
        grouped=group_by_mean(data,"Department","Marks")

        #Display Summary
        print("\nStatistical Summary:")
        for key,value in summary.items():
            print(f"{key}:{value}")

        #Display group by results
        print("\nAverage marks by department:")
        for department,average in grouped.items():
                print(f"{department}:{average}")

        #Export reports
        export_to_markdown(summary,grouped,"output/summary.md")
        export_to_csv(summary,grouped,"output/summary.csv")
        print("\nReports generated generated successfully!")
        print("Markdown:output/summary.md")
        print("CSV:output/summary.csv")


if __name__=="__main__":
    main()









# csv_data=read_csv("sample_data/students.csv")
# print(csv_data)

# json_data=read_json("sample_data/students.json")
# print(json_data)

# file_path="sample_data/students.json"
# valid,msg=validate_file(file_path)
# print(valid,"\n",msg)