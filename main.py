"""
Main
"""

# import pandas and pyplot
from mylib.lib import sum_stats, hist, scatterplot


def generate_summary(data):
    summary = sum_stats(data)
    return summary
  

def generate_markdown(data):
    """generate an md file with outputs"""
    summary = sum_stats(data)
    markdown_table = summary.to_markdown()
    hist(data)
    scatterplot(data)
    # Write the markdown table to a file
    with open("output.md", "w", encoding="utf-8") as file:
        file.write("Summary:\n")
        file.write(markdown_table)
        file.write("\n\n")  # Add a new line
        file.write("![hist](Cereal Calories.png)\n")
        file.write("\n\n")  # Add a new line
        file.write("![scatterplot](Cereal Scatter.png)\n")
