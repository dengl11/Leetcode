from collections import deque
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        
        stack = []
        popped = deque(popped)
        for x in pushed:
            stack.append(x)
            while popped and stack and popped[0] == stack[-1]:
                popped.popleft()
                stack.pop()
        if stack:
            return stack[::-1] == list(popped)
        return not popped
            