# 0. Template

## Approach #1: Brute Force With Sets

### Algorithm

We want to add a new value into a unique set that won't be duplcate. We could create a set of all the entries in nums then iterate through all possible values for the number of bits and add in the first value that meets the criteria.

#### Complexity Analysis

Time: $O(2^n)$

Why this time complexity?

If we have length n bits. 

Space: $O(n)$

Why this space complexity?

We store n values.

## Approach #2: Prefix Tree

### Intuition

We want to minimize the number of checks we make to see if we can add an item to the set. If we visualize the items we have as a tree, we can avoid going down paths with all the options already taken if we've marked that path as being dead. When adding items, we can check to see if we've created a dead path afterwards

### Algorithm

Using a prefix tree with the number of levels as as length n. 

#### Complexity Analysis

Time: $O(n)$

Why this time complexity?

Space: $O(m)$

Why this space complexity?

## Test Cases

Any edge cases to consider? Any unknown or tricky behaviour?

## Personal Comments and Mistakes

Use this to keep track of work process and anything that could have better while solving.