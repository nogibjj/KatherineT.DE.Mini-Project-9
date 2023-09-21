"""
Test goes here
"""
from mylib.lib import (sum_stats,hist,scatterplot)
import pandas as pd

# read dataset
cereal = pd.read_csv("cereal.csv", sep=";")

# define test function
def test_sum_stats():
    summary = sum_stats(cereal)
    assert (
        cereal["calories"].mean() == summary.loc["mean", "calories"]
    ), "Mean test failed"
    assert (
        cereal["protein"].median() == summary.loc["50%", "protein"]
    ), "Median test failed"
    assert (
        cereal["rating"].min() == summary.loc["min", "rating"]
    ), "Standard deviation test failed"
    print("All Test passed!")

def test_hist():
    hist(cereal)

def test_scatter():
    scatterplot(cereal)

# test
if __name__ == "__main__":
    test_sum_stats()
    test_hist()
