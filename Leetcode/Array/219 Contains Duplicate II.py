# Given an array of integers and an integer k
# Find out whether there are two distinct indices i and j in the array
# such that nums[i] = nums[j] and absolute difference between i and j is 
# at most k.
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = dict()
        for i, num in enumerate(nums):
            if num in d:
                if i - d[num] <= k:
                    return True
            d[num] = i
        return False
# Runtime: 44 ms. Memory: 20.4 MB