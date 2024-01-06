# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:
# Input: x = 123
# Output: 321

# Example 2:
# Input: x = -123
# Output: -321

# Example 3:
# Input: x = 120
# Output: 21
 
# Constraints:
# -2^31 <= x <= 2^31 - 1

class Solution:
    def reverse(self, x: int) -> int:
        num_reversed = 0
        if pow(-2,31) <= x <= pow(2,31) - 1:
            num_str = str(x)
            if x<0:
                num_str = '-'+ num_str[:0:-1]
                num_reversed = int(num_str)
            else:
                num_reversed = int(num_str[::-1])
        else:
            return 0
        if pow(-2,31) <= num_reversed <= pow(2,31) - 1:
            return num_reversed
        else:
            return 0