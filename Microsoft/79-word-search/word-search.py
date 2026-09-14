class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        L = len(word)

        # Prune 1: the word can't be longer than the number of cells
        if L > m * n:
            return False

        # Prune 2: the board must contain enough of each letter
        from collections import Counter
        board_count = Counter(ch for row in board for ch in row)
        word_count = Counter(word)

        print(board_count)
        print(word_count)

        # Prune 3: search for the rarer end of the word first
        if board_count[word[0]] > board_count[word[-1]]:
            word = word[::-1]
        
        print(word)


        def dfs(r, c, i):
            if i == L:
                return True

            if r < 0 or r >= m or c < 0 or c >= n or board[r][c] != word[i]:
                return False
            
            tmp = board[r][c]
            board[r][c] = '#'
            found = (dfs(r+1, c, i+1) or dfs(r-1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1))
            board[r][c] = tmp

            return found
        
        for r in range(m):
            for c in range(n):
                if board[r][c] == word[0] and dfs(r,c,0):
                    return True
        
        return False


        