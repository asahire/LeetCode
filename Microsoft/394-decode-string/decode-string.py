class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
    
            if char != ']':
                stack.append(char)
            else:
                substr= ""

                while stack and stack[-1] != '[':
                    substr = stack.pop() + substr

                # pop [
                stack.pop()

                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
     
                stack.append(int(k) * substr)

        return ''.join(stack) 


        