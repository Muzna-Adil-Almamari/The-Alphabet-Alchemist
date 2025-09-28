from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from Alphabet_Alchemist_func import convert_measurements
from typing import List
import uvicorn
import logging


app = FastAPI(title="Alphabet Alchemist API",
              description="Convert encoded strings into measurement values",
              version="0.0.1")


# Logging setup
logging.basicConfig(
    filename="logs/app.log",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)


@app.get("/convert-measurements", response_model=List[int])
def convert_measurements_api(input: str = Query(..., description="Encoded input string")):
    """
    Convert input string into list of measured inflows.
    Example: GET /convert-measurements?input=abbcc → [2, 6]
    """
    try:
        result = convert_measurements(input)
        logging.info(f"Input: {input} → Output: {result}")
        return JSONResponse(content=result, status_code=200)
    except Exception as e:
        logging.error(f"Error converting input '{input}': {e}")
        return JSONResponse(content={"error": str(e)}, status_code=500)




if __name__ == "__main__":
    uvicorn.run("main_app:app", host="0.0.0.0", port=8888, reload=True)

