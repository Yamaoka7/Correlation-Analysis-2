import pandas as pd

def correlation_analysis(data):
    correlation_matrix = data.corr()
    return correlation_matrix

# Example usage:
data = pd.read_csv("data.csv")
correlation_matrix = correlation_analysis(data)
print(correlation_matrix)
