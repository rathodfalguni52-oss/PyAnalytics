import csv
def export_to_csv(summary,group_by_result,output_path):
    with open(output_path,"w",newline="")as file:
        writer=csv.writer(file)
        writer.writerow(["Metric","Value"])
        for metric,value in summary.items():
            writer.writerow([metric,value])
        writer.writerow(["Group","Average"])
        for group,avg in group_by_result.items():
            writer.writerow([group,avg])