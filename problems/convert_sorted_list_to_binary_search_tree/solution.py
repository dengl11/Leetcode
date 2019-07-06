# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        arr = []
        while head:
            arr.append(head.val)
            head = head.next
            
        def construct(i, j):
            if i > j: return None
            mid = (i + j + 1) // 2
            root = TreeNode(arr[mid])
            root.left = construct(i, mid - 1)
            root.right = construct(mid + 1, j)
            return root
        
        return construct(0, len(arr) - 1)
