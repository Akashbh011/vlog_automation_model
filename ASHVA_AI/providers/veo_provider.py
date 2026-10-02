import os
import time

from dotenv import load_dotenv
from google import genai


load_dotenv()


class VeoProvider:

    def __init__(self, api_key: str | None = None):

        api_key = api_key or os.getenv("GEMINI_API_KEY")

        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY is not configured."
            )

        self.client = genai.Client(api_key=api_key)

    def generate_video(
        self,
        prompt: str,
        model: str = "veo-3.1-generate-preview",
        aspect_ratio: str = "9:16",
    ):

        operation = self.client.models.generate_videos(
            model=model,
            prompt=prompt,
            config={
                "aspect_ratio": aspect_ratio
            },
        )

        while not operation.done:

            time.sleep(10)

            operation = self.client.operations.get(
                operation
            )

        return operation