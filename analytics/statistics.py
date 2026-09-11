def calculate_mean(values):
    if not values:
        return

    return sum(values)/len(values)

def calculate_median(values):
    if not values:
        return 0
    sorted_values=sorted(values)
    n=len(sorted_values)
    middle=n//2

    if n%2==1:
        return sorted_values[middle]

    return(
        sorted_values[middle-1]+sorted_values[middle]
    )/2

def calculate_percentile(values,percentile):
    if not values:
        return 0

    sorted_values=sorted(values)
    index=(percentile/100)*(len(sorted_values)-1)
    lower=int(index)
    upper=lower+1

    if upper>=len(sorted_values):
        return sorted_values[lower]
    fraction=index-lower
    return(
        sorted_values[lower]+fraction*(sorted_values[upper]-sorted_values[lower])
    )

def get_numeric_column(data,column):
    values=[]
    for row in data:
        value=row.get(column)
        if isinstance(value,(int,float)):
            values.append(value)
    return values

def calculation(data,column):
    values=get_numeric_column(data,column)

    if not values:
        return {}

    return{
        "count":len(values),
        "mean":calculate_mean(values),
        "median":calculate_mean(values),
        "25th_percentile":calculate_percentile(values,25),
        "50th_percentile":calculate_percentile(values,50),
        "75th_percentile":calculate_percentile(values,75)
    }

def group_by_mean(data,group_column,value_column):
    groups={}
    for row in data:
        group=row.get(group_column)
        value=row.get(value_column)
        if not isinstance(value,(int,float)):
            continue
        if group not in groups:
            groups[group]=[]
        groups[group].append(value)

    result={}
    for group,values in groups.items():
        result[group]=calculate_mean(values)

    return result

