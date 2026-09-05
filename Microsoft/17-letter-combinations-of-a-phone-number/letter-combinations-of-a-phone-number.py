class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        pad = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
 
        combos = [""]

        for d in digits:
            combos = [prefix + ch for prefix in combos for ch in pad[d]]
        
        return combos


        