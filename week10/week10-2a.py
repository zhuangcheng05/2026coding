#week10-2a.py
class Solution:
    def maxDepth(self, root):
        # 如果是空樹，深度是 0
        if root is None:
            return 0
        # 遞迴算左邊的深度
        left = self.maxDepth(root.left)
        # 遞迴算右邊的深度
        right = self.maxDepth(root.right)
        # 回傳較大的 + 1（自己這層）
        return max(left, right) + 1