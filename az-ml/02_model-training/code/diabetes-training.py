
import pandas as pd
import numpy as np
import logging
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.metrics import roc_curve
from sklearn.preprocessing import MinMaxScaler

# 1. Get the data

df = pd.read_csv("../../data/diabetes-data/diabetes.csv")

# 2. Preprocess

X, y = df.drop(["PatientID","Diabetic"], axis=1).values, df["Diabetic"].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

scaler = MinMaxScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 3. Train model

reg = 0.01
model = LogisticRegression(C=1/reg, solver="liblinear").fit(X_train_scaled, y_train)
preds = model.predict(X_test_scaled)

# 4. Evaluate

acc = np.average(preds == y_test)
print(f"Accuracy: {acc}")

pred_scores = model.predict_proba(X_test)
auc = roc_auc_score(y_test,pred_scores[:,1])
print('AUC: ' + str(auc))
