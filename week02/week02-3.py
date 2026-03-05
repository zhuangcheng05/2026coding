#week02-3.py
#LeetCode 392. Is Subsequence
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n1, n2 =len(s),len(t) #字串長度
        if n1==0: return True #左邊字串是空的不用比了
        i = 0 #i從零開始
        for k in range(n2):#右邊一個個去試
            if s[i] == t[k]:
                i+=1#左邊的i往右邊升一級
        if i == n1:#
            return True
        else:
            return False