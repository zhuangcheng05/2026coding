#week04-3.py
#LeetCode 3866. First Unique Even Element

class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        n = len(nums)
        h = [0]*200
        for i in range(n):
            h[nums[i]]+=1
        for i in range(n):
            if nums[i]%2==0 and h[nums[i]]==1:
                return nums[i]
        return -1