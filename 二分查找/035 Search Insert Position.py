'''
Binary Search -- Easy

Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.
'''

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        tgInd = None
        first_ind, last_ind = 0, len(nums)-1
        while first_ind <= last_ind:
            mid_ind = first_ind + (last_ind - first_ind) // 2
            if nums[mid_ind] == target:
                tgInd = mid_ind
                break
            elif nums[mid_ind] < target:
                first_ind = mid_ind + 1
            else:
                last_ind = mid_ind - 1
        # target is not found
        if not tgInd:
            tgInd = first_ind
        return tgInd

if __name__ == "__main__":
    print(Solution().searchInsert([1, 3, 5, 6], 5))
    print(Solution().searchInsert([1, 3, 5, 6], 2))
    print(Solution().searchInsert([1, 3, 5, 6], 7))
    print(Solution().searchInsert([1, 3, 5, 6], 0))