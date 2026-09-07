def remove_duplicates(data):
    clean_data=[]
    for row in data:
        if row not in clean_data:
            clean_data.append(row)
    return clean_data

def handle_missing_values(data):
    for row in data:
        for key,value in row.items():
            if value is None or value == "":
                row[key]="Unknown"
    return data

def cast_numeric_values(data):
    for row in data:
        for key,value in row.items():
            if key in ["Age","Marks"]:
                try:
                    row[key]=int(value)
                except(ValueError,TypeError):
                    pass
    return data

def clean_data(data):
    data=remove_duplicates(data)
    data=handle_missing_values(data)
    data=cast_numeric_values(data)

    return data
