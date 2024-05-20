import time
import torch

class IntegerOperations:
    def perform_operations(self, size=1000000, repeats=100):
        # Create large tensors
        a = torch.randint(low=1, high=100, size=(size,))
        b = torch.randint(low=1, high=100, size=(size,))

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
    integer_ops = IntegerOperations()
    execution_time = integer_ops.perform_operations()
    print("Total execution time:", execution_time, "seconds")