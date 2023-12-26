lista = [4,3,2,7,8,2,3,1]
lista_2 = [1,1]

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        nums_sorted = list(set(nums))
        return list(set(range(1, len(nums) + 1)).difference(nums_sorted))
    
solucao = Solution()
print(solucao.findDisappearedNumbers(lista))