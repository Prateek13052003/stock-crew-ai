from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime
import logging
import os
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
    analysis: str

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
            analysis=result.raw
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