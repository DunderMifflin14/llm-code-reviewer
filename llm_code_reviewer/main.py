from fastapi import FastAPI
from llm_code_reviewer.api import review_code_endpoint, review_code
from llm_code_reviewer.openai_client import CodeReviewRequest  

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello, LLM Code Reviewer!"}

@app.post("/review-code/")
async def review_code_endpoint(request: CodeReviewRequest):
    return await review_code(request)
