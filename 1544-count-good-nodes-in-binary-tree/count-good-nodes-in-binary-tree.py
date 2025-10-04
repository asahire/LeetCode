# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_value_so_far):

            if not node:
                return 0
            
            good = 1 if node.val >= max_value_so_far else 0

            max_value_so_far = max(node.val , max_value_so_far)

            good += dfs(node.left, max_value_so_far)

            good += dfs(node.right, max_value_so_far)

            return good
        
        return dfs(root, root.val)
        