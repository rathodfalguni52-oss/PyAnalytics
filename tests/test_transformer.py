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



# data=[
#     {"Name":"Aisha","Age":20,"Marks":85,"Department":"IT"},
#     {"Name":"Rahul","Age":21,"Marks":90,"Department":"IT"},
#     {"Name":"Neha","Age":21,"Marks":75,"Department":"CS"},
# ]

# print("Original Data:")
# for row in data:
#     print(row)

# print("\nSelected Columns:")
# result=select_columns(data,["Name","Marks"])
# for row in result:
#     print(row)

# print("\nRenamed Columns:")
# result=rename_columns(data,{
#     "Name":"Student_name",
#     "Marks":"Score"
#     })
# for row in result:
#     print(row)

# print("\nFiltered Data:")
# result=filter_rows(data,"Marks",lambda marks:isinstance(marks,int) and marks>=80)
# for row in result:
#     print(row)