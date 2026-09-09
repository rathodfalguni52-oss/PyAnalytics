def select_columns(data,columns):
    transformed_data=[]

    for row in data:
        new_row={}

        for column in columns:
            if column in row:
                new_row[column]=row[column]
        transformed_data.append(new_row)

    return transformed_data

def rename_columns(data,column_mapping):
    transformed_data=[]

    for row in data:
        new_row={}
        for key,value in row.items():
            new_key=column_mapping.get(key,key)
            new_row[new_key]=value
        transformed_data.append(new_row)
    return transformed_data

def filter_rows(data,column,condition):
    filterd_data=[]
    for row in data:
        value=row.get(column)
        if condition(value):
            filterd_data.append(row)
    return filterd_data

