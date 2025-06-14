import os
import openai
from typing import Optional
from openai import OpenAI

class OpenAIClient:
    """
    A simple wrapper class for interacting with OpenAI's API.
    """


    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize OpenAI client with the provided API key.
        
        Args:
            api_key (str, optional): Your OpenAI API key. 
            If not provided, it will look for the environment variable 'OPENAI_API
        """

        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        if not self.api_key:
            raise ValueError("API key must be provided either as an argument or through the 'OPENAI_API_KEY' environment variable.")
        openai.api_key = self.api_key


    def get_completion(self, prompt: str, model: str = "gpt-4o-mini", max_tokens: int = 500) -> str:
        """
        Send prompt to OpenAI API and return the generated completion text.

        Args:
            prompt (str): The text prompt to send to the model.
            model (str): Model name to use.
            max_tokens (int): Max tokens for the response.

        Returns:
            str: Generated text completion from the model.
        """
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=0.7,
        )
        return response.choices[0].message.content.strip()