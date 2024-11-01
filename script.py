import pandas as pd
import sys
import os

def main(input_file, output_file):
    # Check if the input file exists 
    if not os.path.isfile(input_file):
        print(f"Error: The file '{input_file}' does not exist.")
        return

    # Load and read the data
    try:
        data = pd.read_csv(input_file)
    except Exception as e:
        print(f"Error reading the CSV file: {e}")
        return

    # Perform analysis
    metrics = {}
    metrics['average'] = data['metric_column'].mean()
    metrics['max'] = data['metric_column'].max()
    metrics['min'] = data['metric_column'].min()
    metrics['std_dev'] = data['metric_column'].std()

    # Generate report
    with open(output_file, 'w') as file:
        for key, value in metrics.items():
            file.write(f"{key.capitalize()}: {value}\n")

if __name__ == "__main__":
    # Command-line arguments
    input_file = sys.argv[1] if len(sys.argv) > 1 else 'data/metrics.csv'
    output_file = sys.argv[2] if len(sys.argv) > 2 else 'report.txt'
    main(input_file, output_file)
