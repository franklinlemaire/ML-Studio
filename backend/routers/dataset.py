import io
import pandas as pd
from fastapi import APIRouter, UploadFile, File, HTTPException
from services.analyzer import analyze_dataset

router = APIRouter(prefix="/dataset", tags=["dataset"])

# Taille max autorisée : 20 Mo
MAX_SIZE = 20 * 1024 * 1024


@router.post("/upload")
async def upload_dataset(file: UploadFile = File(...)):
    # Vérification du type de fichier
    if not file.filename.endswith(".csv"):
        raise HTTPException(400, detail="Seuls les fichiers CSV sont acceptés pour l'instant.")

    content = await file.read()

    if len(content) > MAX_SIZE:
        raise HTTPException(400, detail="Fichier trop volumineux (max 20 Mo).")

    try:
        # Détection automatique du séparateur (virgule ou point-virgule)
        df = pd.read_csv(io.BytesIO(content), sep=None, engine="python")
    except Exception as e:
        raise HTTPException(422, detail=f"Impossible de lire le fichier : {str(e)}")

    result = analyze_dataset(df)
    result["filename"] = file.filename

    return result


@router.get("/ping")
def ping():
    return {"status": "ok"}