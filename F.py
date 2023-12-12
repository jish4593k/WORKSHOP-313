import torch
from torchvision import transforms
from torch.utils.data import DataLoader
from PIL import Image
import tkinter as tk
from tkinter import ttk
import os


transform = transforms.Compose([
    transforms.RandomRotation(40),
    transforms.RandomHorizontalFlip(),
    transforms.RandomVerticalFlip(),
    transforms.RandomResizedCrop(150),
    transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2, hue=0.2),
    transforms.ToTensor(),
])

# Load the image
img = Image.open('data/test/2.jpg')

# Transform the image
transformed_img = transform(img)
transformed_img = transformed_img.unsqueeze(0)  # Add batch dimension


os.makedirs('preview', exist_ok=True)

# Save the original image
img.save('preview/original.jpg')


for i in range(36):
    augmented_img = transforms.functional.to_pil_image(transformed_img[0])
    augmented_img.save(f'preview/augmented_{i + 1}.jpg')


root = tk.Tk()
root.title("Augmented Image Preview")


original_label = tk.Label(root, text="Original Image")
original_label.pack()
original_image = tk.PhotoImage(file='preview/original.jpg')
original_image_label = tk.Label(root, image=original_image)
original_image_label.pack()


augmented_labels = tk.Label(root, text="Augmented Images")
augmented_labels.pack()

augmented_images = []
for i in range(1, 37):
    augmented_image = tk.PhotoImage(file=f'preview/augmented_{i}.jpg')
    augmented_images.append(augmented_image)
    augmented_image_label = tk.Label(root, image=augmented_image)
    augmented_image_label.pack()

root.mainloop()
