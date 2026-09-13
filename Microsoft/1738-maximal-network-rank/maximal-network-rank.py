class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # naive
        # best = 0
        # for u in range(n):
        #     for v in range(u+1, n):
        #         rank = 0
        #         for a, b in roads:
        #             if a == u or a == v or b == u or b == v:
        #                 rank += 1
                
        #         best = max (best, rank)
        
        # return best

        deg = [0] * n
        connected = set()

        for a , b in roads:
            deg[a] += 1
            deg[b] += 1
            connected.add((min(a,b), max(a,b)))

        best = 0
        for u in range(n):
            for v in range(u+1, n):
                rank = deg[u] + deg[v] - ((u,v) in connected)
                best = max(best, rank)
        
        return best
