class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])

        # num_of_islands = 0

        # for r in range(rows):
        #     for c in range(cols):
        #         # if we find island
        #         if grid[r][c] == "1":
        #             num_of_islands += 1
        #             # sink the island
        #             grid[r][c] = "0"  # sink the node
        #             # start bfs exploration and sink all connected nodes
        #             directions = [[1,0], [-1,0], [0,-1],[0,1]]
        #             queue = deque([(r,c)])
 
        #             while queue:
        #                 curr_r, curr_c = queue.popleft()
        #                 for dr, dc in directions:
        #                     nr, nc = curr_r + dr, curr_c + dc
        #                     # check boundries and if its island
        #                     if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == "1":
        #                         queue.append((nr, nc))
        #                         grid[nr][nc] = "0"
        
        # return num_of_islands
        
        # DFS - 1
        # visited = [[False] * cols for _ in range(rows)]
        # num_of_islands= 0

        # def dfs(r, c):
        #     if r < 0 or r >= rows or c < 0 or c >= cols:
        #         return
        #     if grid[r][c] == '0' or visited[r][c]:
        #         return

        #     visited[r][c] = True

        #     dfs(r+1, c)
        #     dfs(r-1, c)
        #     dfs(r, c+1)
        #     dfs(r, c-1)

        # for m in range(rows):
        #     for n in range(cols):
        #         if grid[m][n] == '1' and not visited[m][n]:
        #             num_of_islands += 1
        #             dfs(m,n)
        
        # return num_of_islands

        # DFS -2 
        m, n = len(grid), len(grid[0])
        count = 0
        
        def sink(r, c):
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] != '1':
                return
            grid[r][c] = '0'                      # mark visited by turning land into water
            sink(r + 1, c)
            sink(r - 1, c)
            sink(r, c + 1)
            sink(r, c - 1)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    count += 1
                    sink(r, c)
        return count

        