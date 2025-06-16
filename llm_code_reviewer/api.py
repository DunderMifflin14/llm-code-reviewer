from fastapi import FastAPI, HTTPException  # FastAPI framework and error handling
from pydantic import BaseModel  # For data validation and request body parsing
from llm_code_reviewer.openai_client import OpenAIClient  # Your custom OpenAI wrapper

# Initialize the FastAPI app
app = FastAPI()

# Create an instance of the OpenAI client
client = OpenAIClient()





# Define the expected structure of the incoming request using Pydantic
class CodeReviewRequest(BaseModel):
    code: str          # The code snippet to review
    language: str      # Programming language of the code (e.g., "python", "sql")





# Define a POST endpoint at "/review-code/"
@app.post("/review-code/")
async def review_code(request: CodeReviewRequest):
    """
    Endpoint to review code using OpenAI's API.

    Args:
        request (CodeReviewRequest): The code and language to review.
        
    Returns:
        dict: The review results from the OpenAI API.
    """

    # Build a prompt to send to the OpenAI model
    prompt = (
        f"Review the following {request.language} code:\n\n"
        f"{request.code}\n\n"
        "Provide feedback on best practices, potential issues, and improvements."
    )

    try:
        # Send the prompt to OpenAI and get the response
        response = client.get_completion(prompt)
        # Return the AI-generated review as a JSON response
        return {"review": response}
    except Exception as e:
        # Handle any errors (e.g., API failure) by returning a 500 HTTP error
        raise HTTPException(status_code=500, detail=str(e))
