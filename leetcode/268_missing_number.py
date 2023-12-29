lista = [9,6,4,2,3,5,7,0,1]

class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        numbers_dict = dict(zip(nums, range(len(nums))))
        for i in range(len(nums)+1):
            if i not in numbers_dict.keys():
                return i
        

solucao = Solution()
print(solucao.missingNumber(lista))
            