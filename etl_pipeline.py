import boto3
import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime, timezone

# Load environment variables
load_dotenv()

username_pg = os.environ.get("DB_USER")
password_pg = os.environ.get("DB_PW")
port_pg = os.environ.get("DB_PORT")
db_name_pg = os.environ.get("DB_NAME")
db_host_pg = os.environ.get("DB_HOST")

SQLALCHEMY_DATABASE_URL_PG = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(username_pg, password_pg, db_host_pg, port_pg, db_name_pg)

engine_pg = create_engine(SQLALCHEMY_DATABASE_URL_PG, echo=False, pool_size=20, max_overflow=10)

conn = engine_pg.connect()

# Create a client for the AWS API to access S3 bucket
s3 = boto3.client(service_name='s3', aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
                  aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY'], region_name=os.environ['AWS_REGION'])

# List all the folders in the bucket
response = s3.list_objects_v2(Bucket=os.environ['AWS_BUCKET_NAME'])

# Print the folders
for content in response['Contents']:
    if content['Key'].endswith('csv'):
        if (datetime.now(timezone.utc) - content['LastModified']).total_seconds() < 300:
            print(content['Key'])
            filename = os.path.join(os.getcwd(), os.path.basename(content['Key']))
            s3.download_file(os.environ['AWS_BUCKET_NAME'], content['Key'], filename)

            # Read the csv file
            df = pd.read_csv(filename)
            # Upload the data to db
            df.to_sql('human_activity_sensor', con=conn, if_exists='append', index=False)

            os.remove(filename)

conn.close()