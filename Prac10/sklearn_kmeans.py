import pandas as pd
import time

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load customer features
df = pd.read_csv("customer_features.csv")

features = [
    "Total_Spend",
    "Purchase_Frequency",
    "Average_Basket_Size",
    "Recency"
]

X = df[features]

# Scaling
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# K-Means
start = time.time()

kmeans = KMeans(
    n_clusters=5,
    random_state=42,
    n_init=10
)

kmeans.fit(X_scaled)

end = time.time()

print("----- SKLEARN K-MEANS -----")
print("Execution time:", end - start, "seconds")
print("WSSSE:", kmeans.inertia_)