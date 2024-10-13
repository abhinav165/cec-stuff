from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError

URL_DATABASE = 'postgresql://postgres:1234@localhost:5432/CECProject'

try:
    engine = create_engine(URL_DATABASE)
    connection = engine.connect()
    print("Connection successful!")
except SQLAlchemyError as e:
    print(f"Error connecting to the database: {e}")
