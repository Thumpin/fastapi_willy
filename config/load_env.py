from dotenv import load_dotenv
import os

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
HOST = os.getenv("HOST")
HOST_PORT = os.getenv("HOST_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_TYPE = os.getenv("DB_TYPE")