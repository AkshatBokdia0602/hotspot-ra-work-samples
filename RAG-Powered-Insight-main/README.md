# RAG-Powered-Insight 📰

Rag Powered Insight is a project that leverages the power of Retrieval-Augmented Generation (RAG) and large language models (LLMs) to provide insightful answers to user queries based on a topic chosen by the user. The project fetches the latest news articles on a given topic and uses this data to answer user queries.

## Table of Contents 📚
- Features
- Installation
- Contributing
- License

## Features 👨🏻‍💻

- **Topic-based News Retrieval**: Users can input a topic, and the project uses GNews to retrieve the latest news articles related to that topic.
- **RAG-based Query Answering**: Users can ask questions based on the aggregated news content, and the project uses a RAG-based model to provide accurate and insightful answers.

## Installation 📲

1. Clone the repository.
2. Navigate to the project directory.
3. Install the required dependencies.
4. Obtain a Developer API key from https://aistudio.google.com/app/u/1/apikey.
5. (Optional) Set up a virtual environment.

```bash
   python -m venv venv
   source venv/bin/activate
   ```
6. Start the application.
   
```bash
   jupyter notebook RAG-Powered Insight.ipynb
   ```

## Contributing 💡

Contributions are welcome! If you have any ideas for improvements, bug fixes, or new features, please open an issue or submit a pull request.

## License ⚖️

This project is licensed under the [MIT License](LICENSE).
