# week13-3.py 學習計畫 Heap / Priority Queue 第1題
# LeetCode 215. Kth Largest Element in an Array
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapify(nums) # 把陣列轉換成最小堆積 (Min-Heap)，最小的元素會在最上面
        for i in range(len(nums) - k): # 彈出前面比較小的元素
            heappop(nums)
        return heappop(nums) # 接下來彈出的這一個，就是第 k 個最大的元素