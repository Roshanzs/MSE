import pandas as pd
from ucimlrepo import fetch_ucirepo

iris = fetch_ucirepo(id=53)
features = iris.data.features
targets = iris.data.targets

dataset = pd.concat([features, targets], axis=1)
duplicate_rows = dataset.duplicated()

print(f"Number of features: {features.shape[1]}")
print(f"Number of classes: {targets.iloc[:, 0].nunique()}")
print("Class names:", ", ".join(sorted(targets.iloc[:, 0].unique())))
print(f"Number of duplicate records: {duplicate_rows.sum()}")

if duplicate_rows.any():
    print("\nDuplicate records:")
    print(dataset[duplicate_rows])
