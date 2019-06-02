class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        if len(arr1) < len(arr2): arr1, arr2 = arr2, arr1
        arr1.reverse()
        arr2.reverse()
        carry = 0
        for i in range(len(arr1)):
            # print(arr1)
            carry += arr1[i]
            if i < len(arr2):
                carry += arr2[i]
            # print(carry)
            if carry == 0: 
                arr1[i] = 0
            elif carry > 0:
                carry, curr = divmod(carry, 2)
                arr1[i] = curr
                carry *= -1
            else:
                arr1[i] = 1
                carry = 1
            # print(arr1)
        if carry:
            arr1 += [1, 1]
        # print(carry)
        while len(arr1) > 1 and arr1[-1] == 0:
            arr1.pop()
        return arr1[::-1]
                
                