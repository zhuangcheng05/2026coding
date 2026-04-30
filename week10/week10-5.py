from collections import Counter

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#week10-5.py
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        counter = Counter()
        counter[0] = 1  # base case
        
        def helper(node, total):
            if not node:
                return 0
            
            # 1. 更新 prefix sum
            total += node.val
            
            # 2. 看有沒有符合 target
            ans = counter[total - targetSum]
            
            # 3. 加入當前 prefix sum
            counter[total] += 1
            
            # 4. 遞迴左右子樹
            ans += helper(node.left, total)
            ans += helper(node.right, total)
            
            # 5. 回溯（超重要！）
            counter[total] -= 1
            
            return ans
        
        return helper(root, 0)