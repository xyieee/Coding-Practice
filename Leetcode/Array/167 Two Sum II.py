# An array is given in ascending order, find two numbers such that 
# they add up to a target number.
# index1 and index2 are not zero-based.
# exactly one solution.
# index 1 must less than index 2.
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        twosum = {}
        for i, num in enumerate(numbers):
            if target - num in twosum:
                return [twosum[target - num], i+1]
            twosum[num] = i+1
# Runtime: 36 ms. Memory: 13.7 MB