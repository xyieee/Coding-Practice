# Give an array, rotate the array to the right by k steps. k is non-negative
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % len(nums)
        nums[:] = nums[n-k:] + nums[:n-k]

# Runtime: 52 ms, memory: 13.7 MB