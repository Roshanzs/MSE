"""
Activity 2: continuing from Activity 1, with missing-value prediction using
linear regression and polynomial regression.
"""
from __future__ import annotations

import re
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures

NUMBER_WORDS = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90,
}


def parse_numeric_text(value):
    """Convert dirty numeric strings into numeric values."""
    if value is None or (isinstance(value, float) and np.isnan(value)):
        return np.nan
    text = str(value).strip()
    if text == "" or text.lower() == "nan":
        return np.nan

    text = text.replace(",", "").replace("$", "").strip()
    if re.fullmatch(r"-?\d+(?:\.\d+)?", text):
        return float(text)

    if re.search(r"[A-Za-z]", text):
        text = text.lower().replace("-", " ")
        words = text.split()
        total = 0
        current = 0
        for word in words:
            if word == "hundred":
                current *= 100
            elif word == "thousand":
                current *= 1000
                total += current
                current = 0
            elif word in NUMBER_WORDS:
                current += NUMBER_WORDS[word]
            else:
                return np.nan
        total += current
        return float(total)

    return np.nan


def load_data(path: str) -> pd.DataFrame:
    """Load data and clean common typos and numeric formats."""
    df = pd.read_csv(path, dtype=str, keep_default_na=True)

    for col in df.columns:
        df[col] = df[col].map(lambda x: x.strip() if isinstance(x, str) else x)

    for col in ["ID", "Age", "Net worth", "Salary"]:
        if col in df.columns:
            df[col] = df[col].apply(parse_numeric_text)

    if "Join Date" in df.columns:
        df["Join Date"] = pd.to_datetime(df["Join Date"], errors="coerce")

    return df


def build_features(df: pd.DataFrame, target_col: str) -> pd.DataFrame:
    """Create feature matrix excluding the target column."""
    candidate_cols = ["ID", "Age", "Net worth", "Salary"]
    feature_cols = [c for c in candidate_cols if c != target_col]
    X = df[feature_cols].copy()

    if "Country" in df.columns:
        country_dummies = pd.get_dummies(df["Country"], prefix="Country")
        X = pd.concat([X.reset_index(drop=True), country_dummies.reset_index(drop=True)], axis=1)

    X = X.fillna(X.median(numeric_only=True))
    return X


def compare_models(df: pd.DataFrame, target_col: str):
    """Train and compare linear vs polynomial regression for one target."""
    valid = df[df[target_col].notna()].copy()
    X = build_features(valid, target_col)
    y = valid[target_col]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42
    )

    linear_model = LinearRegression()
    linear_model.fit(X_train, y_train)
    y_linear_pred = linear_model.predict(X_test)

    poly = PolynomialFeatures(degree=2, include_bias=False)
    X_poly_train = poly.fit_transform(X_train)
    X_poly_test = poly.transform(X_test)
    poly_model = LinearRegression()
    poly_model.fit(X_poly_train, y_train)
    y_poly_pred = poly_model.predict(X_poly_test)

    metrics = {
        "Linear Regression": {
            "MAE": mean_absolute_error(y_test, y_linear_pred),
            "MSE": mean_squared_error(y_test, y_linear_pred),
            "R2": r2_score(y_test, y_linear_pred),
        },
        "Polynomial Regression": {
            "MAE": mean_absolute_error(y_test, y_poly_pred),
            "MSE": mean_squared_error(y_test, y_poly_pred),
            "R2": r2_score(y_test, y_poly_pred),
        },
    }

    best_model_name = min(
        metrics,
        key=lambda name: (metrics[name]["MAE"], metrics[name]["MSE"]),
    )

    return metrics, best_model_name, linear_model, poly_model, poly


def impute_missing_values(df: pd.DataFrame):
    """Fill missing values using both models and compare them."""
    result = {}
    for target_col in ["Age", "Net worth", "Salary"]:
        missing_idx = df.index[df[target_col].isna()].tolist()
        if not missing_idx:
            continue

        metrics, best_model_name, linear_model, poly_model, poly = compare_models(df, target_col)

        X_all = build_features(df, target_col)
        missing_mask = df[target_col].isna()
        X_missing = X_all[missing_mask]

        linear_pred = linear_model.predict(X_missing)
        poly_pred = poly_model.predict(poly.transform(X_missing))

        result[target_col] = {
            "missing_rows": missing_idx,
            "linear_predictions": linear_pred,
            "poly_predictions": poly_pred,
            "metrics": metrics,
            "best_model": best_model_name,
        }

        print(f"\nTarget: {target_col}")
        print("Model comparison:")
        for model_name, m in metrics.items():
            print(
                f"  {model_name}: MAE={m['MAE']:.4f}, "
                f"MSE={m['MSE']:.4f}, R2={m['R2']:.4f}"
            )
        print(f"Best model: {best_model_name}")
        print("Predicted missing values:")
        for row_idx, lin_val, poly_val in zip(
            missing_idx, linear_pred, poly_pred
        ):
            print(
                f"  Row {row_idx}: "
                f"Linear={lin_val:.2f}, Polynomial={poly_val:.2f}"
            )

    return result


def main():
    data_path = Path(__file__).resolve().parent.parent / "activity1" / "Sample_dataset.csv"
    df = load_data(str(data_path))
    print("Cleaned dataset:\n")
    print(df)
    print("\nMissing values before prediction:")
    print(df.isna().sum())

    result = impute_missing_values(df)

    print("\nInterpretation:")
    print(
        "Linear regression assumes the relationship between variables is approximately straight-line. "
        "Polynomial regression allows curves, so it often performs better when the relationship is non-linear. "
        "We compare models using MAE and R2 on the known data before deciding which model is more reliable for the missing values."
    )

    for target_col, info in result.items():
        print(f"\n{target_col}:")
        print(f"  Best model: {info['best_model']}")
        lin_mae = info["metrics"]["Linear Regression"]["MAE"]
        poly_mae = info["metrics"]["Polynomial Regression"]["MAE"]
        lin_r2 = info["metrics"]["Linear Regression"]["R2"]
        poly_r2 = info["metrics"]["Polynomial Regression"]["R2"]

        if info["best_model"] == "Polynomial Regression":
            print(
                "  Conclusion: polynomial regression gives better predictions because it has lower MAE and/or higher R2 than linear regression."
            )
        else:
            print(
                "  Conclusion: linear regression gives better predictions because its MAE is lower and its R2 is stronger."
            )

        print(f"  Linear: MAE={lin_mae:.4f}, R2={lin_r2:.4f}")
        print(f"  Polynomial: MAE={poly_mae:.4f}, R2={poly_r2:.4f}")


if __name__ == "__main__":
    main()
