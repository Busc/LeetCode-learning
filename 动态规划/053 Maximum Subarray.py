# -*-coding:utf-8-*-
'''
Easy

Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

'''

class Solution(object):
    def maxArray(self, nums):
        """
        :param nums:List[int]
        :return: int
        """
        if not nums:
            return 0
        length = len(nums)
        current = nums[0]
        maxSum = current
        for i in range(1, length):
            # nums[i] as the end of subarray
            if current <= 0:
                current = 0
            # add 'current' when current > 0
            current += nums[i]
            maxSum = max(current, maxSum)
        return maxSum

if __name__ == "__main__":
    print(Solution().maxArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))