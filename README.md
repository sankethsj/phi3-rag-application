# RAG Application with Phi3 Model and ChromaDB

Welcome to the RAG (Retrieval-Augmented Generation) application repository! This project leverages the Phi3 model and ChromaDB to read PDF documents, embed their content, store the embeddings in a database, and perform retrieval-augmented generation.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This repository contains a RAG application that reads PDF files, generates embeddings using the Alibaba-NLP/gte-large-en-v1.5 model, stores these embeddings in ChromaDB, and performs retrieval-augmented generation to provide contextual answers based on the embedded content. The system is designed to enhance the capability of answering queries by leveraging the context from the embedded documents.

## Features

- **PDF Reading**: Extracts text content from PDF documents.
- **Embedding Generation**: Utilizes the Alibaba-NLP/gte-large-en-v1.5 model to generate embeddings for the extracted text.
- **Database Storage**: Stores the generated embeddings in ChromaDB.
- **Retrieval-Augmented Generation**: Retrieves relevant embeddings from the database and generates contextually accurate responses.

## Installation

To get started with the RAG application, follow these steps:

1. **Clone the repository**:

    ```bash
    git clone https://github.com/sankethsj/phi3-rag-application.git
    cd phi3-rag-application
    ```

2. **Create a virtual environment and activate it**:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. **Install the required dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Run the notebook

1. Open RAG-Workbook.ipynb and run all cells.

## Contributing

We welcome contributions to enhance the capabilities of this RAG application. To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bugfix:

    ```bash
    git checkout -b feature-name
    ```

3. Make your changes and commit them with descriptive messages.

4. Push your changes to your fork:

    ```bash
    git push origin feature-name
    ```

5. Create a pull request to the main repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

Thank you for using the RAG application with the Phi3 model and ChromaDB. If you encounter any issues or have any questions, please feel free to open an issue on this repository.
