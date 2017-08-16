'''
Tree -- Easy

Given an array where elements are sorted in ascending order, convert it to a height balanced BST.
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :param nums:List[int]
        :return:TreeNode
        """
        return self._sortedArrayToBST(nums, 0, len(nums))

    def _sortedArrayToBST(self, nums, start, end):
        if start == end:
            return None
        mid = (start + end)/2
        root = TreeNode(nums[mid])
        root.left = self._sortedArrayToBST(nums, start, mid)
        root.right = self._sortedArrayToBST(nums, mid+1, end)
        return root

