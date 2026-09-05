class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        pad = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        
        # naive solution  O(n * 4^n), O(n)
        # combos = [""]

        # for d in digits:
        #     combos = [prefix + ch for prefix in combos for ch in pad[d]]
        
        # return combos

        res, path = [], []
        def backtracking(i: int):
            # base case
            if i == len(digits):
                res.append("".join(path))
                return
            
            for ch in pad[digits[i]]:
                path.append(ch)
                backtracking(i+1)
                path.pop()
        
        backtracking(0)

        return res




        
        


        