# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".


# Example 1:
# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        sorted_strs = sorted(strs)
        if len(sorted_strs[0]) > len(sorted_strs[-1]):
            a, b = sorted_strs[-1], sorted_strs[0]
        else:
            a, b = sorted_strs[0], sorted_strs[-1]

        prefixo_comum = ""

        for index, i in enumerate(a):
            if b[index] == i:
                prefixo_comum+=i
            else:
                break
        return prefixo_comum
