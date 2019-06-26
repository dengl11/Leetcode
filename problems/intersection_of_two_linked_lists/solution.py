class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        
#         if headA==headB:
#             return headA
        
        def get_len(node):
            l = 0
            while node: 
                node =node.next
                l +=1
            return l
        
        def k_th(head, k):
            for _ in range(k):
                head = head.next
            return head
        
        def tail(head):
            while head.next:
                head = head.next
            return head
        
        tailB = tail(headB)
        
        l1,l2 = get_len(headA), get_len(headB)
        def reverse(head):
            pre, cur = None, head
            while cur:
                t =  cur.next
                cur.next, cur, pre = pre, t, cur
            return pre
        
        tailA=reverse(headA)
        l22=get_len(headB)
        headA = reverse(tailA)
        
        if tailB != tailA:
            return None
        tail  = (l2+l1 -l22+1)//2
        # print(l1,l2,l22,tail)
        
        return  k_th(headA, l1-tail)