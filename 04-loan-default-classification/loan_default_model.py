"""
Loan Default Classification - imbalanced data
Portfolio recreation on a public loan dataset.
"""
import pandas as pd
from imblearn.over_sampling import SMOTE
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, average_precision_score, f1_score

df = pd.read_csv("loans.csv")
X = df.drop(columns=["default"])
y = df["default"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42)

# Address ~5% class imbalance
X_res, y_res = SMOTE(random_state=42).fit_resample(X_train, y_train)

for name, model in [("LogReg", LogisticRegression(max_iter=1000)),
                    ("RandomForest", RandomForestClassifier(n_estimators=200, random_state=42))]:
    model.fit(X_res, y_res)
    proba = model.predict_proba(X_test)[:, 1]
    pred = model.predict(X_test)
    print(f"{name}: ROC-AUC={roc_auc_score(y_test, proba):.3f}  "
          f"PR-AUC={average_precision_score(y_test, proba):.3f}  "
          f"F1={f1_score(y_test, pred):.3f}")

# Business threshold rules (probability -> underwriting action)
def underwriting_action(p):
    if p < 0.20:  return "Approve"
    if p < 0.50:  return "Review"
    return "Decline"
