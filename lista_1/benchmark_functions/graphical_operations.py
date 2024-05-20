import time
import torch
import torchvision.transforms as transforms
from PIL import Image

class GraphicalOperations:
    def perform_operations(self, image_path, repeats=100):
        # Load an image
        image = Image.open(image_path)

        # Define some transforms
        resize = transforms.Resize((1000, 1000))
        to_tensor = transforms.ToTensor()
        normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406],
                                         std=[0.229, 0.224, 0.225])

        total_time = 0

        # Repeat the operations multiple times
        for _ in range(repeats):
            start_time = time.time()

            image = resize(image)
            image = to_tensor(image)
            image = normalize(image)

            end_time = time.time()
            total_time += end_time - start_time

            # Reload the image for the next iteration
            image = Image.open(image_path)

        # Return the total execution time
        return total_time

if __name__ == "__main__":
    image_path = 'graphics_input.jpg'
    graphical_ops = GraphicalOperations()
    execution_time = graphical_ops.perform_operations(image_path)
    print("Total execution time:", execution_time, "seconds")