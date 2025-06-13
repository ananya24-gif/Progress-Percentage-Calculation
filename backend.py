from fastapi import FastAPI, UploadFile, File
from fastapi.responses import JSONResponse
from uuid import uuid4
from pathlib import Path
import shutil

app = FastAPI()
UPLOAD_DIR = Path("/mnt/data/uploads")
UPLOAD_DIR.mkdir(parents=True, exist_ok=True)


@app.post("/upload/plan/")
async def upload_plan(file: UploadFile = File(...)):
    plan_id = str(uuid4())
    file_path = UPLOAD_DIR / f"{plan_id}_plan_{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {
        "message": "Plan uploaded successfully",
        "plan_id": plan_id,
        "filename": str(file_path),
    }


@app.post("/upload/site-image/")
async def upload_site_image(file: UploadFile = File(...)):
    image_id = str(uuid4())
    file_path = UPLOAD_DIR / f"{image_id}_site_{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    return {
        "message": "Site image uploaded successfully",
        "image_id": image_id,
        "filename": str(file_path),
    }


@app.get("/analyze/progress/")
async def analyze_progress(plan_id: str, image_id: str):
    # Placeholder logic for progress estimation
    # Replace with VLM model inference (e.g., LLaVA) in production
    progress_estimate = 68  # Example percentage
    return JSONResponse(
        content={
            "plan_id": plan_id,
            "image_id": image_id,
            "estimated_progress": f"{progress_estimate}%",
            "status": "Partial Completion",
            "insights": "Ground floor completed. Columns and slabs placed for 1st floor.",
        }
    )
