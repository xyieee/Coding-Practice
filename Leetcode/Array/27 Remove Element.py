# Given an array nums and a value val, 
# remove all instances of that value in-place and return the new length.
# The order of elements can be changed.
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for num in nums[:]:
            if num == val:
                nums.remove(num)
        return len(nums)
        
# Runtime: 32 ms. Memorage Usage: 13.2 MB