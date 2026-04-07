

# TLE APPROACH
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        def helper(s, d, start, curr):
            if curr == len(s):
                return True
                
            while curr <= len(s):
                # split
                if s[start:curr] in d:
                    if helper(s, d, curr, curr) == True: 
                        return True
                curr += 1
            return False

        d = set(wordDict)
        return helper(s, d, 0, 0)

"""
Recursive approach. TLE
We iterate through the input string, checking against the dictionary entries.
As soon as the string we're iterating through has a dictionary entry we split.
1. We choose to use that entry
2. We don't choose to ues that entry.

two pointers: 
start, end 

if we take, change the start, if not keep it the same. 
"""

# BELOW IS WRONG: I INTERPRETED THE QUESTION AS NEEDING TO ONLY HAVE A SINGLE UNIQUE SEQUENCE.
# YOU ARE ALLOWED TO HAVE OVERLAPPING DICTIONARY ENTRIES. THEY MUST BE SEPERATABLE.
class Solution:
    def findLps(self, word) -> List[int]:
        lps = [0]*len(word)
        l, r = 0, 1

        while r < len(word):
            if word[l] == word[r]:
                lps[r] = lps[r-1] + 1
                l += 1 
                r += 1
            elif l == 0:
                r += 1
            else: 
                l = lps[l - 1]
        return lps

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        seen = [False]*len(s)
        
        for word in wordDict:
            lps = self.findLps(word)
            l, r = 0, 0
            while l <= len(s):
                # print("R:", r , "L:", l)
                if r >= len(word):
                    start = l - r
                    print(word)
                    print(start)

                    for i in range(start, start + len(word)):
                        print(i)
                        if seen[i]:
                            # print(seen)
                            # print(word)
                            # print("R:", r , "L:", l, "I:", i, "START:", start)
                            return False
                        seen[i] = True
                    # print(seen)
                    # print(word)
                    # print("R:", r , "L:", l, "START:", start)
                    r = lps[r - 1]

                elif l < len(s) and s[l] == word[r]:
                    print(word)
                    print("R:", r , "L:", l)
                    l += 1
                    r += 1
                elif r == 0:
                    l += 1
                else:
                    r = lps[r-1]
        
        return seen.count(True) == len(seen)
"""
Brute:
Each word walk through all indexes and check to see if it matches.
Mark each word

Slightly better: 
Use LPS
For each word, if found in the input mark those indices as being visited.
If one of the indices has already been visited, return false. else true.

abc
0, 0, 0

aba
0, 0, 1
l = 0, r = 1
- don't match, take previous value 

l = 0, r = 2
- match, take previous value + 1
- index = 1



ababc
0, 0, 1, 2, 0
l = 0, r = 2
- match, take previous value + 1

l = 1, r = 3
- match, take previous value + 1

l = 2, r = 4
- don't match, take left - 1 value 


aaac
 aac
 r = 3 
 len(word) == 3
 l = 4
 l - r = start
for 3 the next 3 values
"""