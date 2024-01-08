class Solution:
    def climbStairs(self, n: int) -> int:
        a, b = 0, 1
        for i in range(1, n+1):
            c = a + b
            a = b
            b = c
        return b

solucao = Solution()
print(solucao.climbStairs(5))
# for solucao.climbStairs(5) the output will be 8, meaning you can climb 5 stairs using 8 variations.