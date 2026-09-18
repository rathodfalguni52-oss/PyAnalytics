from fastapi import APIRouter
from typing import Any
from pydantic import BaseModel
from cleaners.data_cleaner import clean_data
from analytics.statistics import calculation,group_by_mean

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