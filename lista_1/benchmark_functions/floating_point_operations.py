import time
import torch

class FloatingPointOperations:
    def perform_operations(self, size=1000000, repeats=100):
        # Create large tensors of floating point numbers
        a = torch.rand(size)
        b = torch.rand(size)

        total_time = 0

        # Repeat the operations multiple times
        for _ in range(repeats):
            start_time = time.time()

            result = torch.add(a, b)
            result = torch.subtract(result, a)
            result = torch.multiply(result, b)
            result = torch.divide(result, a)

            end_time = time.time()
            total_time += end_time - start_time

        # Return the execution time
        return total_time

if __name__ == "__main__":
    float_ops = FloatingPointOperations()
    execution_time = float_ops.perform_operations()
    print("Total execution time:", execution_time, "seconds")