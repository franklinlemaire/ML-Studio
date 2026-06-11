from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import dataset

app = FastAPI(title="ML Studio API", version="1.0.0")

# Autorise le frontend React (port 5173) à parler au backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(dataset.router)


@app.get("/")
def root():
    return {"message": "ML Studio API — opérationnelle 🚀"}