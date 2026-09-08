class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        total = 0
        n = len(colors)
        max_prev = neededTime[0]
        for i in range(1, n):
            if colors[i] == colors[i-1]:
                total += min (max_prev, neededTime[i])
                max_prev = max(max_prev, neededTime[i])
            else:
                max_prev = neededTime[i]

        return total

        