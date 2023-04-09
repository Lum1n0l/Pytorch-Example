import torch

# Below is an example of a matrix

MATRIX = torch.tensor([[7, 8], [9, 10]])
print(MATRIX)

# Wow! More numbers! Matrices are as flexible as vectors, except they've got an extra dimension.

# Check Dimensions
print(MATRIX.ndim)

# Check Shape
print(MATRIX.shape)
# We get the output torch.Size([2, 2]) because MATRIX is two elements deep and two elements wide.