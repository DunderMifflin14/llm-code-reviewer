# llm-code-reviewer

LLM-powered API to review Python and SQL code snippets.  
Paste your code and get instant feedback with improvement suggestions and a refactored version.  

Built with FastAPI and OpenAI's GPT models, this project demonstrates practical use of LLMs for code quality enhancement.  

## Features
- Supports Python and SQL code reviews  
- Returns detailed feedback and cleaner code samples  
- Easily extendable for other languages or integrations  

## Getting Started

### 1. Activate the virtual environment
```
source /Users/andy/Library/Caches/pypoetry/virtualenvs/llm-code-reviewer-JR0WfYy6-py3.13/bin/activate
```

### 2. Install dependencies (if not already installed)
```
poetry install
```

### 3. Set your OpenAI API key
```
export OPENAI_API_KEY=your_openai_api_key_here
```

### 4. Start the FastAPI server
```
uvicorn llm_code_reviewer.main:app --reload
```

### 5. Test the API
Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to use the interactive API documentation and test the `/review-code/` endpoint.
