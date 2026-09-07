class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        counts = {'a': a, 'b': b, 'c':c}
        res = []
        
        for _ in range(a+b+c):
            order = sorted(counts, key= lambda ch: counts[ch] , reverse=True)
            placed = False

            for ch in order:
                if counts[ch] == 0:
                    continue
                if len(res) >= 2 and res[-1] == ch and res[-2] == ch:
                    continue
                
                res.append(ch)
                counts[ch] -= 1
                placed = True
                break

            # this is needed to handle condition in which there is no separator char avail, 
            # so discard the unused char example 2
            if not placed:
                break
        
        return "".join(res)
            