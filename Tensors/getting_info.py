import torch

# Once you've created tensors (or someone else or a PyTorch module has created them for you), you might want to get some information from them.
# We've seen these before but three of the most common attributes you'll want to find out about tensors are:
#    shape - what shape is the tensor? (some operations require specific shape rules)
#    dtype - what datatype are the elements within the tensor stored in?
#    device - what device is the tensor stored on? (usually GPU or CPU)

# Create a tensor

tensor = torch.rand(3, 4)

print(tensor)
print("Shape of Tensor: " + str(tensor.shape))
print("Datatype of Tensor: " + str(tensor.dtype))
print("Device Tensor is stored on is: " + str(tensor.device))

# Note: When you run into issues in PyTorch, it's very often one to do with one of the three attributes above. So when the error messages show up, sing yourself a little song called "what, what, where":
#  "what shape are my tensors? what datatype are they and where are they stored? what shape, what datatype, where where where"