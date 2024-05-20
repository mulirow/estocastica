import time
import os

class DiskOperations:
    def perform_operations(self, file_path, data_size=1000000, repeats=100):
        # Generate some data to write
        data = os.urandom(data_size)

        total_time = 0

        # Repeat the operations multiple times
        for _ in range(repeats):
            # Measure the time taken to write the data to a file
            start_time = time.time()
            with open(file_path, 'wb') as f:
                f.write(data)
            end_time = time.time()
            total_time += end_time - start_time

            # Measure the time taken to read the data from the file
            start_time = time.time()
            with open(file_path, 'rb') as f:
                _ = f.read()
            end_time = time.time()
            total_time += end_time - start_time

        # Return the total execution time
        return total_time

if __name__ == "__main__":
    file_path = 'disk_operations.bin'
    disk_ops = DiskOperations()
    execution_time = disk_ops.perform_operations(file_path)
    print("Total execution time:", execution_time, "seconds")