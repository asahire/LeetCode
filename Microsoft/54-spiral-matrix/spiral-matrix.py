class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        if not matrix or not matrix[0]:
            return []
        
        m = len(matrix)
        n = len(matrix[0])
        dirs = [(0,1),(1,0),(0, -1),(-1, 0)]   # right, down, left, top

        visited = [[False] * n for _ in range(m)]

        r,c,d = 0,0,0
        result = []

        for _ in range(m*n):
            result.append(matrix[r][c])
            # keeps track of visited elements 
            visited[r][c] = True 

            nr, nc = r + dirs[d][0], c + dirs[d][1]

            if not(0 <= nr < m and 0 <= nc <n and not visited[nr][nc]):
                d = (d + 1) % 4    # controls the direction
                nr, nc = r + dirs[d][0], c + dirs[d][1]
            
            r, c = nr, nc
        
        return result


        