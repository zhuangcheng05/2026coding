#week01-4.py 學習計劃 
#LeetCode 1431. Kids With the Greatest Number of Candies
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        ans = []
        best = max(candies)
        for candie in candies: #逐一檢查、如果把extraCandies給小朋友
            if candie + extraCandies >= best: ans.append(True)
            else: ans.append(False) #他會不會>=最多的
        return ans