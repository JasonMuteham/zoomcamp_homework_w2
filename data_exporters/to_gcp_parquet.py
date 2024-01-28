from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from pandas import DataFrame
import os
import pyarrow as pa
import pyarrow.parquet as pq

if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "zoompcamp_homework_w2/terraform/keys/terraform-demo-411110-8ef6da51b509.json"
bucket_name = 'homework-w2-411110-bucket'
project_id = 'terraform-demo-411110'
table_name = 'green_taxi.data'

root_path = f"{bucket_name}/{table_name}"

@data_exporter
def export_data_to_google_cloud_storage(data, *args, **kwargs):


    table = pa.Table.from_pandas(data)
    gcs = pa.fs.GcsFileSystem()
    pq.write_to_dataset(
        table,
        root_path=root_path,
        partition_cols=['lpep_pickup_date'],
        filesystem=gcs
    )
    