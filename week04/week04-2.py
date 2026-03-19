#week04-2.py 
#LeetCode 1732. Find the Highest Altitude
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        n = len(gain)
        ans = h = 0
        for i in range(n):
            h += gain[i]
            ans = max(ans,h)
        return ans