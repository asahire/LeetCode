class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:

        pq = []

        for char_count, char in [(-a,'a'), (-b, 'b'), (-c,'c')]:
            if char_count < 0:
                heapq.heappush(pq, (char_count, char))
        
        print(pq)
    
        result = []
        while pq:
            first_count, first_char = heapq.heappop(pq)
            if len(result) >= 2 and result[-1] == result[-2] == first_char:
                if not pq:
                    break  # No other option

                second_count, second_char = heapq.heappop(pq)
                result.append(second_char)
                second_count += 1

                if second_count < 0:
                    heapq.heappush(pq, (second_count, second_char))
                
                heapq.heappush(pq, (first_count, first_char))
            else:
                result.append(first_char)

                first_count += 1
                if first_count < 0:
                    heapq.heappush(pq, (first_count, first_char))
        

        return ''.join(result)




        