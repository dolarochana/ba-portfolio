# Loan Default Risk Classification — Imbalanced Data + Risk Tiers

**Portfolio recreation on a public loan dataset.**

## Business problem
Predict borrower default on an imbalanced dataset (~5% default rate) and translate model scores into an operational underwriting workflow.

## BA approach
- Applied SMOTE to address class imbalance; benchmarked Logistic Regression vs Random Forest on Accuracy, F1, ROC-AUC, and Precision-Recall AUC.
- Facilitated the calibration decision with the credit team by framing it in financial terms: false negative (~$45K average default cost) vs false positive (~$25 intervention cost) — leading the team to maximise recall.
- Defined Approve / Review / Decline threshold rules mapping model probability to underwriting action.

## What's in this folder
- `loan_default_model.py` — SMOTE, model comparison, precision-recall trade-off, threshold logic

Dashboard: [public.tableau.com/profile/rochana.dixit](https://public.tableau.com/profile/rochana.dixit)
