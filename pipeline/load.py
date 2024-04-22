from kfp import dsl
from google_cloud_pipeline_components.types.artifact_types import BQTable
from typing import NamedTuple

# Load data from BigQuery and save to CSV
@dsl.component()
def get_dataframe(
    project_id: str,
    bq_table: str,
    train_data: dsl.OutputPath("Dataset"),
    test_data: dsl.OutputPath("Dataset"),
    val_data: dsl.OutputPath("Dataset"),
):
    from google.cloud import bigquery
    from sklearn.model_selection import train_test_split
    import logging

    bqclient = bigquery.Client(project=project_id)
    logging.info(f"Pulling data from {bq_table}")
    table = bigquery.TableReference.from_string(bq_table)
    rows = bqclient.list_rows(table)
    dataframe = rows.to_dataframe(create_bqstorage_client=True)
    # Drop the Time column, otherwise the model will just memorize when the fraud cases happened
    # Also drop the ml_use column - we will split here. ML_use just splits in test+rest, and we need a 3-way split.
    dataframe.drop(columns=['Time', 'ML_use'], inplace=True) 
    logging.info("Data loaded, writing splits")

    # 60 / 20 / 20
    df_train, df_test = train_test_split(dataframe, test_size=0.4)
    df_test, df_val = train_test_split(df_test, test_size=0.5)

    df_train.to_csv(train_data, index=False)
    df_test.to_csv(test_data, index=False)
    df_val.to_csv(val_data, index=False)


@dsl.component()
def upload_to_bq(
    project: str,
    location: str,
    dest_dataset_id: str,
    dest_table_id: str, 
    csv_data: dsl.Input[dsl.Dataset], 
    bq_table: dsl.Output[BQTable]) -> NamedTuple('outputs', [('bq_table_uri', str)]):

    from collections import namedtuple
    import logging
    import pandas as pd
    import numpy as np
    
    from config import CLASS_NAMES

    bq_table.metadata["projectId"] = project
    bq_table.metadata["datasetId"] = dest_dataset_id
    bq_table.metadata["tableId"] = dest_table_id
    logging.info(f"BQ table: {bq_table}\nmetadata: {bq_table.metadata}")

    logging.info(f"Reading {csv_data.path}")
    dest_table = f'{dest_dataset_id}.{dest_table_id}'
    logging.info(f"Writing to {dest_table}")

    df = pd.read_csv(csv_data.path)

    # Convert Class column to int and map to CLASS_NAMES label
    df_class = df.pop('Class')
    df['Class'] = list(map(lambda f: CLASS_NAMES[f], np.rint(df_class).astype(np.int64)))

    df.to_gbq(
        destination_table=f"{dest_table}", 
        project_id=project, 
        location=location)

    t = namedtuple('outputs', ['bq_table_uri'])
    return t(f'bq://{project}.{dest_dataset_id}.{dest_table_id}')
    