from dotenv import load_dotenv
import os
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

USERNAME = os.getenv("db_user_name")
DATABASE_PASSWORD = os.getenv("db_password")
CONNECTION = os.getenv('connection')
DATABASE = os.getenv('database')
AWS_ACCESS_KEY_ID = os.getenv('aws_access_key_id')
AWS_SECRET_KEY = os.getenv('aws_secret_access_key')