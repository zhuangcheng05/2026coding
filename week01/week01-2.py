#week01-2.py 學習計劃 Array/String 第一題
#LeetCode 1768. Merge Strings Alternately
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans = "" #答案在ans
        N1 , N2 = len(word1),len(word2)
        i , j = 0,0
        while i<N1 or j<N2:
            if i<N1: ans += word1[i]
            if j<N2: ans += word2[j]
            i , j = i+1 , j+1
        return ans #答案在這裡