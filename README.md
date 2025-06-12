# Keep

This repository contains a FastAPI project designed for deployment on Google
Cloud Run, a serverless compute platform that allows you to run stateless
containers.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Local Development](#local-development)
- [Deployment to Google Cloud Run](#deployment-to-google-cloud-run)

## Prerequisites

Before you begin, ensure you have the following installed/configured:

- **Python 3.11+**
- **Docker**: To build and run the project locally
- **Google Cloud SDK (gcloud CLI)**: For interacting with Google Cloud.
    - [Installation Guide](https://cloud.google.com/sdk/docs/install)


## Local Development

Follow these steps to run the FastAPI application locally:

1.  **Clone the repository:**

    ```bash
    git clone [https://github.com/omartrinidad/keep.git](https://github.com/omartrinidad/keep.git)
    cd keep
    ```

2.  **Create a virtual env**

    ```bash
    python -m venv venv
    source venv/bin/activate
    ```

3.  **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Run the FastAPI application:**

    ```bash
    uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
    ```

    Your API will be accessible at `http://localhost:8000`

## Deployment to Google Cloud Run

This section outlines the steps to deploy `Keep` to Google Cloud Run:

1. Go to Cloud Run
2. Select the option: Continuosly deploy from a repository.
    2.1. Select the repository
3. Configure `Service name` and `Region`.
