# Credit Score Prediction — Random Forest + Business Thresholds

**Portfolio recreation on a public credit dataset.** Reproduces the modeling and the BA threshold-definition work from the original engagement.

## Business problem
Identify customers at risk of credit-score deterioration early enough to intervene.

## BA approach
- Defined the business problem and specified 12 input features (with Legal sign-off in the original).
- Set the model acceptance criterion up front: ROC-AUC > 0.75.
- Translated feature importance into a plain-language business rule: customers consistently exceeding 30% credit utilisation are ~3.5x more likely to deteriorate.
- Built a Tableau risk-tier dashboard with drill-down to individual profiles.

## What's in this folder
- `credit_risk_model.py` — EDA, Random Forest, evaluation (MAE/RMSE/R2, ROC-AUC), feature importance

## Note
The 0.81 / 0.45 correlations and 30% threshold are from the original analysis; figures here are illustrative on public data.

Dashboard: [public.tableau.com/profile/rochana.dixit](https://public.tableau.com/profile/rochana.dixit)
