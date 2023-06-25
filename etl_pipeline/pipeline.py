import boto3
import os
import pandas as pd
from datetime import datetime, timezone
from dbconn import connect

def etl_manager():
    conn = connect()
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