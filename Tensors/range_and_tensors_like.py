import torch

# Sometimes you might want a range of numbers, such as 1 to 10 or 0 to 100.
# You can use torch.arange(start, end, step) to do so.
# Where:
#
#    start = start of range (e.g. 0)
#    end = end of range (e.g. 10)
#    step = how many steps in between each value (e.g. 1)

zero_to_ten = torch.arange(start=0, end=10, step=1)
print(zero_to_ten)


# Sometimes you might want one tensor of a certain type with the same shape as another tensor.
# For example, a tensor of all zeros with the same shape as a previous tensor.

# Can also create a tensor of zeros similar to another tensor
ten_zeros = torch.zeros_like(input=zero_to_ten) # Will have the same shape
print(ten_zeros)