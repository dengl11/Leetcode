class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        state = [None, "", 0, 0]
        n = 0
        curr = ""
        for c in S:
            if c.isdigit():
                n = (n + len(curr)) * int(c)
                state = [state, curr, int(c), n]
                curr = ""
            else:
                curr += c
            if n >= K: break
        if curr:
            state = [state, curr, 1, n + len(curr)]
        K -= 1
        while 1:
            K = K % (state[0][-1] + len(state[1]))
            if K >= state[0][-1]:
                return state[1][K - state[0][-1]]
            state = state[0]
