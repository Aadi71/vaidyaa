import pandas as pd
import numpy as np
from xgboost import XGBClassifier
from sklearn.model_selection import train_test_split


def heart_disease(sample):
    data = pd.read_csv('heart.csv')

    y = data["target"]
    new_x = data.drop(columns=['target', 'fbs'], axis=1)

    X_train, X_test, y_train, y_test = train_test_split(new_x, y, test_size=0.35, random_state=10)

    fmodel = XGBClassifier(max_depth=3, n_estimators=350, learning_rate=0.1, min_child_weight=3, colsample_bytree=0.2,
                           reg_lambda=4)
    fmodel.fit(X_train, y_train)

    out1 = pd.DataFrame(sample,
                        columns=['age', 'sex', 'cp', 'trestbps', 'chol', 'restecg', 'thalach', 'exang', 'oldpeak',
                                 'slope', 'ca', 'thal'])

    y_pred = fmodel.predict(out1)
    return y_pred


# if (y_pred == 1):
#     print("RISK OF HEART DISEASE")
# else:
#     print("NO RISK OF HEART DISEASE")
# sample = [[52, 1, 0, 125, 212, 1, 168, 0, 1, 2, 2, 3]]
# print(heart_disease(sample))