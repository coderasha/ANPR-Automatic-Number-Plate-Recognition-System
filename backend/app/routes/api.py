from fastapi import APIRouter, UploadFile, File
from ..anpr import extract_number_plate

router = APIRouter()

@router.post("/analyze/")
async def analyze_plate(file: UploadFile = File(...)):
    content = await file.read()
    number = extract_number_plate(content)
    return {"plate_number": number}
