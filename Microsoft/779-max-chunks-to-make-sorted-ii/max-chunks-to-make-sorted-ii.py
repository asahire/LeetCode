class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # naive solution
        # max(a[0..i]) <= min(a[i+1:])

        n = len(arr)
        chunk = 0
        
        for i in range(n):
            left_max = max(arr[:i+1])
            right_min = min(arr[i+1:]) if i + 1 < n else float('inf')

            if left_max <= right_min:
                chunk += 1
        
        return chunk
        