# Exercise 1 — Image Data Inspection

## Overview

Learn how to load, inspect, and prepare image datasets for deep learning. You'll work with the **Serengeti balanced dataset** (camera trap wildlife images) to understand:

- How to load images using PIL and convert them to PyTorch tensors
- Tensor shapes: (Channels, Height, Width) — the standard format
- Pixel value ranges and normalization using ImageNet statistics
- Class distribution and identifying class imbalance
- Creating PyTorch DataLoaders for batched training

## Learning Objectives

After completing this exercise, you will:

- Load image datasets from Hugging Face Hub using `datasets.load_dataset()`
- Understand tensor shapes, data types, and pixel value ranges
- Apply image transforms: resizing, augmentation, and normalization
- Inspect batch shapes and create DataLoaders for training

## Estimated Time

25–30 minutes (including reading and debugging)

## Dataset

**Serengeti Balanced Dataset** (`marco-willi7/serengeti-balanced`)
A balanced wildlife camera trap dataset with multiple animal species. Automatically downloaded from Hugging Face Hub on first use.

## Structure

### solution.ipynb

The complete, working solution. Read this if you get stuck or want to see the expected output.

### exercise.ipynb

The exercise notebook with code stubs (`# YOUR CODE HERE` + `raise NotImplementedError`). This is what you'll fill in.

## How to Run

### Locally

```bash
# Install dependencies
pip install torch torchvision datasets numpy matplotlib pillow

# Open the notebook
jupyter notebook exercise.ipynb
```

### Google Colab

Click the "Open in Colab" link in the course materials to run directly in the browser.

## Hints

### Part 1 — Load a Single Image

- Use `load_dataset()` from the `datasets` library
- PIL Images can be displayed directly with `plt.imshow()`
- `transforms.ToTensor()` converts PIL/numpy to torch tensor AND scales values to [0, 1]

### Part 2 — Dataset Exploration

- Use `Counter` from the `collections` module to count labels
- Class imbalance can hurt model performance — watch for it!
- A ratio of max/min counts > 1.5× is generally considered imbalanced

### Part 3 — Normalization

- ImageNet statistics are pre-computed on the ImageNet dataset (1.2M images)
- Normalization shifts pixel values: `(x - mean) / std`
- After normalization, images can have negative values and values > 1 — this is normal!

### Part 4 — DataLoader

- Create a wrapper class that inherits from `torch.utils.data.Dataset`
- Implement `__len__()` and `__getitem__()` methods
- `DataLoader` handles batching, shuffling, and parallel loading

## Verification

Each part has a verification cell with assertions. Run them to check your work:

```python
assert img_tensor.shape == (3, 224, 224)
print("✓ Verification passed!")
```

## Common Errors

**Error:** `ModuleNotFoundError: No module named 'datasets'`
**Fix:** `pip install datasets`

**Error:** `RuntimeError: shape '[8, 3, 224, 224]' is invalid for input of size ...`
**Fix:** Check that your DataLoader is returning tuples of (images, labels) with correct shapes

**Error:** Normalized image looks "wrong"
**OK!** This is expected. Normalized images have pixel values centered at 0 with std=1. The visual appearance will be different from the original.

## Next Steps

- Exercise 2: Image Classification — train a ResNet-50 on camera trap images
- Read: Lecture on "Images as Data" and CNN fundamentals

## Questions?

Refer to the solution notebook for complete, working code. Ask your instructor during the exercise block!
