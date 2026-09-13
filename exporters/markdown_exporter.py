def export_to_markdown(summary,group_by_result,output_path):
    with open(output_path,'w')as file:
        file.write("#PyAnalytics Statistical Summary\n\n")
        file.write("##Overall Statistics\n\n")
        file.write('|Metric|Value|\n')
        file.write("|-----|-----|\n")
        for metric,value in summary.items():
            file.write(f"|{metric}|{value}|\n")
        file.write("\n##Group by Statistics")
        file.write("|Group|Average|\n")
        file.write("|-----|-----|\n")
        for group,avg in group_by_result.items():
            file.write(f"|{group}|{avg}|\n")
