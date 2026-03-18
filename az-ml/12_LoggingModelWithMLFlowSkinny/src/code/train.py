import argparse
import mltable
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_recall_fscore_support, roc_auc_score
import mlflow
from mlflow.models import infer_signature 
from datetime import datetime as dt


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
    model = RandomForestClassifier(n_estimators=80, criterion="gini")
    mlflow.log_params(model.get_params())

    model.fit(X_train, y_train)

    # Validate
    y_pred = model.predict(X_test)

    # Metrics
    accuracy = accuracy_score(y_test, y_pred)
    auc = roc_auc_score(y_test, y_pred)
    precision, recall, fscore, _ = precision_recall_fscore_support(y_test, y_pred)

    mlflow.log_metrics({
         "accuracy" : accuracy
        ,"precision" : precision[1]
        ,"recall": recall[1]
        ,"fscore": fscore[1]
        ,"auc": auc    
    })

    # Log model
    signature = infer_signature(
            model_input     = df.iloc[:4,:]
        ,model_output    = y_pred[:4]
        )

    mlflow.sklearn.log_model(model, "model", signature=signature)

    print(accuracy)


### EXECUTE

if __name__ == "__main__":
    main()