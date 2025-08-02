from fastapi import FastAPI
from .routes import api
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(api)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change to frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
