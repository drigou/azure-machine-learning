
import argparse
import glob
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument("--input-data", type=str)

args = parser.parse_args()

data_path = args.input_data
all_files = glob.glob(data_path + "/*.csv")

df = pd.concat((pd.read_csv(f) for f in all_files), sort=False)
