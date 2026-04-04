import os
from typing import List
from dotenv import load_dotenv

from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma
from langchain_core.documents import Document

load_dotenv()


def load_text_files(folder_path: str = "docs") -> List[Document]:
    """Load all text files from the given directory"""
    print(f"Loading all text files from {folder_path}...")

    # Check if the directory exists
    if not os.path.exists(folder_path):
        raise FileNotFoundError(f"The directory {folder_path} does not exists.")

    # Load all *.txt files from the directory
    loader = DirectoryLoader(path=folder_path, glob="*.txt", loader_cls=TextLoader)
    documents = loader.load()

    if len(documents) == 0:
        print(f"No .txt file found in {folder_path}.")
        raise FileNotFoundError(f"No .txt file found in {folder_path}")

    print(f"{len(documents)} text files from {folder_path} loads successfully.")
    return documents


def split_documents(
    documents: List[Document], chunk_size: int = 800, chunk_overlap: int = 0
) -> List[Document]:
    """Split documents into similar chunks with overlap"""
    print(
        f"Splitting documents into chunks. Chunk size: {chunk_size}, Chunk overlap: {chunk_overlap}"
    )

    text_splitter = CharacterTextSplitter(
        chunk_size=chunk_size, chunk_overlap=chunk_overlap
    )

    chunks = text_splitter.split_documents(documents=documents)

    print("Documents splitted successfully..")
    return chunks


def create_vector_store(
    chunks: List[Document], persist_directory: str = "db/chroma_db"
) -> Chroma:
    """Create the embedding and store it into vector db"""
    print("Creating embedding and storing into chroma db...")

    embedding = OllamaEmbeddings(
        base_url=os.environ.get("OLLAMA_BASE_URL"),
        model="qwen3-embedding:0.6b",
    )

    vector_store = Chroma.from_documents(  # type: ignore
        documents=chunks,
        embedding=embedding,
        persist_directory=persist_directory,
        collection_metadata={"hnsw:space": "cosine"},
    )

    print(f"Vector store created and saved to {persist_directory}")
    return vector_store


def main() -> None:
    """The main method: entry point of the ingestion pipeline"""
    print("Ingestion Pipeline Started....")

    # 1. Loading the files
    documents = load_text_files(folder_path="docs")

    # 2. Chunking the files
    chunks = split_documents(documents=documents, chunk_size=500, chunk_overlap=50)

    # 3. Embedding and Storing in Vector DB
    create_vector_store(chunks=chunks)

    print("Ingestion Pipeline Completed.")


if __name__ == "__main__":
    try:
        main()
    except Exception as ex:
        print(f"Error: {ex}")
