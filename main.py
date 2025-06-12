# main.py
from fastapi import FastAPI, Query
from pydantic import BaseModel
import googlemaps
import os


app = FastAPI()

GOOGLE_MAPS_API = "XXXXXXXXX"

maps = googlemaps.Client(GOOGLE_MAPS_API)

# Define a Pydantic model for request/response bodies 
# (optional but good practice)
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


@app.get("/")
async def root():
    """
    A simple root endpoint that returns a greeting.
    """
    return {"message": "Hello from FastAPI on Cloud Run!"}


@app.get("/query")
async def query(
        query: str = Query(..., min_length=3, max_length=50, description="The search string")
    ):
    """
    """
    textquery = query.lower()

    result = maps.find_place(
        "restaurant",
        textquery,
        fields=["business_status", "geometry/location", "place_id"],
        location_bias="point:90,90",
        language="en-US",
    )

    print(result)

    return {"message": result}


# The Cloud Run environment will set 
# the PORT environment variable.
if __name__ == "__main__":
    import uvicorn
    # Use 0.0.0.0 to listen on all available interfaces, as required by Cloud Run
    # Get port from environment variable, default to 8000 for local development
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
