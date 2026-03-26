#week05-4.py
#3546. Equal Sum Grid Partition I
class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        total = sum([sum(row)for row in grid])

        preSum = 0 
        for row in grid:
            preSum += sum(row)
            if preSum == total - preSum:
                return True
        
        preSum = 0
        for col in zip(*grid):#把transpose轉至矩陣逐個處理
            preSum += sum(col)
            if preSum == total - preSum:
                return True
        return False