from os import path, getenv
from dotenv import load_dotenv

dirname = path.dirname(__file__)

try:
    load_dotenv(dotenv_path=path.join(dirname, '..', '.env'))
except FileNotFoundError:
    pass

DATABASE_FILENAME = getenv('DATABASE_FILENAME') or 'database.sqlite'
DATABASE_FILE_PATH = path.join(dirname, '..', 'data', DATABASE_FILENAME)
