# S3 API Project

## Overview

This FastAPI application provides a RESTful API for simulating viability de investimento de um projeto pelo governo e como
isso afeta oo Indice de felicidade , IDH, nos direitos humanos,  IPCA, Cade,  PIB, na taxa cambial e no dolar, defict primario , taxa de importacao e expotacao  e   Politica protecao aos animais e meio ambiente.


## Features

- 
- Download files from S3.
- Move files within the S3 bucket.
- List files in the S3 bucket.
- Retrieve a secret from AWS Secrets Manager.

## Requirements

- Python 3.11
- FastAPI
- Uvicorn (for running the server)
- Boto3 (for AWS services)
- Pytest (for testing)

## Setup

1. Clone the repository.
2. Install dependencies:

3. Set up your AWS credentials and `.env` file with necessary configurations.

## Running the Application

1. Start the FastAPI server:

2. The API will be available at `http://localhost:8000`.

## Acesing Swagger
2. The API doc will be available at `http://localhost:8000/docs`.

## Running Tests

Run tests using pytest:

## Project tree
s3-api/
├── app/
│   ├── __init__.py
│   ├── config/
│   ├── dto/
│   │   ├── __init__.py
│   │   ├── req/
│   │   └── res/
│   └── main.py
├── tests/
│   ├── __init__.py
│   ├── test_main.py
│   ├── test_s3.py
│   └── test_secret.py
├── Dockerfile
├── api.http
├── requirements.txt
└── venv/
