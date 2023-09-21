"""
Test Cases
"""

# import functions
from main import generate_summary,generate_graph,generate_markdown
import pandas as pd

cereal = pd.read_csv("cereal.csv", sep=";")

# test cases
def test_markdown():
    generate_markdown(cereal)

if __name__ == "__main__":
    test_markdown()