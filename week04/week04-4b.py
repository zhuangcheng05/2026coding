#week04-4b.py
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        h = [0]*200
        for nn in nums:
            h[nn]+=1
        for nn in nums:
            if nn %2 ==0 and h[nn]==1:
                return nn
        return -1