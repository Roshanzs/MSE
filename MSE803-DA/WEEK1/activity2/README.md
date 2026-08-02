# Activity 2: Iris Dataset Exploration and Analysis

## Understanding

The Iris dataset is a classic classification dataset created by R. A. Fisher. Each record describes one iris flower using four numeric measurements. The target column identifies the flower species.

## Findings

- Number of records: 150
- Number of features: 4
  - sepal length
  - sepal width
  - petal length
  - petal width
- Number of classes: 3
  - Iris-setosa
  - Iris-versicolor
  - Iris-virginica
- Number of duplicate records: 3

The duplicate count uses `DataFrame.duplicated()`, so it counts rows repeated after their first occurrence. These three rows belong to two duplicate groups: one group of three identical Iris-setosa records and one pair of identical Iris-virginica records.

## Steps Followed

1. Loaded the Iris dataset from the UCI Machine Learning Repository using `ucimlrepo`.
2. Retrieved the feature and target data as pandas DataFrames.
3. Combined the feature and target data into one DataFrame so a full record, including its class, is checked for duplication.
4. Counted features with `features.shape[1]`.
5. Counted classes with `targets.iloc[:, 0].nunique()`.
6. Identified duplicate rows with `dataset.duplicated()` and counted them with `.sum()`.

## Run the Analysis

From the `WEEK1/activity2` directory, run:

```bash
../../.venv/bin/python iris_analysis.py
```

Or activate the virtual environment from the repository root first:

```bash
source .venv/bin/activate
cd WEEK1/activity2
python iris_analysis.py
```
