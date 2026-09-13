class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # naive
        best = 0
        for u in range(n):
            for v in range(u+1, n):
                rank = 0
                for a, b in roads:
                    if a == u or a == v or b == u or b == v:
                        rank += 1
                
                best = max (best, rank)
        
        return best
        