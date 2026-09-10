class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        # if not matrix or not matrix[0]:
        #     return []
        
        # m = len(matrix)
        # n = len(matrix[0])
        # dirs = [(0,1),(1,0),(0, -1),(-1, 0)]   # right, down, left, top

        # visited = [[False] * n for _ in range(m)]

        # r,c,d = 0,0,0
        # result = []

        # for _ in range(m*n):
        #     result.append(matrix[r][c])
        #     # keeps track of visited elements 
        #     visited[r][c] = True 

        #     nr, nc = r + dirs[d][0], c + dirs[d][1]

        #     if not(0 <= nr < m and 0 <= nc <n and not visited[nr][nc]):
        #         d = (d + 1) % 4    # controls the direction
        #         nr, nc = r + dirs[d][0], c + dirs[d][1]
            
        #     r, c = nr, nc
        
        # return result # TC = Theta(m*n), SC = Theta(m*n) as one iteration per cell, constant work each.
        if not matrix or not matrix[0]:
            return []
        
        top, bottom = 0, len(matrix) -1
        left, right = 0, len(matrix[0]) - 1
        result = []
        while top <= bottom and left <=right:
            for c in range(left, right+1):
                result.append(matrix[top][c])
            top+=1
            
            for r in range(top, bottom+1):
                result.append(matrix[r][right])
            right -= 1

            if top <= bottom:
                for c in range(right, left-1, -1):
                    result.append(matrix[bottom][c])
                bottom -= 1
            
            if left <= right:
                for r in range(bottom, top-1, -1):
                    result.append(matrix[r][left])
                
                left += 1
        
        return result




        