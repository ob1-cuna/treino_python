lista = [9,6,4,2,3,5,7,0,1]

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        nums_sorted = sorted(nums)
        for n in range(len(nums)+1):
                if n not in nums_sorted:
                    return n

solucao = Solution()
print(solucao.missingNumber(lista))
            