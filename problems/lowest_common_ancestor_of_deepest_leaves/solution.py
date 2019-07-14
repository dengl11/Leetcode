class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        def depth(node):
            if not node: return 0
            return max(depth(node.left), depth(node.right)) + 1
        
        D = depth(root)
        self.todo = 0
        
        stack = [(root, 1)]
        while stack:
            node, d = stack.pop()
            if d == D: self.todo += 1
            if node.left: stack.append((node.left, d + 1))
            if node.right: stack.append((node.right, d+ 1))
        T = self.todo     
        def check(node, d = 1):
            if not node: return 0, None

            left = check(node.left, d + 1)
            if left[1]: return 0, left[1]
            right = check(node.right, d + 1)
            if right[1]: return 0, right[1]
            done = left[0] + right[0]
            if d == D: 
                done += 1
            if done == T:
                return 0, node
            return done, None
        
        return check(root)[1]
            
            
        
        