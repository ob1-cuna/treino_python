lista = [4,3,2,7,8,2,3,1]
lista_2 = [1,1]

class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        lista = []
        nums_sorted = list(set(nums))
        [lista.append(n) for n in range(1, len(nums) + 1) if n not in nums_sorted]
        return lista
    
solucao = Solution()
print(solucao.findDisappearedNumbers(lista))