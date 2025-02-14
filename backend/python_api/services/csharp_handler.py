import os
from fastapi.responses import FileResponse

DESIGN_FILES_DIR = "design_files/"

def get_design_file():
    """Simulates retrieving a .dwg design file from C# backend."""
    latest_file = os.path.join(DESIGN_FILES_DIR, "output.dwg")
    
    if os.path.exists(latest_file):
        return FileResponse(latest_file, media_type="application/acad", filename="design.dwg")
    else:
        return {"error": "No design file available"}
