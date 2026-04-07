class Solution:
    # runtime = O(n * n)
    # space   = O(n)
    def countPrimes(self, n: int) -> int:
        isPrime = [True] * (n)
        primes = set()
        
        if n < 2:
            return 0

        for i in range(2, n):
            if isPrime[i]:
                for x in range(i + i, n, i):
                    isPrime[x] = False
            
        return isPrime.count(True) - 2

"""
Brute:
For each number, try to mod it by all other numbers less than it.

Slightly optimized:
For each number, try to mod it by all primes less than it (existing primes list)

Slightly more optimized:
For each prime, set each multiple of prime > prime to false until n.
This is slightly better than above since we don't have to run the current number against the growing list of primes. We preemptively set it. 

Most optimial: 
Change the inner for loop to start at i * i. 
The reason being is that all factors up until i have already been calculated, so i * j where j < i is repeated work. 
By starting at factors greater than i, we're able to reduce repeated i work for each iteration.

Inner loop: for x in range(i * i, n, i):

https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes

Time complexity is actually O(n*log(log(n))))
"""