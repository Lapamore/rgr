# Text Summarization API

Backend service for text summarization using LLM model.

## Features

- Text summarization using Llama model
- RESTful API endpoints
- Configurable summarization parameters
- Input validation and error handling

## Setup

1. Install Poetry (if not already installed):
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

2. Install dependencies:
```bash
poetry install
```

3. Make sure you have Ollama installed and the Llama model downloaded:
```bash
ollama pull llama3.1
```

4. Activate the virtual environment:
```bash
poetry shell
```

5. Run the application:
```bash
poetry run uvicorn main:app --reload
```

## API Endpoints

### POST /api/v1/summary

Summarize text content.

Request body:
```json
{
    "text": "Your text to summarize",
    "max_length": 500,  // optional
    "min_length": 100   // optional
}
```

## Development

- Run tests: `poetry run pytest`
- Format code: `poetry run black .`
- Sort imports: `poetry run isort .`
- Type checking: `poetry run mypy src`
- Lint code: `poetry run flake8`
- API documentation: http://localhost:8000/docs
