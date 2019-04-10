# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def allPossibleFBT(self, N: int) -> List[TreeNode]:
        nodes = [[] for _ in range(N + 1)]
        nodes[1].append(TreeNode(0))
        for i in range(3, N + 1, 2):
            for j in range(1, i, 2):
                for l in nodes[j]:
                    for r in nodes[i - 1 -j]:
                        root = TreeNode(0)
                        root.left = l
                        root.right = r
                        nodes[i].append(root)
        return nodes[-1]
                        
                
            
            
        