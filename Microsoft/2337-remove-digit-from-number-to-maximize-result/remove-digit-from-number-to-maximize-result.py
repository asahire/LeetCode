class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        last = -1

        for i, ch in enumerate(number):
            if ch == digit:
                last = i
                if i+1 < len(number) and number[i+1] > number[i]:
                    return number[:i] + number[i+1:]
                

        return number[:last] + number[last+1:]    
        