# Given an array of integers, return indices of the two numbers 
# such that they add up to a specific target.
# You may assume that each input would have exactly one solution.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twosum = {}
        for i in range(len(nums)):
            if target-nums[i] in twosum:
                return [twosum[target-nums[i]],i]
            if target-nums[i] not in twosum:
                twosum[nums[i]] = i