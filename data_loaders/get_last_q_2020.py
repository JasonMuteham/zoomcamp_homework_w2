import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    kwarg_logger = kwargs.get('logger')

    taxi_dtypes = {


        'trip_distance': float,

        'store_and_fwd_flag': str,
        'fare_amount': float,
        'extra': float,
        'mta_tax': float,
        'tip_amount': float,
        'tolls_amount': float,
        'improvement_surcharge': float,
        'total_amount': float,
        'congestion_surcharge': float 
        }

    parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']
    df_out = pd.DataFrame()
   
    for month in range(10,13):
        url = f'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-{month}.csv.gz'
        df = pd.read_csv(url, sep=',', compression = 'gzip', dtype=taxi_dtypes, parse_dates=parse_dates)
        kwarg_logger.info(f'green_tripdata_2020-{month}.csv.gz - shape{df.shape}')
        df_out = pd.concat([df_out, df], ignore_index=True)

    kwarg_logger.info(f'green_tripdata - shape{df_out.shape}')

    return df_out


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """

    assert output is not None, 'The output is undefined'
