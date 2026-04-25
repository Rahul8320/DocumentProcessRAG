from core.llm import LLM
from core.llm_message import LLMMessage


llm = LLM()

vector = llm.get_embedding(text="Once upon a time, there was a cat.")
print(vector[:5])

message = llm.get_chat(
    messages=[
        LLMMessage(
            role="system",
            content="You are a very intelligent and mindful assistance. Read the user query very carefully, think deeply, give short, precise and intelligent answer.",
        ),
        LLMMessage(
            role="user",
            content="How many character 'a' is appeared in this sentence?",
        ),
    ],
)
print(message)
