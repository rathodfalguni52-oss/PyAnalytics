from fastapi import FastAPI
from api.routes import router

app=FastAPI(
    title="PyAnalytics API",
    description="REST API for the PyAnalytics data processing engine",
    version="1.0.0"
)

app.include_router(router)