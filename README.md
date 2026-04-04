# Document Processing RAG Application

Process multiple documents like pdf, image or text file and chat with this documents by using LLM.

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
    .\venv\Scripts\Activate       (for Windows)
    source .venv/bin/activate     (for Linux and Mac)
    ```

5. Running the application

    ```bash
    streamlit run .\src\main.py    (for Windows)
    streamlit run ./src/main.py    (for Linux and Mac)
    ```

## Prepare sample text file

Run the `prepare_data` script to generate txt file from wikipedia

    ```bash
    uv run .\Script\prepare_data.py
    ```

## Tools and Technologies Used

 - [Python](https://www.python.org)
 - [uv](https://docs.astral.sh/uv)
 - [LangChain](https://python.langchain.com/docs/introduction)


## Related Blogs and Videos

 - [Youtube Playlist](https://www.youtube.com/watch?v=63B-3rqRFbQ&list=PLNIQLFWpQMRUMjxfe8o6g3uzJ6LH_VotY)