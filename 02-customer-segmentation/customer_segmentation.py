"""
Customer Segmentation - K-Means persona clustering
Portfolio recreation on public data. Adjust column names to your dataset.
"""
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

df = pd.read_csv("customers.csv")   # public segmentation dataset

features = ["balance", "txn_frequency", "products_held"]
X = StandardScaler().fit_transform(df[features])

inertia = []
for k in range(1, 10):
    inertia.append(KMeans(n_clusters=k, n_init=10, random_state=42).fit(X).inertia_)
plt.plot(range(1, 10), inertia, marker="o")
plt.xlabel("k"); plt.ylabel("inertia"); plt.title("Elbow Method")
plt.savefig("elbow.png", dpi=120)

km = KMeans(n_clusters=4, n_init=10, random_state=42)
df["segment"] = km.fit_predict(X)

profile = df.groupby("segment")[features].mean().round(1)
print("Segment profiles (mean values):")
print(profile)

persona_map = {0: "Dormant", 1: "Regular", 2: "Valuable", 3: "Premium"}
df["persona"] = df["segment"].map(persona_map)
df.to_csv("customers_segmented.csv", index=False)
print("\nSaved segmented customers for the Tableau dashboard.")
