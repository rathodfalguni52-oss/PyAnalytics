import os
from exporters.markdown_exporter import export_to_markdown
from exporters.csv_exporter import export_to_csv

def test_markdown_export(tmp_path):
    summary={"count":2,"mean":85}
    grouped={"IT":85}
    output_file=tmp_path/"summary.md"
    export_to_markdown(summary,grouped,output_file)
    assert output_file.exists()
    content=output_file.read_text()
    assert "PyAnalytics Statistical Summary" in content


def test_csv_export(tmp_path):
    summary={"count":2,"mean":85}
    grouped={"IT":85}
    output_file=tmp_path/"summary.csv"
    export_to_csv(summary,grouped,output_file)
    assert output_file.exists()
    # content=output_file.read_text()
    # assert "PyAnalytics Statistical Summary" in content

