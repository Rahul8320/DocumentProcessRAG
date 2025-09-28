# Document Processing RAG Application

Process multiple documents like pdf, image or urls and chat with this documents by using LLM.

## Requirements

 - [Python](https://www.python.org)
 - [uv](https://docs.astral.sh/uv)

## Local Development Setup

1. Clone this git repo and change directory to this folder

    ```bash
    git clone https://github.com/Rahul8320/DocumentProcessRAG.git
    cd DocumentProcessRAG
    ```

2. Install python packages

    ```bash
    uv sync 
    ```

3. Add env variables

    ```bash
    cp .env.sample .env
    ```

Update this environment variables

4. Activating the virtual environment 

    ```bash
    .\venv\Scripts\Activate  (for Windows)
    source .venv/bin/activate (for Linux and Mac)
    ```

5. Running the application

    ```bash
    streamlit run main.py
    ```

## Tools and Technologies Used

 - [Python](https://www.python.org)
 - [uv](https://docs.astral.sh/uv)
 - [Streamlit](https://streamlit.io)
 - [LangChain](https://python.langchain.com/docs/introduction)


## Related Blogs and Videos

 - [Build a Retrieval Augmented Generation (RAG) App](https://python.langchain.com/docs/tutorials/rag/)
 - [Chat With Multiple PDF Documents With LangChain And Google Gemini Pro](https://www.youtube.com/watch?v=uus5eLz6smA&list=PLZoTAELRMXVORE4VF7WQ_fAl0L1Gljtar&index=14)