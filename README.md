# Project Title 🚀

## Overview 💡
This project was developed using **FastAPI**, **Peewee**, and follows the **PEP8** style guide, with **Pylint** and **Black** to ensure code quality and formatting. The project also utilizes **Docker** 🐳 for creating a **MySQL** database environment. Additionally, **Uvicorn** is used as the ASGI server to run the FastAPI application, and **Swagger** is integrated for API documentation and testing.

## Features ✨
- 🐍 **FastAPI**: A modern web framework for building APIs quickly with Python.
- 🐦 **Peewee**: A lightweight ORM for handling database operations.
- 🛠️ **Pylint & Black**: Used to ensure code adheres to PEP8 standards, with Pylint for linting and Black for automatic formatting.
- 🐳 **Docker**: Containerized environment for the MySQL database and other services.
- 📜 **Swagger**: Automatically generated API documentation available at `/docs`.
- ✅ **Pylint Job**: A job created to automatically verify that the code meets the PEP8 standards using Pylint.

## Project Structure 🏗️
- 📂 **Routes**: Defined for handling API endpoints.
- 🧩 **Services**: Business logic is organized in service layers for clean architecture.

## Prerequisites 📋
Ensure the following are installed on your system:
- 🐍 Python 3.x
- 🐳 Docker & Docker Compose
- 🛠️ Pylint & Black (for development)

## Setup Instructions ⚙️

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/yourproject.git
    cd yourproject
    ```

2. **Set up virtual environment**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run Black for code formatting**:
    Ensure the code follows PEP8 style guide using Black:
    ```bash
    black your_project/
    ```

5. **Run Pylint to verify code quality**:
    Use Pylint to check that the code meets PEP8 and other standards:
    ```bash
    pylint your_project/
    ```

6. **Build and start Docker services**:
    Build the Docker image and start the MySQL container:
    ```bash
    docker-compose up -d
    ```

7. **Run the FastAPI app with Uvicorn**:
    After Docker services are running, start the FastAPI app:
    ```bash
    uvicorn main:app --reload
    ```

8. **Access the API documentation**:
    Open your browser and go to `http://localhost:8000/docs` to view and interact with the API documentation powered by Swagger.

## Testing the API 🧪
- Use Swagger UI at `/docs` to test the endpoints directly from your browser.
- Alternatively, you can use tools like **Postman** or **cURL** to interact with the API.

## Database 🗄️
- The database used is **MySQL**, set up using Docker Compose. The connection details are managed through environment variables defined in the `.env` file.

## Pylint Job ✅
A job is set up to automatically run Pylint, ensuring that the code adheres to PEP8 and other best practices each time code is pushed.

## Contribution 🤝
Feel free to contribute by forking the repository, making your changes, and submitting a pull request.

## License 📄
This project is licensed under the MIT License.
