
import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("--data-asset", type=str)
args = parser.parse_args()

df = pd.read_csv(args.data_asset)
print(df.head())
