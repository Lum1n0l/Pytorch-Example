import torch

# Scalar
scalar = torch.tensor(7)
print(scalar)

print(scalar.ndim)

# Get the python number from within a tensor (only works for one-element tensors)
print(scalar.item())

# Tensor = numerical representation of data. i.e [3, 224, 224] could be used to represent the colour_channels, height and width of an image. 
# Scalar = A scalar is a single number, and is a zero dimension tensor. 