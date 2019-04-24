from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        width = {} #{level: [left, right]}
        ans = 0
        stack = [(root, 0, 0)] # [(node, x, y)]
        while stack:
            node, x, y = stack.pop()
            if y not in width: width[y] = [x,x]		
            width[y][0] = min(width[y][0], x)
            width[y][1] = max(width[y][1], x)
            ans = max(ans, width[y][1] - width[y][0])
            if node.left: stack.append((node.left, 2 * x, y + 1))
            if node.right: stack.append((node.right, 2 * x + 1, y + 1))
        return ans + 1
                    
                    
            
