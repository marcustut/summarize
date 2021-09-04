from fastapi import FastAPI, HTTPException
from summarize.ai import naive

METHODS = ["naive", "textrank", "bart", "pegasus", "t5"]

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "ashdjkashldk"}


@app.get("/summarize/{method}")
async def summarize_text(method: str, text: str):
    # Handle method that is not allowed
    if method not in METHODS:
        raise HTTPException(status_code=404, detail=f"Method {method} is not allowed.")

    summary = naive.summarize(text)

    return {"method": method, "summary": summary}
