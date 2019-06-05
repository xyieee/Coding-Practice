# Given a 32-bit integer, reverse digits of an integer
# Integers could only be stored within the 32-bit signed integer range:
# [-2^31, 2^31 -1]. Function returns 0 when the reversed integer overflows.

class Solution:
    def reverse(self, x: int) -> int:
        x = int(str(x)[::-1]) if x >= 0 else -int(str(-x)[::-1])
        return x if x > (2**31 -1) and x <= (-2**31) else 0
    
x= 1534236469
sol = Solution()
print(sol.reverse(x))

# Runtime: 36 ms. Memory Usage: 13.2 MB