import torch

# In deep learning, data (images, text, video, audio, protein structures, etc) gets represented as tensors.
# A model learns by investigating those tensors and performing a series of operations (could be 1,000,000s+) on tensors to create a representation of the patterns in the input data.
# These operations are often a wonderful dance between:
#
#    Addition
#    Substraction
#    Multiplication (element-wise)
#    Division
#    Matrix multiplication

# And that's it. Sure there are a few more here and there but these are the basic building blocks of neural networks.
# Stacking these building blocks in the right way, you can create the most sophisticated of neural networks (just like lego!).

# Create a tensor of values and add a number to it
tensor = torch.tensor([1, 2, 3])
print(tensor + 10)

# Multyply it by 10
print(tensor * 10)

# The original tensor values don't change unless reassigned
print(tensor)

# Subtract and Reassign
tensor = tensor - 10
print(tensor)

# Add and Reassign
tensor = tensor + 10
print(tensor)

# PyTorch also has a bunch of built-in functions like torch.mul() (short for multiplcation) and torch.add() to perform basic operations.
print(torch.multiply(tensor, 10))
# Original remains unchanged
print(tensor)

# Element-wise multiplication (each element multiplies its equivalent, index 0->0, 1->1, 2->2)
print(tensor, "*", tensor)
print("Equals:", tensor * tensor)