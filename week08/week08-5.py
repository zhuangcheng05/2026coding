# week08-5.py 學習單五 Binary Search 第3題
# LeetCode 162. Find Peak Element 找到 比左右都大的 峰頂

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        # 笨方法：for迴圈找 (因為資料量限制，這題其實不會TLE)
        N = len(nums)  # 陣列大小 N

        if N == 1:
            return 0  # i=0 最大 (只有1個數，直接回傳)

        for i in range(N):  # 每個 index i 都去判斷 左邊右邊

            if i == 0:  # 沒有左邊，只看右邊 (若比右邊大)
                if nums[i] > nums[i+1]:
                    return i

            elif i == N-1:  # 沒有右邊，只看左邊 (若比左邊大)
                if nums[i] > nums[i-1]:
                    return i

            # 中間情況：左右都存在
            elif nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i

# 這題其實標準解是 Binary Search
# 但題目有註明，用暴力 for 迴圈也可以