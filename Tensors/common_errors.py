import torch

# Because much of deep learning is multiplying and performing operations on matrices and matrices have a strict rule about what shapes and sizes can be combined, one of the most common errors you'll run into in deep learning is shape mismatches.

# Shapes need to be in the right way  
tensor_A = torch.tensor([[1, 2],
                         [3, 4],
                         [5, 6]], dtype=torch.float32)

tensor_B = torch.tensor([[7, 10],
                         [8, 11], 
                         [9, 12]], dtype=torch.float32)

# torch.matmul(tensor_A, tensor_B) # (this will error)


# We can make matrix multiplication work between tensor_A and tensor_B by making their inner dimensions match.
# One of the ways to do this is with a transpose (switch the dimensions of a given tensor).
# You can perform transposes in PyTorch using either:
# torch.transpose(input, dim0, dim1) - where input is the desired tensor to transpose and dim0 and dim1 are the dimensions to be swapped.
# tensor.T - where tensor is the desired tensor to transpose.

# View tensor_A and tensor_B
print(tensor_A)
print(tensor_B)

# View tensor_A and tensoe_B.T
print(tensor_A)
print(tensor_B.T)

# The operation works when tensor_B is transposed
print(f"Original shapes: tensor_A = {tensor_A.shape}, tensor_B = {tensor_B.shape}\n")
print(f"New shapes: tensor_A = {tensor_A.shape} (same as above), tensor_B.T = {tensor_B.T.shape}\n")
print(f"Multiplying: {tensor_A.shape} * {tensor_B.T.shape} <- inner dimensions match\n")
print("Output:\n")
output = torch.matmul(tensor_A, tensor_B.T)
print(output) 
print(f"\nOutput shape: {output.shape}")

# You can also use torch.mm() - short for torch.matmul()

# torch.mm is a shortcut for matmul
print(torch.mm(tensor_A, tensor_B.T))