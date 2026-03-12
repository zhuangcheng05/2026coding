#week03-2.py
#LeetCode 1456. Maximum Number of Vowels in a Substring of Given Length
#母音 vowels:a,e,i,o,u
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')#把五個數字變成set()
        count = 0 
        for i in range(k):
            if s[i] in vowels:count += 1
        ans = count
        n=len(s)
        for i in range(k,n):
            if s[i]in vowels: count += 1
            if s[i-k]in vowels: count -= 1
            ans = max(ans,count)
        return ans