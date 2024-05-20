import csv
from benchmark_functions.integer_operations import IntegerOperations
from benchmark_functions.floating_point_operations import FloatingPointOperations
from benchmark_functions.matrix_operations import MatrixOperations
from benchmark_functions.graphical_operations import GraphicalOperations
from benchmark_functions.disk_operations import DiskOperations

# Define the number of times to run each operation
N = 30

# Define the paths for the image and file for the graphical and disk operations
image_path = 'graphics_input.jpg'
file_path = 'disk_operations.bin'

# Initialize the operation classes
matrix_ops = MatrixOperations()
graphical_ops = GraphicalOperations()
disk_ops = DiskOperations()
floating_point_ops = FloatingPointOperations()
integer_ops = IntegerOperations()

# Define a dictionary to store the results
results = {
    'Integer Operations Time': [],
    'Floating Point Operations Time': [],
    'Matrix Operations Time': [],
    'Graphical Operations Time': [],
    'Disk Operations Time': []
}

# Run the operations and save the results
for _ in range(N):
    integer_time = integer_ops.perform_operations()
    results['Integer Operations Time'].append(integer_time)
    print("Integer Operations Time:", integer_time)

for _ in range(N):
    floating_point_time = floating_point_ops.perform_operations()
    results['Floating Point Operations Time'].append(floating_point_time)
    print("Floating Point Operations Time:", floating_point_time)

for _ in range(N):
    matrix_time = matrix_ops.perform_operations()
    results['Matrix Operations Time'].append(matrix_time)
    print("Matrix Operations Time:", matrix_time)

for _ in range(N):
    graphical_time = graphical_ops.perform_operations(image_path)
    results['Graphical Operations Time'].append(graphical_time)
    print("Graphical Operations Time:", graphical_time)

for _ in range(N):
    disk_time = disk_ops.perform_operations(file_path)
    results['Disk Operations Time'].append(disk_time)
    print("Disk Operations Time:", disk_time)

# Write the results to a CSV file
with open('results.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(results.keys())
    writer.writerows(zip(*results.values()))