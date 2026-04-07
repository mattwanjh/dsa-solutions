class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        factors = []
        factors.append(n)
        
        for i in range(n // 2, 0, -1):
            if n % i == 0: 
                factors.append(i)
        if k > len(factors): 
            return -1

        return factors[-k]