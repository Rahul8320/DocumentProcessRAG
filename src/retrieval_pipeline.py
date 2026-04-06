import os
from dotenv import load_dotenv

from langchain.messages import HumanMessage, SystemMessage
from langchain_chroma import Chroma
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_core.language_models.base import LanguageModelInput


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

context: str = ""

for i, doc in enumerate(relevant_docs, 1):
    context += f"Document {i}:\n{doc.page_content}\n"

model = OllamaLLM(base_url=os.environ.get("OLLAMA_BASE_URL"), model="gemma3:1b")

messages: LanguageModelInput = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(
        content=f"""Based on the following documents, please answer this question: 
                    Query: '{query}'. 
                    Documents: '{context}'
                    Please provided a clear, helpful answer using only the information from these documents. If you can't find the answer in the documents, say 'I don't have enough information to answer this question.' """
    ),
]

result = model.invoke(messages)

print(f"Response: {result}")
