class Solution:
    def nextGreaterElement(self, n: int) -> int:

        digits = list(str(n))
        d = len(digits)

        i = d-2
        # step 1 find pivot at i where i's rightmost is less than pivot
        while i >= 0 and digits[i] >= digits[i+1]:
            i -=1
        
        if i < 0:
            return -1
        
        # step 2: find jth element which is grater than pivot
        j = d-1

        while digits[j] <= digits[i]:
            j -=1
        
        temp = digits[i]
        digits[i] = digits[j]
        digits[j] = temp

        # step 3: reverse i's rightmost element to mimimize the number

        digits[i+1:] = reversed(digits[i+1:])

        result = int("".join(digits))

        return result if result <= 2**31 -1 else -1


