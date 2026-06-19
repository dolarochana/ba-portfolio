"""
Credit Score Prediction - Random Forest
Portfolio recreation on a public credit dataset.
"""
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import roc_auc_score, classification_report

df = pd.read_csv("credit.csv")

# Correlation scan to find strongest drivers (BA uses this to define the business rule)
print(df.corr(numeric_only=True)["deteriorated"].sort_values())

X = df.drop(columns=["deteriorated"])
y = df["deteriorated"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

proba = model.predict_proba(X_test)[:, 1]
print("ROC-AUC:", round(roc_auc_score(y_test, proba), 3), "(acceptance bar: > 0.75)")
print(classification_report(y_test, model.predict(X_test)))

# Feature importance -> translated into the business recommendation
importance = pd.Series(model.feature_importances_, index=X.columns).sort_values(ascending=False)
print("\nTop drivers:\n", importance.head(5))
