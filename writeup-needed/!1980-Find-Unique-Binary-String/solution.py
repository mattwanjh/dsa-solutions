class Solution:
    class Node:
        def __init__(self, value, filled=False, left=None, right=None):
            self.value = value
            self.filled = False
            # 0 is next value
            self.left = left
            # 1 is next value
            self.right = right

        
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # root of the prefix node
        prefix = self.Node("")
        levels = len(nums[0])

        def insertTree(prefix, num) -> None: 
            stack = []
            
            for i in range(len(num)):
                if num[i] == "0":
                    if prefix.left is None:
                        prefix.left = self.Node("0")
                    prefix = prefix.left
                else:
                    if prefix.right is None:
                        prefix.right = self.Node("1")
                    stack.append(prefix)
                    prefix = prefix.right
                stack.append(prefix)
            
            # leaf nodes are not visited 
            stack[-1].filled = True
            
            # check if the child nodes are filled
            stack.pop()

            while stack:
                curr = stack.pop()
                if curr.left is not None and curr.right is not None:
                    curr.filled = True
                else: 
                    return
        
        # builds the prefix tree
        def buildTree(prefix, nums) -> None:
            for num in nums: 
                insertTree(prefix, num)
            

        # returns the first string that is available
        def findNode(prefix, levels) -> str:
            ans = []
            for i in range(levels):
                if not prefix.left:
                    prefix.left = self.Node("0")
                if not prefix.right:
                    prefix.right = self.Node("1")
                
                if prefix.left.filled is True:
                    ans.append("1")
                    prefix = prefix.right
                else:
                    ans.append("0")
                    prefix = prefix.left
                
            return ''.join(ans)

        buildTree(prefix, nums)
        return findNode(prefix, levels)