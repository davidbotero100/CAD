from pydantic import BaseModel

class DesignPrompt(BaseModel):
    prompt: str

class DesignResponse(BaseModel):
    message: str
    file_url: str  # URL to access the design file
