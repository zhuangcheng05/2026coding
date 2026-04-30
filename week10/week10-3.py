# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#week10-3.py
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, max_val):
            # 如果節點不存在
            if not node:
                return 0
            
            # 判斷是不是 good node
            count = 0
            if node.val >= max_val:
                count = 1  # 是 good node
            
            # 更新目前最大值
            max_val = max(max_val, node.val)
            
            # 繼續往左右走
            count += dfs(node.left, max_val)
            count += dfs(node.right, max_val)
            
            return count
        
        # 初始 max 是 root 的值
        return dfs(root, root.val)