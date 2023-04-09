import torch

# A vector is a single dimension tensor, but it can contain many numbers. 

# As in, you could have a vector [3, 2] to describe [bedrooms, bathrooms] in your house. Or you could have [3, 2, 2] to describe [bedrooms, bathrooms, car_parks] in your house.
# The important trend here is that a vector is flexible in what it can represent (the same with tensors).

vector = torch.tensor([7, 7])
print(vector)

# Verify how many dimensions is in 'vector'
print(vector.ndim)

# You can tell the number of dimensions a tensor in PyTorch has by the number of square brackets on the outside ([) and you only need to count one side.

# Another important concept for tensors is their shape attribute. The shape tells you how the elements inside them are arranged
# Check shape of vector
print(vector.shape)
# The above returns torch.Size([2]) which means our vector has a shape of [2]. This is because of the two elements we placed inside the square brackets ([7, 7]).