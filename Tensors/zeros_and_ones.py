import torch

# Sometimes you'll just want to fill tensors with zeros or ones.
# This happens a lot with masking (like masking some of the values in one tensor with zeros to let a model know not to learn them).

# Create a tensor of all zeros
zeros = torch.zeros(size=(3, 4))
print(zeros, zeros.dtype)

# We can do the same to create a tensor of all ones except using torch.ones() instead.

ones = torch.ones(size=(3, 4))
print(ones, ones.dtype)