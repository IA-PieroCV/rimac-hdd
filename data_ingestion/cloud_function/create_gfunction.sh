#!/bin/bash

gcloud functions deploy trigger_csv2bq \
    --runtime python312 \
    --trigger-resource rimac-hdd-rawdata \
    --trigger-event google.storage.object.finalize \
    --entry-point trigger_csv2bq.py \
    --gen2 \
    --region us-east1