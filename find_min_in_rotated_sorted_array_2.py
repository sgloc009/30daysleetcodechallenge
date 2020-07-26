#July_25th 2020 Leetcode challenge
class Solution:
    def findMin(self, nums: List[int]) -> int:
        min = 0
        return(self.recursiveBS(nums))
        
    def recursiveBS(self, nums):
        if(len(nums)==1):
            return(nums[0])
        pivot = len(nums)//2
        lhs = self.recursiveBS(nums[:pivot])
        rhs = self.recursiveBS(nums[pivot:])
        if(lhs>nums[pivot] and nums[pivot]<rhs):
            return nums[pivot]
        elif(lhs>rhs):
            return rhs
        else:
            return lhs
