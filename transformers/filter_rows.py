from mage_ai.data_cleaner.transformer_actions.base import BaseAction
from mage_ai.data_cleaner.transformer_actions.constants import ActionType, Axis
from mage_ai.data_cleaner.transformer_actions.utils import build_transformer_action
from pandas import DataFrame

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def execute_transformer_action(df: DataFrame, *args, **kwargs) -> DataFrame:
    """
    Execute Transformer Action: ActionType.FILTER

    Docs: https://docs.mage.ai/guides/transformer-blocks#filter
    """
    df['lpep_pickup_date'] = df['lpep_pickup_datetime'].dt.date
    df = df.rename(columns={"VendorID": "vendor_id", 
                            "RatecodeID": "ratecode_id",
                            "PULocationID": "pu_location_id",
                            "DOLocationID": "do_location_id"
                            })
    action = build_transformer_action(
        df,
        action_type=ActionType.FILTER,
        axis=Axis.ROW,
        action_code='passenger_count > 0 and trip_distance > 0'
    )


    return BaseAction(action).execute(df)


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'

@test
def test_output2(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output['passenger_count'].isin([0]).sum()==0 , 'Passenger count is zero'
    assert output['trip_distance'].isin([0]).sum()==0 , 'Trip distance is zero'
    assert output['vendor_id'].isin([1,2]).count() == output['vendor_id'].count() , 'vendor id error'