class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key= lambda iv: iv[0])

        merged = [intervals[0]]

        for start, end in intervals[1:]:
            last = merged[-1]

            if start <= last[1]:
                last[1] = max(end, last[1])
            else:
                merged.append([start, end])
        
        return merged
