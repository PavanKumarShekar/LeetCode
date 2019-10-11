'''
1. Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
'''

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for index,value in enumerate(nums):
            number = target - value
            if number in dic:
                return[dic[number], index]
            else:
                dic[value]=index


def main():
    TwoSum = Solution()
    output = TwoSum.twoSum([2, 7, 11, 15],9)
    print (output)


if __name__ == "__main__":
    main()
