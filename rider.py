import uvicorn
from fastapi import FastAPI
from src.web import rider  
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:8003",
]

app = FastAPI(swagger_ui_parameters={"displayModelsExpandDepth": -1})

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(rider.router, tags=["Rider"])  # Corrected syntax here

if __name__ == "__main__":
    uvicorn.run("rider:app", reload=True, host="0.0.0.0", port=8001)