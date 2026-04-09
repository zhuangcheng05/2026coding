#week07-6.py
#649. Dota2 Senate
from collections import deque

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        R = deque()
        D = deque()
        
        # 初始化
        for i in range(n):
            if senate[i] == 'R':
                R.append(i)
            else:
                D.append(i)
        
        # 模擬
        while R and D:
            r = R.popleft()
            d = D.popleft()
            
            if r < d:
                R.append(r + n)
            else:
                D.append(d + n)
        
        return "Radiant" if R else "Dire"