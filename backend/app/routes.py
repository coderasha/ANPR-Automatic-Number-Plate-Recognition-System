from fastapi import APIRouter, File, UploadFile
from .anpr import extract_number_plate

api = APIRouter()

@api.post("/extract")
async def extract(file: UploadFile = File(...)):
    contents = await file.read()
    number = extract_number_plate(contents)
    return {"number_plate": number}
