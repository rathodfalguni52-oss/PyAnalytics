from analytics.statistics import calculation,group_by_mean
from exporters.markdown_exporter import export_to_markdown
from exporters.csv_exporter import export_to_csv

data=[
    {"Name":"Aisha","Marks":85,"Department":"IT"},
    {"Name":"Rahule","Marks":90,"Department":"IT"},
    {"Name":"Neha","Marks":75,"Department":"CS"},
    {"Name":"Priya","Marks":92,"Department":"IT"},
    {"Name":"Rohan","Marks":80,"Department":"CS"}
]
summary=calculation(data,"Marks")
grouped=group_by_mean(data,"Department","Marks")
export_to_markdown(summary,grouped,"output/summary.md")
export_to_csv(summary,grouped,"output/summary.csv")

print("Report generated Successfully!")