# Data Science and Machine Learning Vault

The required *Python* version for this project is *3.12.x.*

## About me

Hello, my name is *Oscar*, I am 26 years old, and I am from Bogotá, Colombia. My experience in the world of software development is what I acquired during my time at university. This degree has been quite challenging for me because I also work at Airbnb in customer service, which is why I speak Portuguese and have an intermediate level of English. The reason I chose this career is because I love automating processes and really enjoy analyzing data on a small scale. I'm not the best at math, but I believe that with practice and study, anything is possible.

## Project Description

**MiCasaBot** is a sophisticated chatbot designed to provide answers to questions related to home acquisition in Colombia. It helps users understand various concepts, clarifies rights and procedures, and guides them through the process of acquiring a home using a curated knowledge base.

## How It Is Built?

**MiCasaBot** utilizes several advanced technologies:

* **LangChain + Chroma**: Integrates the language model (LLM) with the Chroma vector database for efficient semantic search.
* **Embeddings (Hugging Face `sentence-transformers/all-MiniLM-L6-v2`)**: Converts text into vector representations for similarity search.
* **Gemini-2.5-Flash Model**: Provides the processing power for natural language understanding and response generation.
* **Directive-based prompt pattern**: Guides the language model to generate appropriate responses based on query context and user interaction directives.

## Architecture Overview
![alt text](./documentation/images/capstone/architecture.png)

## Setup environment

As usual setup your virtual environment:

```
$ python -m venv venv
$ source venv/bin/activate
$ pip install --upgrade pip setuptools
$ pip install -r requirements-dev.txt
$ pip install -e .
```

## Basic code compliance

```
$ black .
All done! ✨ 🍰 ✨
X files left unchanged.
$ mypy .
Success: no issues found in X source files
```

## About the CI/CD pipeline

This `monorepo` comes with a pre-configured CI/CD pipeline that is triggered every time a push is made to a **merge request** or when a **merge request** is integrated into the **main** branch.

The pipeline is configured to:

- Execute **code compliance** checks.
- Generate documentation.

> You may add more stages or jobs to the pipeline, but make sure you **do not remove the existing ones**. In addition, make sure you do your best to **keep the pipeline green** at all times.

## Running the Backend

### 1. **Configure Environment Variables**

Create a `.env` file in the root of your project with the following necessary variables:

```js
GOOGLE_API_KEY = "YOUR_GOOGLE_API_KEY"
GEMINI_MODEL = "gemini-2.5-flash"
EMBEDDING_MODEL = "all-MiniLM-L6-v2"
COLLECTION_NAME = "documents"
CHROME_HOST = "localhost"
```

**Explanation of variables:**

- **`GOOGLE_API_KEY`**: Your Google API key used for integrating Google services.
- **`GEMINI_MODEL`**: Specifies the model used for Gemini (e.g., `"gemini-2.5-flash"`).
- **`EMBEDDING_MODEL`**: Defines the model used for embeddings, typically used for NLP tasks (e.g., `"all-MiniLM-L6-v2"`).
- **`COLLECTION_NAME`**: The name of the VectorDatabase collection where vectors will be stored.
- **`CHROMA_HOST`**: Specifies the host address for Chroma.

The variables specified in the `.env` file will be used by default. If any variable is missing, the application will use the default values specified in the `settings` configuration.

### 2. Run service

This project uses Docker Compose to run the backend service along with a **Chroma** container for vector storage. Make sure you have **Docker** and **Docker Compose** installed.

To start the backend, run:

```bash
# Using the modern docker compose
$ docker compose up -d --build

# Or with
$ docker-compose up -d --build
```

This command will:

* Build the backend Docker image (if not built already).
* Start the backend service.
* Start the Chroma container for vector storage.

## **Endpoints**

#### **Base URL:**

`http://localhost:8001`

#### 1. **Add a new document to the database**

- **Method:** `POST`
- **Endpoint:** `/api/documents/add`
- **Description:** Adds a new document to the database.
- **Request Body:**

  ```json
  //form-data
  {
    "files": "Decreto 431 de 2024.pdf"
  }
  ```

- **Example Usage:**

  ![Add Document Example](./documentation/images/capstone/example_add_document_request.png)

#### 2. **Search for answers in the document database**

- **Method:** `POST`
- **Endpoint:** `/api/documents/search`
- **Description:** Search for answers within the document database.
- **Request Body:**

  ```json
  {
    "question": "Un colombiano tiene derecho a tener una vivienda?"
  }
  ```

- **Example Usage:**

  ![Search Example](./documentation/images/capstone/example_search_request.png)

*You can go to the `documentation/postman-collection` to find the endpoint requests and the body of the requests.*
