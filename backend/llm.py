from google import genai
from google.genai import types
from google.genai.errors import ClientError
from .config import GEMINI_API_KEY, MODEL_NAME, TEMPERATURE


class LLM:

    def __init__(self):
        self.client = genai.Client(
            api_key=GEMINI_API_KEY
        )

    def invoke(self, prompt):

        try:

            response = self.client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt
        )

            return response.text

        except ClientError:

            return "Gemini API quota exceeded."

        except Exception as e:

            return f"Gemini Error: {e}"