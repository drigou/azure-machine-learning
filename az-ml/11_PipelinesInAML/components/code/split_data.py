
import argparse
from sklearn.model_selection import train_test_split
import mltable
from math import ceil, floor
import numpy as np
import os

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input-data", dest="input_data", type=str, required=True)
    parser.add_argument("--train-output", dest="train_output", type=str, required=False)
    parser.add_argument("--test-output", dest="test_output", type=str, required=False)
    parser.add_argument("--test-size", dest="test_size", type=float, required=True)
    parser.add_argument("--random-state", dest="random_state", type=int, required=False)
    return parser.parse_args()

### 

def split_data(
         input_data
        ,test_split=0.3
        ,random_state=None
        ):

    # Set random state
    random_state = np.random.randint(low=1, high=1e8) if not random_state else random_state
    rs = np.random.RandomState(random_state)

    # Load data
    df = mltable.load(input_data).to_pandas_dataframe()

    # create an index
    test_size = int(floor(len(df) * test_split))
    idx = rs.choice(np.array(df.index), size=test_size, replace=False)

    df_test     = df.loc[idx,:]
    df_train    = df[~df.index.isin(idx)]

    return df_train, df_test

def save_as_mltable(df, output_path):

    # Make directory
    os.makedirs(output_path, exist_ok=True)

    # Create the data filename
    data_filename = "data.csv"
    df.to_csv(os.path.join(output_path, data_filename), index=False)

    # Create the YAML
    mltable_yaml = \
        "paths:" \
        f"\n   - file: ./{data_filename}" \
        "\ntransformations:" \
        "\n   - read_delimited:" \
        "\n       delimiter: ','" \
        "\n       encoding: 'ascii'" \
        "\n       header: 'all_files_same_headers'"
    
    # write the YAML 
    with open(os.path.join(output_path, "MLTable"), "w") as f:
        f.write(mltable_yaml)


if __name__ == "__main__":

    # Parse the arguments
    args = parse_args()

    df_train, df_test = split_data(
         input_data     = args.input_data
        ,test_split     = args.test_size
        ,random_state   = args.random_state
        )

    if args.train_output:
        save_as_mltable(df_train, args.train_output)

    if args.test_output:
        save_as_mltable(df_test, args.test_output)

