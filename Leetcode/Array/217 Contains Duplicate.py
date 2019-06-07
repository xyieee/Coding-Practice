# Given an array of integers, find if the array contains any duplicates.
# Your function should return true if any value appears at least twice 
# in the array, it should return false if every element is distinct.
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        result = set()
        for num in nums:
            if num in result: return True
            result.add(num)
        return False

# Runtime: 48 ms. Memory: 18.9 MB