class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        passed = 0

        for i, ch in enumerate(number):
            if ch == digit:
                passed = i
                if i+1 < len(number) and number[i+1] > number[i]:
                    return number[:i] + number[i+1:]
                

        return number[:passed] + number[passed+1:]    
        