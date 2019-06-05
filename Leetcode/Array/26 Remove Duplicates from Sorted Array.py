# Given a sorted array nums, remove the duplicates in-place 
# such that each element appear only once and return the new length.
# You must do this by modifying the input array in-place with O(1) extra memory.
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        current = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[current]:
                current += 1
                nums[current] = nums[i]
        return current+1
    
# Runtime: 52 ms. Memory: 14.8MB