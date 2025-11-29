# source/generate_data.py

import os
import numpy as np
import pandas as pd

from utils import ensure_directories


def generate_panel_data(
    n_units: int = 200,
    n_periods: int = 10,
    treatment_start: int = 6,
    treatment_share: float = 0.4,
    seed: int = 42,
) -> pd.DataFrame:
    """
    Generate a synthetic balanced panel dataset suitable for
    difference-in-differences analysis.

    Parameters
    ----------
    n_units : int
        Number of cross-sectional units (e.g., firms or regions).
    n_periods : int
        Number of time periods.
    treatment_start : int
        First period in which treated units are exposed to the policy.
        Periods are 1-indexed in the simulated data.
    treatment_share : float
        Share of units that are eventually treated.
    seed : int
        Random seed for reproducibility.

    Returns
    -------
    df : pandas.DataFrame
        Simulated panel dataset with columns:
        ['unit_id', 'time', 'treated', 'post', 'treat_post', 'y', 'x1', 'x2'].
    """
    rng = np.random.default_rng(seed)

    unit_ids = np.arange(1, n_units + 1)
    time_periods = np.arange(1, n_periods + 1)

    n_treated_units = int(treatment_share * n_units)
    treated_units = rng.choice(unit_ids, size=n_treated_units, replace=False)

    records = []

    # True parameters for data generation
    beta_0 = 2.0      
    beta_trend = 0.3  
    beta_treat = 0.0  
    beta_post = 0.1   
    beta_dd = 1.0     
    beta_x1 = 0.5
    beta_x2 = -0.3

    alpha_i = rng.normal(loc=0.0, scale=1.0, size=n_units)

    for i_idx, unit in enumerate(unit_ids):
        for t in time_periods:
            treated = 1 if unit in treated_units else 0
            post = 1 if t >= treatment_start else 0
            treat_post = treated * post

            x1 = rng.normal(loc=0.0, scale=1.0)
            x2 = rng.normal(loc=0.0, scale=1.0)

            eps = rng.normal(loc=0.0, scale=1.0)

            y = (
                beta_0
                + alpha_i[i_idx]
                + beta_trend * t
                + beta_treat * treated
                + beta_post * post
                + beta_dd * treat_post
                + beta_x1 * x1
                + beta_x2 * x2
                + eps
            )

            records.append(
                {
                    "unit_id": unit,
                    "time": t,
                    "treated": treated,
                    "post": post,
                    "treat_post": treat_post,
                    "x1": x1,
                    "x2": x2,
                    "y": y,
                }
            )

    df = pd.DataFrame.from_records(records)
    return df


def main() -> None:
    """Generate the synthetic dataset and write it to disk."""
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_processed = os.path.join(base_dir, "data", "processed")

    ensure_directories([data_processed])

    df = generate_panel_data()

    output_path = os.path.join(data_processed, "sim_panel.csv")
    df.to_csv(output_path, index=False)

    print(f"Synthetic panel data saved to: {output_path}")
    print(df.head())


if __name__ == "__main__":
    main()
