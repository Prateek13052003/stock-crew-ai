from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime
from fastapi.middleware.cors import CORSMiddleware
import logging
from typing import Any
import os
from fastapi.responses import FileResponse
from pathlib import Path
import json
import traceback
import time

from stock.crew import StockPicker

# ============================================================
# Configuration
# ============================================================

REQUEST_TIMEOUT_SECONDS = int(
    os.getenv("REQUEST_TIMEOUT_SECONDS", "120")
)

APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

# ============================================================
# Logging
# ============================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)

logger = logging.getLogger(__name__)

# ============================================================
# FastAPI App
# ============================================================

app = FastAPI(
    title="Stock Crew AI API",
    version=APP_VERSION,
    description="AI-powered stock research and analysis using CrewAI + Groq + Serper"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ============================================================
# Request Models
# ============================================================

class AnalyzeRequest(BaseModel):
    sector: str = Field(
        default="Technology",
        min_length=2,
        max_length=100,
        description="Sector to analyze"
    )

# ============================================================
# Response Models
# ============================================================

class AnalyzeResponse(BaseModel):
    success: bool
    sector: str
    generated_at: str
    execution_time_seconds: float
    analysis: Any

class ErrorResponse(BaseModel):
    success: bool
    error: str
    message: str

# ============================================================
# Routes
# ============================================================

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "stock-crew-ai",
        "version": APP_VERSION,
        "timestamp": datetime.utcnow().isoformat()
    }


@app.post(
    "/analyze",
    response_model=AnalyzeResponse,
    responses={
        500: {
            "model": ErrorResponse
        }
    }
)
def analyze(request: AnalyzeRequest):

    start_time = time.time()

    logger.info(
        f"Analysis request received | sector={request.sector}"
    )

    try:

        result = StockPicker().crew().kickoff(
            inputs={
                "sector": request.sector,
                "current_date": str(datetime.now())
            }
        )

        execution_time = round(
            time.time() - start_time,
            2
        )

        logger.info(
            f"Analysis completed | sector={request.sector} | duration={execution_time}s"
        )

        return AnalyzeResponse(
            success=True,
            sector=request.sector,
            generated_at=datetime.utcnow().isoformat(),
            execution_time_seconds=execution_time,
            analysis=json.loads(result.raw) 
        )

    except Exception as e:

        logger.error(
            f"Analysis failed | sector={request.sector}"
        )

        logger.error(traceback.format_exc())

        raise HTTPException(
            status_code=500,
            detail={
                "success": False,
                "error": type(e).__name__,
                "message": str(e)
            }
        )


@app.get("/download-pdf")
def download_pdf():

    output_dir = Path("output")

    if not output_dir.exists():
        raise HTTPException(
            status_code=404,
            detail="No reports generated yet."
        )

    pdf_files = sorted(
        output_dir.glob("*.pdf"),
        key=lambda f: f.stat().st_mtime,
        reverse=True,
    )

    if not pdf_files:
        raise HTTPException(
            status_code=404,
            detail="No PDF found."
        )

    latest_pdf = pdf_files[0]

    return FileResponse(
        latest_pdf,
        media_type="application/pdf",
        filename=latest_pdf.name,
    )
