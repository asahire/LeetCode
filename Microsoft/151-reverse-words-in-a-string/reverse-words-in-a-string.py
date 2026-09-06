class Solution:
    def reverseWords(self, s: str) -> str:
        i, n = 0, len(s)
        words = []
        while i < n:
            while i < n and s[i] == " ":
                i += 1
            
            if i == n:
                break

            start = i
            while i < n and s[i] != " ":
                i += 1
            
            words.append(s[start:i])
              
        return " ".join(reversed(words))
        