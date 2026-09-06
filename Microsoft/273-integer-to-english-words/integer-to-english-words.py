class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        BELOW_20 = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven",
                    "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen",
                    "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen",
                    "Nineteen"]
        TENS = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty",
                "Seventy", "Eighty", "Ninety"]
        SCALES = ["", "Thousand", "Million", "Billion"]
        group = []
        scale = 0

        def three(n: int):
            if n == 0:
                return []
            if n < 20:
                return [BELOW_20[n]]
            
            if n < 100:
                return [TENS[n//10]] + three(n % 10)
            
            return [BELOW_20[n//100], "Hundred"] + three(n%100)

        while num:
            num, rem = divmod(num, 1000)

            if rem:
                group.append( three(rem) + ([SCALES[scale]] if scale else []))
                print(group)
            
            scale+=1
        
        output = []

        print(group)
        # reversed the output
        for g in reversed(group):
            output.extend(g)
        
        return " ".join(output)

        


        