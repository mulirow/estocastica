import time
import torch

class MatrixOperations:
    def perform_operations(self, size=512, repeats=100):
        # Create large matrices
        a = torch.randn(size, size)
        b = torch.randn(size, size)

        total_time = 0

        # Repeat the operations multiple times
        for _ in range(repeats):
            start_time = time.time()

            result = torch.mm(a, b)  # Matrix multiplication
            result = torch.t(result)  # Transpose
            result = torch.inverse(result)  # Inverse

            end_time = time.time()
            total_time += end_time - start_time

        # Return the total execution time
        return total_time

if __name__ == "__main__":
    matrix_ops = MatrixOperations()
    execution_time = matrix_ops.perform_operations()
    print("Total execution time:", execution_time, "seconds")