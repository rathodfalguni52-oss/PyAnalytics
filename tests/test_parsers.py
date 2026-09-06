from parsers.csv_parser import read_csv
from parsers.json_parser import read_json

def test_csv_parser():
    data=read_csv("sample_data/students.csv")

    assert len(data)>0
    assert "Name" in data[0]

def test_json_parser():
    data=read_csv("sample_data/students.json")

    assert len(data)>0
    assert "Name" in data[0]


