class Solution:
    def romanToInt(self, s: str) -> int:
        roman_hashmap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX':9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

        val = 0 
        i = 0
        n = len(s)

        while i < n:
            if s[i] in ['I', 'X', 'C'] and i + 1 < n and s[i] + s[i+1] in roman_hashmap:
                val += roman_hashmap[s[i] + s[i+1]]
                i+= 1
            else:
                val += roman_hashmap[s[i]]

            i+= 1

        return val      