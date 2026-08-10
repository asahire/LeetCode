class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # naive solution
        # max(a[0..i]) <= min(a[i+1:])

        # n = len(arr)
        # chunk = 0

        # for i in range(n):
        #     left_max = max(arr[:i+1])
        #     right_min = min(arr[i+1:]) if i + 1 < n else float('inf')

        #     if left_max <= right_min:
        #         chunk += 1
        
        # return chunk
        
        n = len(arr)
        suffix_min = [0] * n
        suffix_min[-1] = arr[-1]
  
        for i in range(n-2, -1, -1):
            suffix_min[i] = min(arr[i], suffix_min[i+1])

        chunks=0
        prefix_max = float('-inf')

        for i in range(n):
            prefix_max = max(arr[i], prefix_max)

            if i == n-1 or prefix_max <= suffix_min[i+1]:
                chunks += 1
        
        return chunks
