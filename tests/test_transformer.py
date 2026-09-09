from transformers.data_transformer import(select_columns,rename_columns,filter_rows)

def test_select_columns():
    data=[
        {"Name":"Aisha","Age":20,"Marks":85},
    ]
    result=select_columns(data,["Name","Marks"])

    assert result[0]=={
        "Name":"Aisha",
        "Marks":85
    }

def test_rename_columns():
    data=[
        {"Name":"Aisha","Age":20,"Marks":85},
    ]
    result=rename_columns(data,{
    "Name":"Student_name",
    })
    assert result[0]["Student_name"]=="Aisha"

def test_filter_rows():
    data=[
        {"Name":"Aisha","Age":20,"Marks":85},
        {"Name":"Neha","Age":21,"Marks":75},
    ]
    result=filter_rows(data,"Marks",lambda marks:marks>=80)
    assert len(result)==1
    assert result[0]["Name"]=="Aisha"