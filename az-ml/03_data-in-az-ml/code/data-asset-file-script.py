
import argparse
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("--data-asset", type=str)
parser.add_argument("--version", type="str")
args = parser.parse_args()

ml_client = MLClient.from_config(credential=DefaultAzureCredential())
data_asset = ml_client.data.get(name=args.input_data, version=args.version)

df = pd.read_csv(data_asset.path)
print(df.head())
