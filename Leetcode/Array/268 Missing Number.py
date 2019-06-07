# Given an array containing n distinct numbers taken from 0, 1, ... , n.
# Find the one that is missing from the array.
# Algorithm should run in linear runtime complexity. 
# Using only constant extra space complexity.

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seq = len(nums) * (len(nums)+1)/2
        return int(seq - sum(nums))

# Runtime: 28 ms. Memory: 13.9 MB.
