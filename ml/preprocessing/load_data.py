"""
Module Name : load_data.py

Purpose:
Load all datasets required for the project in a reusable way.

Author:
Team Forecast Engine

Project:
Time Series-Driven E-Commerce Sales Forecasting
and Intelligent Recommendation System
"""

from pathlib import Path

import pandas as pd


# Root Project Directory
PROJECT_ROOT = Path(__file__).resolve().parents[2]

# Raw Dataset Folder
RAW_DATA_PATH = PROJECT_ROOT / "ml" / "data" / "raw"


def load_dataset(filename: str) -> pd.DataFrame:
    """
    Load a CSV dataset from the raw data directory.

    Parameters
    ----------
    filename : str
        CSV file name.

    Returns
    -------
    pd.DataFrame
        Loaded dataset.
    """

    file_path = RAW_DATA_PATH / filename

    if not file_path.exists():
        raise FileNotFoundError(
            f"Dataset not found: {file_path}"
        )

    df = pd.read_csv(file_path)

    return df


def display_basic_info(df: pd.DataFrame, dataset_name: str) -> None:
    """
    Display basic information about the dataset.
    """

    print("=" * 60)
    print(f"Dataset : {dataset_name}")
    print("=" * 60)

    print(f"Rows    : {df.shape[0]}")
    print(f"Columns : {df.shape[1]}")

    print("\nColumns")
    print(df.columns.tolist())

    print("\nData Types")
    print(df.dtypes)

    print("\nFirst Five Rows")
    print(df.head())


def main():

    orders = load_dataset("olist_orders_dataset.csv")

    display_basic_info(
        orders,
        "Orders Dataset"
    )


if __name__ == "__main__":
    main()