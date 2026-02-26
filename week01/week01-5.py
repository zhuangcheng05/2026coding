#week01-5.py
#LeetCode 238. Product of Array Except Self
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)#陣列長度
        preSum =[1]#左邊累積成起來的直
        postSum =[1]
        for i in range(N):
            preSum.append(preSum[-1]*nums[i])#每次多成一個數
            #print(preSum)#看一下乘出來的過程
            postSum.append(postSum[-1]*nums[N-1-i])
        ans = []
        for i in range(N):
            ans.append(preSum[i]*postSum[N-1-i])
        return ans