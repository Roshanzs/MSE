"""
Basic data analytics script for WEEK3 activity.

The script reads the dataset, cleans common dirty numeric values,
computes descriptive and categorical summaries, and writes a human-readable
report plus CSV summaries to an output directory.
"""
from __future__ import annotations

import argparse
import os
import re
from datetime import datetime
from pathlib import Path
from typing import Dict

import numpy as np
import pandas as pd


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


def parse_numeric_text(value: object) -> float:
    """Convert strings such as '30,000', 'thirty-eight', or 'sixty five thousand' to numbers."""
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
        if not words:
            return np.nan

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
    """Load the CSV file and clean common dirty numeric values."""
    df = pd.read_csv(path, dtype=str, keep_default_na=True)

    for col in df.columns:
        df[col] = df[col].map(lambda x: x.strip() if isinstance(x, str) else x)

    numeric_cols = ["ID", "Age", "Net worth", "Salary"]
    for col in numeric_cols:
        if col in df.columns:
            df[col] = df[col].apply(parse_numeric_text)

    if "Join Date" in df.columns:
        df["Join Date"] = pd.to_datetime(df["Join Date"], errors="coerce")

    return df


def numeric_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Return descriptive statistics for numeric columns."""
    num = df.select_dtypes(include=[np.number])
    if num.shape[1] == 0:
        return pd.DataFrame()

    desc = num.describe().T
    median = num.median()
    q1 = num.quantile(0.25)
    q3 = num.quantile(0.75)
    missing = num.isna().sum()
    missing_pct = missing / len(df) * 100

    out = pd.DataFrame(
        {
            "count": desc["count"].astype(int),
            "missing_count": missing.astype(int),
            "missing_pct": missing_pct.round(3),
            "mean": desc["mean"].round(6),
            "median": median.round(6),
            "std": desc["std"].round(6),
            "min": desc["min"].round(6),
            "q1": q1.round(6),
            "q3": q3.round(6),
            "max": desc["max"].round(6),
        }
    )
    return out


def categorical_summary(df: pd.DataFrame, top_n: int = 3) -> pd.DataFrame:
    """Return summary for non-numeric columns: unique count and top values."""
    cat = df.select_dtypes(exclude=[np.number])
    rows = []
    for col in cat.columns:
        vc = cat[col].value_counts(dropna=False)
        top = "; ".join([f"{i} ({vc[i]})" for i in vc.index[:top_n]])
        rows.append(
            {
                "column": col,
                "unique": vc.shape[0],
                "top_values": top,
                "missing_count": int(cat[col].isna().sum()),
            }
        )
    return pd.DataFrame(rows).set_index("column")


def correlation_matrix(df: pd.DataFrame) -> pd.DataFrame:
    """Return Pearson correlation matrix for numeric columns."""
    num = df.select_dtypes(include=[np.number])
    if num.shape[1] == 0:
        return pd.DataFrame()
    return num.corr()


METRIC_EXPLANATIONS: Dict[str, str] = {
    "count": "Number of non-missing observations in the column. This tells you how many valid values are available for analysis.",
    "missing_count": "Number of missing values. A large value suggests data quality issues or incomplete records.",
    "missing_pct": "Percentage of rows with missing values. It shows how severe the gap is relative to the whole dataset.",
    "mean": "Arithmetic average. It represents the centre of the data but can be skewed by extreme values.",
    "median": "Median or middle value. It is more robust than the mean when outliers exist.",
    "std": "Standard deviation. It measures how spread out the values are around the mean.",
    "min": "Smallest recorded value. It helps define the lower bound of the observed data.",
    "q1": "25th percentile. One quarter of the values fall below this point.",
    "q3": "75th percentile. Three quarters of the values fall below this point.",
    "max": "Largest recorded value. It helps define the upper bound of the observed data.",
    "unique": "Number of distinct categories in a non-numeric column. It helps show variety in the data.",
    "top_values": "Most frequent categories and their counts. It reveals the dominant patterns in a categorical variable.",
    "correlation": "Pearson correlation coefficient: from -1 to +1. Values near +1 indicate strong positive association, near -1 strong negative association, and near 0 weak or no linear relationship.",
}


def write_report(
    df: pd.DataFrame,
    numeric_desc: pd.DataFrame,
    categorical_desc: pd.DataFrame,
    corr: pd.DataFrame,
    outdir: str,
):
    """Write the human-readable report and CSV summaries to disk."""
    os.makedirs(outdir, exist_ok=True)
    timestamp = datetime.now().isoformat(timespec="seconds")
    txt_path = os.path.join(outdir, f"analysis_report_{timestamp}.txt")

    with open(txt_path, "w", encoding="utf-8") as f:
        f.write(f"Analysis report\nGenerated: {timestamp}\n\n")
        f.write(f"Dataset shape: {df.shape[0]} rows, {df.shape[1]} columns\n\n")

        f.write("Numeric summaries:\n")
        if numeric_desc.empty:
            f.write("  (no numeric columns)\n\n")
        else:
            f.write(numeric_desc.to_string())
            f.write("\n\n")
            f.write("Metric explanations:\n")
            for key in ["count", "missing_count", "missing_pct", "mean", "median", "std", "min", "q1", "q3", "max"]:
                f.write(f"- {key}: {METRIC_EXPLANATIONS.get(key, '')}\n")
            f.write("\n")

        f.write("Categorical summaries:\n")
        if categorical_desc.empty:
            f.write("  (no categorical columns)\n\n")
        else:
            f.write(categorical_desc.to_string())
            f.write("\n\n")
            f.write("Categorical metric explanations:\n")
            for key in ["unique", "top_values"]:
                f.write(f"- {key}: {METRIC_EXPLANATIONS.get(key, '')}\n")
            f.write("\n")

        f.write("Correlations (Pearson):\n")
        if corr.empty:
            f.write("  (no numeric columns)\n")
        else:
            f.write(corr.to_string())
            f.write("\n\n")
            f.write(f"Correlation explanation: {METRIC_EXPLANATIONS['correlation']}\n")

    if not numeric_desc.empty:
        numeric_desc.to_csv(os.path.join(outdir, "numeric_summary.csv"))
    if not categorical_desc.empty:
        categorical_desc.to_csv(os.path.join(outdir, "categorical_summary.csv"))
    if not corr.empty:
        corr.to_csv(os.path.join(outdir, "correlations.csv"))


def main():
    base_dir = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description="Basic data analytics report")
    parser.add_argument("--input", "-i", default=str(base_dir / "Sample_dataset.csv"), help="Path to input CSV")
    parser.add_argument("--outdir", "-o", default=str(base_dir / "report_output"), help="Output directory for reports")
    args = parser.parse_args()

    input_path = Path(args.input).resolve()
    out_dir = Path(args.outdir).resolve()

    try:
        df = load_data(str(input_path))
    except FileNotFoundError:
        print(f"Input file not found: {input_path}")
        return

    numeric_desc = numeric_summary(df)
    categorical_desc = categorical_summary(df)
    corr = correlation_matrix(df)

    write_report(df, numeric_desc, categorical_desc, corr, str(out_dir))
    print(f"Report written to {out_dir}")


if __name__ == "__main__":
    main()
