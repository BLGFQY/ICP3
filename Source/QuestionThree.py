import numpy as np
from numpy import sort


def three():
    nums = np.random.randint(1, 20, 20)
    print("nums =\n", nums, "\n")
    nums = np.reshape(nums, (4, 5))
    print("nums =\n", nums, "\n")
    maxVal = np.max(nums, 1)
    print("max = ", maxVal, "\n")

    nums[np.arange(len(nums)), nums.argmax(1)] = 0
    print("nums =\n", nums, "\n")
