class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        localmax = globalmax = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i]+localmax:
                localmax = nums[i]
            else:
                localmax = nums[i]+localmax
            if localmax>globalmax:
                globalmax = localmax
        return globalmax
            
       