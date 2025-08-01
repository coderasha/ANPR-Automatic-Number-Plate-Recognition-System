from fastapi import FastAPI, UploadFile, File
from .routes import api

app = FastAPI(title="ANPR Platform")
app.include_router(api.router)
