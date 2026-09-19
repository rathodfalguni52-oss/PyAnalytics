from fastapi import APIRouter,UploadFile,File
import os
import tempfile
from typing import Any
from pydantic import BaseModel
from cleaners.data_cleaner import clean_data
from analytics.statistics import calculation,group_by_mean
from parsers.csv_parser import read_csv
from parsers.json_parser import read_json
from validators.input_validator import validate_file

class AnalyzeRequest(BaseModel):
    data:list[dict[str,Any]]

router=APIRouter()

@router.get("/")
def root():
    return{"message":"Welcome to PyAnalytics Api"}

@router.get("/health")
def health_check():
    return{"status":"healthy"}

@router.post("/analyze")
def analyze_data(request:AnalyzeRequest):
    data=request.data
    cleaned_data=clean_data(data)

    summary=calculation(cleaned_data,"Marks")

    grouped=group_by_mean(cleaned_data,"Department","Marks")

    return{
        "clean_data":cleaned_data,
        "Statistical_summary":summary,
        "average_marks_by_department":grouped
    }

@router.post("/upload")
async def upload_file(file:UploadFile =File(...)):
    if not file.filename:
        return{"error":"No file selected"}

    extension=os.path.splitext(file.filename)[1].lower()
    if extension not in["csv","json"]:
        return{
            "Error":"Unsupported file type.Only CSV and JSON files are supported."
        }

    contents=await file.read()
    if not contents:
        return{"Error":"Uplaoded file is empty"}

    temp_fd,temp_path=tempfile.mkstemp(suffix=extension)

    try:
        with os.fdopen(temp_fd,"wb")as temp_file:
            temp_file.write(contents)

        is_valid,message=validate_file(temp_path)
        if not is_valid:
            return{"Error":message}
        if extension=="csv":
            data=read_csv(temp_path)
        else:
            data=read_json(temp_path)

        if not data:
            return{"Error":"No data could be loaded from the file"}

        cleaned_data=clean_data(data)

        summary=calculation(cleaned_data,"Marks")

        grouped=group_by_mean(cleaned_data,"Department","Marks")

        return{
            "File name":file.filename,
            "Message":"File uploaded and analyzed successfully",
            "Cleaned Data":cleaned_data,
            "Statistical summary":summary,
            "Average Marks by Department":grouped
        }
    finally:
        if os.path.exists(temp_path):
            os.remove(temp_path)

