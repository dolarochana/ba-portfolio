"""
Healthcare Claims Denial Analysis - Exploratory Data Analysis
Portfolio recreation on public/synthetic claims data.

Demonstrates the Python EDA approach used to quantify denial drivers
before redesigning the submission workflow. Adjust column names to your dataset.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ---------------------------------------------------------------------
# 1. Load and inspect
# ---------------------------------------------------------------------
df = pd.read_csv("claims.csv")          # <- your public/synthetic claims file

print("Shape:", df.shape)
print(df.head())
print(df.info())
print("\nMissing values:\n", df.isna().sum())

# ---------------------------------------------------------------------
# 2. Basic cleaning
# ---------------------------------------------------------------------
df["claim_status"] = df["claim_status"].str.strip().str.title()
if "submission_date" in df.columns:
    df["submission_date"] = pd.to_datetime(df["submission_date"], errors="coerce")

# ---------------------------------------------------------------------
# 3. Overall denial rate
# ---------------------------------------------------------------------
denial_rate = (df["claim_status"] == "Denied").mean() * 100
print(f"\nOverall denial rate: {denial_rate:.1f}%")

# ---------------------------------------------------------------------
# 4. Root cause: denials by reason
# ---------------------------------------------------------------------
denied = df[df["claim_status"] == "Denied"]
reason_breakdown = (
    denied["denial_reason"]
    .value_counts(normalize=True)
    .mul(100)
    .round(1)
    .rename("pct_of_denials")
)
print("\nDenials by reason (% of total denials):")
print(reason_breakdown)

plt.figure(figsize=(8, 5))
reason_breakdown.sort_values().plot(kind="barh")
plt.xlabel("% of total denials")
plt.title("Denial Drivers — Root Cause Breakdown")
plt.tight_layout()
plt.savefig("denial_drivers.png", dpi=120)

# ---------------------------------------------------------------------
# 5. Denial rate by provider (operational drill-down)
# ---------------------------------------------------------------------
by_provider = (
    df.groupby("provider")["claim_status"]
    .apply(lambda s: (s == "Denied").mean() * 100)
    .round(1)
    .sort_values(ascending=False)
)
print("\nTop providers by denial rate:")
print(by_provider.head(10))

# ---------------------------------------------------------------------
# 6. Monthly trend
# ---------------------------------------------------------------------
if "submission_date" in df.columns:
    monthly = (
        df.set_index("submission_date")
        .resample("M")["claim_status"]
        .apply(lambda s: (s == "Denied").mean() * 100)
        .round(1)
    )
    plt.figure(figsize=(9, 4))
    monthly.plot(marker="o")
    plt.ylabel("Denial rate (%)")
    plt.title("Monthly Denial Rate Trend")
    plt.tight_layout()
    plt.savefig("denial_trend.png", dpi=120)

print("\nEDA complete. Charts saved as PNG for the dashboard/report.")
