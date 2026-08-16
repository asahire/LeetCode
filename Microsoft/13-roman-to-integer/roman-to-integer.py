class Solution:
    def romanToInt(self, s: str) -> int:
        roman_hashmap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        # val = 0 
        # i = 0
        # n = len(s)

        # while i < n:
        #     if s[i] in ['I', 'X', 'C'] and i + 1 < n and s[i] + s[i+1] in roman_hashmap:
        #         val += roman_hashmap[s[i] + s[i+1]]
        #         i+= 1
        #     else:
        #         val += roman_hashmap[s[i]]

        #     i+= 1

        # return val

        # pattern here is if s[i] < s[i+1], then value -= val[s[i]] else value += val[s[i]]


        n = len(s)
        val = 0 

        for i in range(n-1):
            if roman_hashmap[s[i]] < roman_hashmap[s[i+1]]:
                val -= roman_hashmap[s[i]]
            else:
                val += roman_hashmap[s[i]]

        
        return val + roman_hashmap[s[-1]]