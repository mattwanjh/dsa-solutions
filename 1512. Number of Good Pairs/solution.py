from collections import defaultdict
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        num_map = defaultdict(int)
        ans = 0
        
        for num in nums:
            ans += num_map[num]
            num_map[num] += 1

        return ans
