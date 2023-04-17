import os


# Set the application variables
API_ENDPOINT_PORT: int = int(os.environ.get("API_ENDPOINT_PORT", 8000))
API_ENDPOINT_HOST: str = os.environ.get("API_ENDPOINT_HOST", "127.0.0.1")
PROJECT_NAME: str = "The Fridge"
API_V1_STR: str = os.environ.get("API_V1_STR", "/api/v1")


# Database settings
DB_CONFIG = {
    "db_name": os.getenv("DB_NAME", "test1"),
    "db_user": os.getenv("DB_USER", "postgres"),
    "db_password": os.getenv("DB_PASSWORD", "psw"),
    "db_port": os.getenv("DB_PORT", "5432"),
    "db_host": os.getenv("DB_HOST", "localhost"),
}