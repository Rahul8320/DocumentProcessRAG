import os
from dotenv import load_dotenv
from typing import List

from openai import OpenAI

from core.llm_message import LLMMessage

load_dotenv(override=True)


class LLM:
    def __init__(self) -> None:
        self._client = OpenAI(
            base_url=os.getenv("OPENAI_BASE_URL"),
            api_key=os.getenv("OPENAI_API_KEY"),
        )

    def get_embedding(
        self, text: str, model: str = "text-embedding-qwen3-embedding-0.6b"
    ) -> List[float]:
        response = self._client.embeddings.create(input=[text], model=model)
        return response.data[0].embedding

    def get_chat(
        self, messages: List[LLMMessage], model: str = "qwen/qwen3-4b-thinking-2507"
    ) -> str | None:
        response = self._client.chat.completions.create(messages=messages, model=model)  # type: ignore
        return response.choices[0].message.content
