import os
from dotenv import load_dotenv
from sqlalchemy import create_engine

# Load environment variables
load_dotenv()

username_pg = os.environ.get("DB_USER")
password_pg = os.environ.get("DB_PW")
port_pg = os.environ.get("DB_PORT")
db_name_pg = os.environ.get("DB_NAME")
db_host_pg = os.environ.get("DB_HOST")

SQLALCHEMY_DATABASE_URL_PG = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(username_pg, password_pg, db_host_pg, port_pg, db_name_pg)

def connect():
    try:
        engine_pg = create_engine(SQLALCHEMY_DATABASE_URL_PG, echo=False, pool_size=20, max_overflow=10)
        conn = engine_pg.connect()
        return conn
    except Exception as e:
        print(e)
        print("Error connecting to the database")
        exit(1)