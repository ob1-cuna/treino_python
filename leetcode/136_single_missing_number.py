# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity and use only constant extra space.

# Example 1:
# Input: nums = [2,2,1]
# Output: 1

# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4

# Example 3:
# Input: nums = [1]
# Output: 1

nums = [1,1,2,1,2]

class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        nums_dict = {}
        for n in nums:
            if n in nums_dict:
                nums_dict[n] = nums_dict[n] + 1
            else:
                nums_dict[n] = 1
        less = sorted(nums_dict.items(), key=lambda x:x[1])
        print(less)
        if less[1] == 1:
            return less[0]
        else:
            return None
    

solucao = Solution()
print(solucao.singleNumber(nums))