#week03-2.py
#LeetCode 643. Maximum Average Subarray I
#sliding window毛毛蟲解法 右邊吃左邊吐保持長度k
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        total = sum(nums[:k])
        maxTotal = total
        for i in range(k,n):
            total = total + nums[i] - nums[i-k]
            maxTotal = max(maxTotal,total)
        return maxTotal/k