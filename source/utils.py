# source/utils.py

import os
from typing import List


def ensure_directories(paths: List[str]) -> None:
    """
    Ensure that each directory in `paths` exists. If not, create it.

    Parameters
    ----------
    paths : list of str
        List of directory paths to create if missing.
    """
    for p in paths:
        os.makedirs(p, exist_ok=True)
