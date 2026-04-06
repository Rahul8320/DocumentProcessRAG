import os
from dotenv import load_dotenv

from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings

load_dotenv()

persistent_directory = "db/chroma_db"

# Loading embedding model
embedding = OllamaEmbeddings(
    base_url=os.environ.get("OLLAMA_BASE_URL"),
    model="qwen3-embedding:0.6b",
)

# Loading vector database
db = Chroma(
    persist_directory=persistent_directory,
    embedding_function=embedding,
    collection_metadata={"hnsw:space": "cosine"},
)

# Search for relevant documents
# query = "Which island does SpaceX lease for its launches in the Pacific?"
query = "What was NVIDIA's first graphics accelerator called?"

retriever = db.as_retriever(search_kwargs={"k": 3})

relevant_docs = retriever.invoke(query)

print(f"User Query: {query}")
print(f"{'-' * 10}-Context-{'-' * 10}")
for i, doc in enumerate(relevant_docs, 1):
    print(f"Document {i}:\n{doc.page_content}\n")
