# week13-4.py 學習計畫 Heap / Priority Queue 第2題
# LeetCode 2336. Smallest Number in Infinite Set 找到最小的數
class SmallestInfiniteSet:

    def __init__(self): # 建構子 會準備好「資料結構」
        self.now = 1 # 在資料結構之外，有個會慢慢增加的數
        self.heap = [] # 資料結構，會吐出最小的數

    def popSmallest(self) -> int: # 吐出最小的數
        if self.heap: # 如果資料結構裡「有裝1個比較小的數」
            return heappop(self.heap) # 就吐出來
        self.now += 1 # 不然，就慢慢往上增加
        return self.now - 1

    def addBack(self, num: int) -> None:
        #print('zzz')
        if num < self.now: # 另外處理「比較小的數」
            # 為了避免重複加入相同的數字，進階實作可以加上「if num not in self.heap」的判斷
            if num not in self.heap:
                heappush(self.heap, num)

# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)