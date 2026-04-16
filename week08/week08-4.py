#week08-4.py
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        p = len(potions)
        ans=[]
        for spell in spells:
            now = p - bisect_left(potions,success/spell)
            ans.append(now)
        return ans
        