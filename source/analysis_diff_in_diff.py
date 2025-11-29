# source/analysis_diff_in_diff.py

import os
import pandas as pd
import statsmodels.formula.api as smf

from utils import ensure_directories


def load_data() -> pd.DataFrame:
    """Load the processed synthetic panel dataset."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_processed = os.path.join(base_dir, "data", "processed")
    file_path = os.path.join(data_processed, "sim_panel.csv")

    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"Data file not found at {file_path}. "
            f"Run `python src/generate_data.py` first."
        )

    df = pd.read_csv(file_path)
    return df


def run_diff_in_diff(df: pd.DataFrame):
    """
    Estimate a difference-in-differences regression with unit and time fixed effects.

    Model:
        y_it = a_i + λ_t + β * (treated_i * post_t) + γ1 x1_it + γ2 x2_it + ε_it

    We implement this by including unit and time dummies via C(unit_id) and C(time).
    """
    print("Data preview:")
    print(df.head())
    print("\nBasic summary:")
    print(df.describe())

    # Difference-in-differences regression
    formula = "y ~ treated:post + x1 + x2 + C(unit_id) + C(time)"
    model = smf.ols(formula=formula, data=df)
    results = model.fit(cov_type="cluster", cov_kwds={"groups": df["unit_id"]})

    return results


def main() -> None:
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_processed = os.path.join(base_dir, "data", "processed")
    ensure_directories([data_processed])

    df = load_data()
    results = run_diff_in_diff(df)

    print("\nDifference-in-Differences Results:")
    print(results.summary().tables[1])

    # Save the regression table to a text file
    output_path = os.path.join(data_processed, "did_results.txt")
    with open(output_path, "w") as f:
        f.write(results.summary().as_text())

    print(f"\nRegression results saved to: {output_path}")


if __name__ == "__main__":
    main()
