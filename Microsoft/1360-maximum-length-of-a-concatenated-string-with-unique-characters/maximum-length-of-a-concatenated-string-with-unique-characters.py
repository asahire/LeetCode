class Solution:
    def maxLength(self, arr: List[str]) -> int:
        masks = []
        for s in arr:
            mask = 0
            valid = True
            for ch in s:
       
                bit = 1 << (ord(ch) - ord('a'))
                
                if bit & mask:
                    valid = False
                    break
                mask |= bit
            
            if valid:
                masks.append(mask)
        print(masks)

        best = 0 

        def dfs(i, used):
            nonlocal best
            best = max(best, bin(used).count('1'))
    
            for j in range(i, len(masks)):
                if used & masks[j] == 0:
                    dfs(j+1, used | masks[j])
            
        dfs(0,0)

        return best
        