import pandas as pd

# Load data
data = pd.read_csv('data/metrics.csv')

# Perform analysis
average_value = data['metric_column'].mean()
max_value = data['metric_column'].max()

# Generate report
with open('report.txt', 'w') as file:
    file.write(f"Average: {average_value}\n")
    file.write(f"Max: {max_value}\n")
