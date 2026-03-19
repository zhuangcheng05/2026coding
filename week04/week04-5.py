#week04-5.py
#LeetCode 724. Find Pivot Index
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [0]
        for i in range(n):
            prefix.append(prefix[-1]+nums[i])
        postfix = [0]*(n+1)
        for i in range(n-1,-1,-1):
            postfix[i]=postfix[i+1]+nums[i]
        for i in range(n):
            if prefix[i]==postfix[i+1]:return i
        return -1