import torch

# Tensor

TENSOR = torch.tensor([[[1, 2, 3],[3, 6, 9], [2, 4, 5]]])
print(TENSOR)

# I want to stress that tensors can represent almost anything.
# The one we just created could be the sales numbers for a steak and almond butter store (two of my favourite foods).

# How many dimensions?
print("TENSOR has " + str(TENSOR.ndim) + " dimensions!")

# Shape?
print(TENSOR.shape)