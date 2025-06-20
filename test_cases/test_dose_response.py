# This test compares expected vs. calculated drug responses.
# If the error between the two is more than 0.05, the test fails.

import pandas as pd
import pytest

def test_dose_response_accuracy():
    df = pd.read_csv('data/dose_response_with_failures.csv')
    expected = df['expected_response']
    actual = df['calculated_response']
    for i, (e, a) in enumerate(zip(expected, actual)):
        assert abs(e - a) <= 0.05, f"Sample {i+1} failed: Expected {e}, got {a}"
