# Movie Recommendation API

This project is a **FastAPI** based backend for recommending movies using **Qdrant** as the vector search engine. Currently, the system handles **5000 movies** and provides personalized recommendations. Further enhancements are planned to make the project end-to-end, including improvements to scalability, feature integration, and more.

## Project Status

🚧 **In progress**:  
This project is actively being developed, with more features and functionalities planned for future releases.

## Tech Stack

- **Backend Framework**: FastAPI
- **Vector Search Engine**: Qdrant (latest client version)
- **Database**: Custom movie database (5000 movies)
- **Language**: Python

## Features

- **Movie Recommendation**: The current system provides personalized recommendations based on user preferences, leveraging vector search through Qdrant.
- **Scalability**: Supports fast and efficient retrieval of movie recommendations from a dataset of 5000 movies.

## Setup and Installation

### Prerequisites

- Python 3.9+
- Docker (optional, for containerized deployment)
- Qdrant (can be run locally using Docker or as a managed service)

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/vancityrahul/Movie-Recommender.git

2. **Install Dependencies**:
    
    It's recommended to create a virtual environment first:
   ```bash
    python3 -m venv env
    source env/bin/activate
   ```
    Install the required packages:
   ```bash
    pip install -r requirements.txt
    ```
3. **Run the API**:

   ```bash
   uvicorn backend.server.models_server:app