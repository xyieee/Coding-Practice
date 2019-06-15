# Students are asked to stand in non-decreasing
# order of heights for an annual photo.
# Return the minimum number of students not standing 
# in the right positions. 
class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        height_copy = sorted(heights)
        count = 0 
        for i in range(len(heights)):
            if height_copy[i] != heights[i]:
                count += 1
        return count
# Runtime: 32 ms. Memory: 13.1 MB