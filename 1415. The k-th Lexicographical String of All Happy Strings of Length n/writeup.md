```python
"""
t = total options
k = index we want
b = numerical boundaries
o = options
"""


"""
Brute:
Create all possible strings, add them to a list, sort, then index

Optimized


Pattern:
n = 1
a, b, c

n = 2

ab, ac, ba, bc, ca, cb

                ""
        a       b       c
    b       c  a c  a       b


The size of each subpath is 2, you have total 6 choices. 3 * 2

n = 3

["aba", "abc", "aca", "acb", "bab", "bac", "bca", "bcb", "cab", "cac", "cba", "cbc"]

                                            ""
                    a
            b               c
        a       c        a      b
        1       2        3      4
3 * 2 * 2
12 

t = total options
k = index we want
b = numerical boundaries
o = options

Layer 1: 
total options = to - 1
k = k - 1
k = 8
Numerical boundary:
layer 1: total options / choices = 12 / 3 = 4 = b = next total options
k / b = 8 / 4 = 2
k / b = choose c
a = 0, b = 1 c = 2

a(0,1,2,3), b(4,5,6,7), c(8,9,10,11)
choose c
---

k = k - 1
k = 3
layer 2: total options / choices = 4 / 2 = 2
a(0, 1) b(2, 3) 
choose a 

SELECT a
UNSURE
layer 3:  
b(0) c(1)

"""
```

# 0. Template

## Approach #1: Brute Force

### Intuition

What considerations or key parts of the question should we take into account?

### Algorithm

How can this approach be implemented?

#### Complexity Analysis

Time: $O(n^2)$

Why this time complexity?

Space: $O(n*m)$

Why this space complexity?

## Approach #2: Optimized

### Intuition

What considerations or key parts of the question should we take into account?

### Algorithm

How can this approach be implemented?

#### Complexity Analysis

Time: $O(n)$

Why this time complexity?

Space: $O(m)$

Why this space complexity?

## Test Cases

Any edge cases to consider? Any unknown or tricky behaviour?

## Personal Comments and Mistakes

Use this to keep track of work process and anything that could have better while solving.