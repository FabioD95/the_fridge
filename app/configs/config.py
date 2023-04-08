import os


# Database settings
DB_CONFIG = {
    "db_name": os.getenv("DB_NAME", "test1"),
    "db_user": os.getenv("DB_USER", "postgres"),
    "db_password": os.getenv("DB_PASSWORD", "psw"),
    "db_port": os.getenv("DB_PORT", "5432"),
    "db_host": os.getenv("DB_HOST", "localhost"),
}