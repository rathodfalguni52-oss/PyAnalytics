from parsers.csv_parser import read_csv
from parsers.json_parser import read_json
from cleaners.data_cleaner import(remove_duplicates,handle_missing_values,cast_numeric_values)

def test_csv_parser():
    data=read_csv("sample_data/students.csv")

    assert len(data)>0
    assert "Name" in data[0]

# def test_json_parser():
#     data=read_csv("sample_data/students.json")

#     assert len(data)>0
#     assert "Name" in data[0]

def test_remove_duplicated():
    data=[
        {"Name":"Aisha","Age":"20"},
        {"Name":"Aisha","Age":"20"} 
    ]
    result=remove_duplicates(data)

    assert len(result)==1

def test_handle_missing_values():
    data=[
        {"Name":"Rahul","Age":""}
    ]
    result=remove_duplicates(data)
    assert len(result)==1

def test_cast_numeric_values():
    data=[
            {"Name":"Aisha","Age":"20","Marks":"85"}
        ]
    result=cast_numeric_values(data)

    assert result[0]["Age"]==20
    assert result[0]["Marks"]==85


