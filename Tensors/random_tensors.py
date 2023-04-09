import torch

# Create a random tensor of size (3, 4)
random_tensor = torch.rand(size=(3, 4))
print(random_tensor, random_tensor.dtype)

# The flexibility of torch.rand() is that we can adjust the size to be whatever we want.
# For example, say you wanted a random tensor in the common image shape of [224, 224, 3] ([height, width, color_channels]).

# Create a random tensor in the size of a common image... 

random_image_size_tensor = torch.rand(size=(224, 224, 3))
print(random_image_size_tensor.shape, random_image_size_tensor.ndim)