from fastapi import APIRouter
from models import DesignPrompt, DesignResponse
from ..services.csharp_handler import get_design_file
from ..services.crewai_handler import send_to_crewai

router = APIRouter()

@router.post("/submit-prompt/", response_model=DesignResponse)
async def submit_prompt(data: DesignPrompt):
    """Receives prompt, sends to CrewAI, and retrieves design from C# backend."""
    ai_response = send_to_crewai(data.prompt)
    return {"message": f"Processed: {ai_response}", "file_url": "/get-design/"}

@router.get("/get-design/")
async def get_design():
    """Returns the design file to the frontend."""
    return get_design_file()
