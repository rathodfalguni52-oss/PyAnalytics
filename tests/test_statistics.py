from analytics.statistics import(calculate_mean,calculate_median,calculate_percentile,calculation,group_by_mean)

def test_mean():
    values=[10,20,30]

    assert calculate_mean(values)==20

def test_median():
    values=[10,20,30]
    assert calculate_median(values)==20

def test_median_even():
    values=[10,20,30,40]
    assert calculate_median(values)==25

def test_percentile():
    values=[10,20,30,40,50]
    assert calculate_percentile(values,50)==30

def test_calculation():
    data=[
        {"Name":"Aisha","Marks":80},
        {"Name":"Rahul","Marks":90}
    ]
    result=calculation(data,"Marks")
    assert result["count"]==2
    assert result["mean"]==85
    assert result["median"]==85

def test_group_by_mean():
    data=[
        {"Department":"IT","Marks":80},
        {"Department":"IT","Marks":90},
        {"Department":"CS","Marks":70}
    ]
    result=group_by_mean(data,"Department","Marks")
    assert result["IT"]==85
    assert result["CS"]==70