import torch

# Most common datatype (and default) is torch.float32 pr torch.float
# This is referred to as a 32-bit floating point

# There's also 16-bit floating point ( torch.float16 or torch.half ) and 64-bit floating point
# ( torch.float64 or torch.double )

# Note: There are also -bit, 16-bit, 32-bit and 64-bit integers too. 
# The greater the bit value, the greater the amount of precision (and data) is able to be stored within these values. 

# Let's see how to create some tensors with specific datatypes. We can do so using the dtype parameter.

# default datatype for tensors is float32

float_32_tensor = torch.tensor([3.0, 6.0, 9.0], dtype=None, device=None, requires_grad=False)
print(float_32_tensor.shape, float_32_tensor.dtype, float_32_tensor.device)

# dtype - Defaults to None, which is torch.float32
# device - Defaults to None, which uses the default tensor type
#requires_grad - if True, operations performed on the tensor are recorded

float_16_tensor = torch.tensor([3.0, 6.0, 9.0], dtype=torch.float16)
print(float_16_tensor.dtype)