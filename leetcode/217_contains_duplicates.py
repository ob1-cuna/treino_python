lista = [1, 2, 4, 5, 4]

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        nums_sorted = sorted(nums)
        for n in range(len(nums_sorted) - 1):
            if [n] == nums_sorted[n+1]:
                return True
        return False
    
solucao = Solution()
print(solucao.containsDuplicate(lista))