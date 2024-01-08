# Given an integer x, return true if x is a palindrome, and false otherwise.

# Example 1:
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.

# Example 2:
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 
# Constraints:
# -2^31 <= x <= 2^31 - 1


class Solution:
    def is_palidrome(self, x:int) -> bool:
        return str(x) == str(x)[::-1]
               
solucao = Solution()
print(solucao.is_palidrome(101)) # True
print(solucao.is_palidrome(10)) # False