class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # naive - polynomial complexity
        # if not p:
        #     return not s
    
        # first_match = bool(s) and (p[0] == s[0] or p[0] == '.')
    
        # if len(p) >= 2 and p[1] == '*':
        #     # zero occurrences of p[0], OR one-or-more occurrences
        #     return self.isMatch(s, p[2:]) or (first_match and self.isMatch(s[1:], p))
        # else:
        #     return first_match and self.isMatch(s[1:], p[1:])
        

        m , n = len(s), len(p)

        dp = [[False] * (n+1) for _ in range(m+1)]
        
        # base case - empty string matches with empty pattern 
        dp[0][0] = True

        # base case - empty string matches with any pattern that has '*' like a*, a*b*
        for j in range(1, n+1):
            if p[j-1] == '*':
                dp[0][j] = dp[0][j-2]
                
        for i in range(1, m+1):
            for j in range(1, n+1):
                # normal character match
                if s[i-1] == p[j-1] or p[j-1] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == '*':
                        # case 1: match 0 occurance of preceding element
                        dp[i][j] = dp[i][j-2]

                        # case 2: one or more occrance (if preceding element matches)
                        if s[i-1] == p[j-2] or p[j-2] =='.':
                            dp[i][j] = dp[i][j] or dp[i-1][j]
        
        return dp[m][n]
