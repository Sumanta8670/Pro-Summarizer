from fastapi import FastAPI
import uvicorn
import sys
import os
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from fastapi.responses import Response
from fastapi import Query
from fastapi import HTTPException
from Pro_Summerizer.pipeline.prediction import PredictionPipeline

text:str = "what is Text Summarization?"

app = FastAPI()

@app.get("/", tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")

@app.get("/train", tags=["training"])
async def train_route():
    try:
        os.system("python main.py")
        return Response("Training successful !!")
    except Exception as e:
        return Response(f"Error Occurred! {e}")

@app.post("/predict", tags=["prediction"])
async def predict_route(text: str = Query(..., description="Input text to summarize")):
    try:
        obj = PredictionPipeline()
        result = obj.predict(text)
        return {"summary": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)