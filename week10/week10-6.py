# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#week10-6.py
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def helper(root):
            # 回傳 (往左走的最長ZigZag, 往右走的最長ZigZag)
            if root is None:
                return 0, 0
            
            # 遞迴左右子樹
            Lleft, Lright = helper(root.left)
            Rleft, Rright = helper(root.right)
            
            # 如果現在往左走 → 下一步一定要往右（從左子樹的右開始）
            left = Lright + 1
            
            # 如果現在往右走 → 下一步一定要往左（從右子樹的左開始）
            right = Rleft + 1
            
            # 更新答案
            self.ans = max(self.ans, left, right)
            
            return left, right
        
        helper(root)
        return self.ans -1