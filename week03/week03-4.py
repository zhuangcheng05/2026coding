#week03-4.py
#LeetCode 1004. Max Consecutive Ones III
#你可以把k個0翻轉成1,最長的那堆1,有幾個1
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros = 0
        n= len(nums)
        ans = 0
        tail = 0
        for head in range(n):
            if nums[head]==0:
                zeros += 1
                while zeros > k:
                    if nums[tail]==0:
                        zeros -= 1
                    tail += 1
            ans = max(ans,head-tail+1)
        return ans