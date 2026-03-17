import argparse
import mltable
from sklearn.model_selection import train_test_split, KFold
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression, SGDClassifier
from sklearn.metrics import precision_recall_fscore_support, accuracy_score
from sklearn.preprocessing import MinMaxScaler
import mlflow
import os
import joblib
from math import ceil


### LOAD DATA

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--train-data", dest="train_data", type=str, required=True)
    parser.add_argument("--test-data", dest="test_data", type=str, required=True)
    parser.add_argument("--alpha", dest="alpha", type=float, required=False)
    parser.add_argument("--max-iter", dest="max_iter", type=int, required=False)
    return parser.parse_args()

def load_dataframe(data_asset, local=False):
    if local:
        df = pd.read_csv(data_asset)
    else:
        tbl = mltable.load(data_asset)
        df = tbl.to_pandas_dataframe()
    return df 

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

### Early stopping:

def split_k(dataset, k):
    p = ceil(dataset.shape[0] / k)
    l,n = [], 0
    for i in range(k):
        ub = n + p if (n + p) <= dataset.shape[0] else dataset.shape[0]
        l.append(range(n,ub))
        n += p
    return l


### MAIN


def main(
     df_train
    ,df_test
    ,hyperparameters
    ):

    # Create train and test sets
    X_train = df_train[get_features()].to_numpy()
    y_train = df_train[get_target()].to_numpy().ravel()
    X_test  = df_test[get_features()].to_numpy()
    y_test  = df_test[get_target()].to_numpy().ravel()

    with mlflow.start_run() as run:

        lr = SGDClassifier(loss="log_loss", **hyperparameters)
        mlflow.log_params(lr.get_params())

        for i, r in enumerate(split_k(X_train, k=3)):
            
            X_train_sub = X_train[r[0]:r[-1],:]
            y_train_sub = y_train[r[0]:r[-1]]

            # Train model 
            lr.fit(X_train_sub, y_train_sub)

            # test model
            y_pred = lr.predict(X_test)
            accuracy = accuracy_score(y_test, y_pred)

            # Log to MLFlow to support early stopping
            mlflow.log_metric("accuracy", accuracy, step=i+1)

        # Log params
        mlflow.log_params(lr.get_params())

        # Validate
        y_pred = lr.predict(X_test)
        precision, recall, fscore, _ = precision_recall_fscore_support(y_test, y_pred)

        mlflow.log_metrics({
             "precision"    : float(precision[1])
            ,"recall"       : float(recall[1]) 
            ,"fscore"       : float(fscore[1])
        })

        model_path = "./outputs"
        os.makedirs(model_path, exist_ok=True)

        joblib.dump(lr, os.path.join(model_path, "model.pkl"))





### EXECUTE

if __name__ == "__main__":

    # Load arguments
    args = parse_args()

    # Set hyperparameters
    hyperparameters = dict(
         alpha      = args.alpha
        ,max_iter   = int(args.max_iter)
    )
    
    # Load data
    df_train    = load_dataframe(args.train_data)
    df_test     = load_dataframe(args.test_data)

    main(
         df_train
        ,df_test
        ,hyperparameters = hyperparameters
    )