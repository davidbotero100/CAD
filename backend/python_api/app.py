from fastapi import FastAPI
from fastapi.responses import FileResponse
import json

# create instance of FastAPI
app = FastAPI()

# Basic FastAPT routes and functions ---------------------------------
# create a route
@app.get("/")

# define a function to read the root
def read_root():
    return {"Message": "Welcome to the FastAPI Backend!"}

# What is a route? - A route is a URL path to access the API endpoint.
@app.get("/designs")
def get_designs():
    return {"designs": ["Design 1", "Design 2"]}

# Basic FastAPT routes and functions ---------------------------------

# AutoCAD Civil3D API routes and functions ---------------------------
@app.get("/designs/2d")
def get_2d_designs():
    with open("example_2d.json") as f:
        return json.load(f)
    
@app.get("/designs/3d")
def get_3d_designs():
    return FileResponse("example.dwg", media_type="application/acad")

    



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
