import torch

tensor = torch.tensor([1, 2, 3])
print(tensor.shape)

# For matrix multiplication to be possible, the inner dimensions must match..
# I.e. (3, 2) @ (3, 2) WON'T WORK
# (2, 3) @ (3, 2)

# Element Wise - [1*1, 2*2, 3*3] = [1, 4, 9]
# Matrix Multiplication - [1*1 + 2*2 + 3*3] = [14]

# Element-wise matrix multiplication
print(tensor * tensor)

# Matrix Multiplication
print(torch.matmul(tensor, tensor))