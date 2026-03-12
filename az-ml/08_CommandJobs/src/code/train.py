import argparse
import mltable
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

### LOAD DATA

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-asset", type=str)
    return parser.parse_args()

def load_dataframe(data_asset):
    tbl = mltable.load(data_asset)
    return tbl.to_pandas_dataframe()


### preprocess

def get_features():
    return [
     "Pregnancies"
    ,"PlasmaGlucose"
    ,"DiastolicBloodPressure"
    ,"TricepsThickness"
    ,"SerumInsulin"
    ,"BMI"
    ,"DiabetesPedigree"
    ,"Age"
    ]

def get_target():
    return ["Diabetic"]
    
def preprocess(df):

    # Split in features and targets
    X, y = df[get_features()].to_numpy(), df[get_target()].to_numpy()

    # Split the data in train and test
    return train_test_split(X, y, test_size=0.3, random_state=42)


### MAIN

def main():

    # Parse 
    args = parse_args()
    
    # Load data
    df = load_dataframe(args.data_asset)

    # preprocess
    X_train, X_test, y_train, y_test = preprocess(df)

    # Train model 
    lr = LogisticRegression()
    lr.fit(X_train, y_train)

    # Validate
    y_pred = lr.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(accuracy)


### EXECUTE

if __name__ == "__main__":
    main()