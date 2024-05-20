import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

# Read the CSV files into pandas DataFrames
df1 = pd.read_csv('results1.csv')
df2 = pd.read_csv('results2.csv')

# Ensure the operations are the same and in the same order in both files
assert all(df1.columns == df2.columns), "The operations in the two files do not match."

# Determine the types of the operations
operation_types = []
for operation in df1.columns:
    operation_type = operation.split('_')[-1]
    if operation_type not in operation_types:
        operation_types.append(operation_type)

# Open the report file
with open('report.txt', 'w') as f:
    # For each operation type
    for operation_type in operation_types:
        # Get the operations of this type
        operations = [operation for operation in df1.columns if operation.split('_')[-1] == operation_type]

        # Generate a graph for each operation
        for operation in operations:
            plt.figure(figsize=(10, 6))
            plt.plot(df1[operation], label='PC_1')
            plt.plot(df2[operation], label='PC_2')
            plt.title(f'Execution time for {operation}')
            plt.xlabel('Execution (nº)')
            plt.ylabel('Time (s)')
            plt.legend()
            plt.savefig(f'{operation}.png')
            plt.close()

        # Write the mean execution time for each operation in each file and their difference
        f.write(f"\n\nMean execution time for {operation_type} operations:\n")
        f.write(f"File 1: {df1[operations].mean().values[0]:.6f}\n")
        f.write(f"File 2: {df2[operations].mean().values[0]:.6f}\n")
        f.write(f"Diff. : {abs(df1[operations].mean() - df2[operations].mean()).values[0]:.6f}\n")
        f.write(f"% Diff: {(abs(df1[operations].mean() - df2[operations].mean()) / df1[operations].mean() * 100).values[0]:.2f}%\n")

        # Write the median execution time for each operation in each file and their difference
        f.write(f"\n\nMedian execution time for {operation_type} operations:\n")
        f.write(f"File 1: {df1[operations].median().values[0]:.6f}\n")
        f.write(f"File 2: {df2[operations].median().values[0]:.6f}\n")
        f.write(f"Diff. : {abs(df1[operations].median() - df2[operations].median()).values[0]:.6f}\n")
        f.write(f"% Diff: {(abs(df1[operations].median() - df2[operations].median()) / df1[operations].median() * 100).values[0]:.2f}%\n")

        # Write the standard deviation of the execution time for each operation in each file and their difference
        f.write(f"\n\nStandard deviation of execution time for {operation_type} operations:\n")
        f.write(f"File 1: {df1[operations].std().values[0]:.6f}\n")
        f.write(f"File 2: {df2[operations].std().values[0]:.6f}\n")
        f.write(f"Diff. : {abs(df1[operations].std() - df2[operations].std()).values[0]:.6f}\n")
        f.write(f"% Diff: {(abs(df1[operations].std() - df2[operations].std()) / df1[operations].std() * 100).values[0]:.2f}%\n")

        # Perform a paired t-test to check if the differences in mean execution times are statistically significant
        for operation in operations:
            t_stat, p_val = stats.ttest_rel(df1[operation], df2[operation])
            f.write(f"\n\nPaired t-test for {operation}:\n")
            f.write(f"T-statistic: {t_stat:.6f}, p-value: {p_val:.6f}")

        # Separator
        f.write("\n" + "-" * 50 + "\n")