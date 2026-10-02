import os
from typing import Type, TypeVar

from dotenv import load_dotenv
from google import genai
from pydantic import BaseModel


load_dotenv()

T = TypeVar("T", bound=BaseModel)


class GeminiProvider:

    def __init__(self, api_key: str | None = None):

        api_key = api_key or os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY is not configured."
            )

        self.client = genai.Client(api_key=api_key)

    def generate_structured(
        self,
        prompt: str,
        response_schema: type[T],
        model: str = "gemini-2.5-flash",
    ) -> T:

        response = self.client.models.generate_content(
            model=model,
            contents=prompt,
            config={
                "response_mime_type": "application/json",
                "response_schema": response_schema,
            },
        )

        return response_schema.model_validate_json(
            response.text
        )