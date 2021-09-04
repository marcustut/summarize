from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

from summarize.scraper import parser
from model.summarize import SummarizeTypes, SummarizeMethods
from internal.logic import SummarizeMethodNotSupported, handleSummarize

app = FastAPI()

origins = ["http://localhost:3333"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/summarize/{type}/{method}")
async def summarize(
    type: str,
    method: str,
    url: Optional[str] = None,
    text: Optional[str] = None,
    tag: Optional[str] = "p",
):
    # Handle type that is not allowed
    try:
        summarizeType = SummarizeTypes(type)
    except ValueError:
        raise HTTPException(status_code=404, detail=f"Type {type} is not allowed.")

    # Handle method that is not allowed
    try:
        summarizeMethod = SummarizeMethods(method)
    except ValueError:
        raise HTTPException(status_code=404, detail=f"Method {method} is not allowed.")

    # Handle summarizing
    if summarizeType == SummarizeTypes.Text:
        if text == None:
            raise HTTPException(status_code=404, detail="'text' cannot be empty.")

        try:
            summary = handleSummarize(summarizeMethod, text)
            return {"summary": summary, "length": len(summary.split(" "))}
        except SummarizeMethodNotSupported as err:
            raise HTTPException(status_code=404, detail=err)
    elif summarizeType == SummarizeTypes.Url:
        if url == None:
            raise HTTPException(status_code=404, detail="'url' cannot be empty")

        content = parser.parse_html_to_paragraphs(url, [tag])

        try:
            summary = handleSummarize(summarizeMethod, content)
            return {"summary": summary, "length": len(summary.split(" "))}
        except SummarizeMethodNotSupported as err:
            raise HTTPException(status_code=404, detail=err)
    else:
        raise HTTPException(
            status_code=404, detail=f"Type {type} is currently not supported."
        )
