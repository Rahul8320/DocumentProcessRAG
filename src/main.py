from langchain_ollama import OllamaEmbeddings


embedding = OllamaEmbeddings(
    model="qwen3-embedding:0.6b", base_url="http://localhost:11434"
)

vector = embedding.embed_query("Once upon a time, there was a cat.")
print(vector[:5])
