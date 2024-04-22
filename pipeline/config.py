import os

PROJECT_ID = os.getenv("PROJECT_ID", "analytics-project-373621")
REGION = os.getenv("REGION", "us-east1")
IMAGE=os.getenv("CICD_IMAGE_URI", f'{REGION}-docker.pkg.dev/{PROJECT_ID}/rimac-hdd-kfp/base:latest')
TRAIN_COMPONENT_IMAGE=f'{REGION}-docker.pkg.dev/{PROJECT_ID}/rimac-hdd-kfp/train-fraud:latest'
IMAGE_MODEL_CARD=os.getenv("CICD_IMAGE_MODEL_CARD", f'{REGION}-docker.pkg.dev/{PROJECT_ID}/rimac-hdd-kfp/model-card:latest')

CLASS_NAMES = ['Heart Desease', 'Not HD']
TARGET_COLUMN = 'HeartDisease'

PIPELINE_NAME = os.getenv("PIPELINE_NAME", 'cb-rimac-hdd')
PIPELINE_ROOT = os.getenv("PIPELINES_STORE", f'gs://{PROJECT_ID}/pipeline_root/{PIPELINE_NAME}')
SERVICE_ACCOUNT = os.getenv("SERVICE_ACCOUNT", "pipeline-runner@analytics-project-373621.iam.gserviceaccount.com")
NETWORK = os.getenv("NETWORK")
KEY_ID = os.getenv("CMEK_KEY_ID") # e.g. projects/my-project/locations/my-region/keyRings/my-kr/cryptoKeys/my-key

BQ_INPUT_DATA=f"{PROJECT_ID}.{os.getenv('BQ_DATASET_NAME', 'rimac_hdd')}.{os.getenv('ML_TABLE', 'rimac_hdd_input')}"
PARENT_MODEL='' # f'projects/{PROJECT_ID}/locations/{REGION}/models/YOUR_NUMERIC_MODEL_ID_HERE'

BQ_OUTPUT_DATASET_ID="rimac_hdd_output"

MODEL_DISPLAY_NAME = os.getenv("MODEL_DISPLAY_NAME", 'rimac-hdd-kfp')
MODEL_CARD_CONFIG='../model_card_config.json'

PRED_CONTAINER='us-docker.pkg.dev/vertex-ai/training/sklearn-cpu.1-0:latest'
ENDPOINT_NAME=PIPELINE_NAME

EMAILS=['piero.casusolv@pucp.edu.pe']

# Evaluation pipeline
DATAFLOW_SA = os.getenv("DATAFLOW_SA", "pipeline-runner@analytics-project-373621.iam.gserviceaccount.com")
DATAFLOW_NETWORK = os.getenv("DATAFLOW_NETWORK")
DATAFLOW_PUBLIC_IPS = False
