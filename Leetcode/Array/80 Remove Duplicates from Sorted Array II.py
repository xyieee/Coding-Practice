# Given a sorted array nums, remove the duplicates in-place such that
# duplicates appeared at most twice and return the new length.
# You must do this by modifying the intput array in-place with O(1) extra memory.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for n in nums:
            if i < 2 or n != nums[i-2]:
                nums[i] = n
                i += 1  
        return i
# Runtime: 48 ms. Memory: 13.3.MB