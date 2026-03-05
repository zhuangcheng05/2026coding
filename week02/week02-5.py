#week02-5.py
#LeetCode 1679. Max Number of K-Sum Pairs
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()#小到大排好，左挑一個右挑一個
        i , j = 0 , len(nums)-1
        ans=0
        while i<j:#左右還沒有撞在一起
            if nums[i] + nums[j]==k:
                ans += 1
                i,j = i+1,j-1
            if nums[i] + nums[j] < k:
                i = i+1
            if nums[i] + nums[j] > k:
                j = j-1
        return ans

