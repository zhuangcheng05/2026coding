#week04-4a.py 
#LeetCode 1732. Find the Highest Altitude
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ans = h = 0
        for gg in gain:
            h +=gg
            ans = max(ans,h)
        return ans
