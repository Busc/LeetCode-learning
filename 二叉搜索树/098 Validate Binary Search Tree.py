'''
Tree -- Medium

Given a binary tree, determine if it is a valid binary search tree (BST).

Example 1:
    2
   / \
  1   3
Binary tree [2,1,3], return true.
Example 2:
    1
   / \
  2   3
Binary tree [1,2,3], return false.
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isValidBST(self, root):
        """
        :param root:TreeNode
        :return:bool
        """
        stack = []
        prev = None
        # BT inorder traversal
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # inorder of BST is ascending
            if prev and root.val <= prev.val:
                return False
            prev = root
            root = root.right
        return True


if __name__ == "__main__":

    node11 = TreeNode(2)
    node12 = TreeNode(1)
    node13 = TreeNode(3)
    node11.left = node12
    node11.right = node13

    node21 = TreeNode(1)
    node22 = TreeNode(2)
    node23 = TreeNode(3)
    node21.left = node22
    node21.right = node23

    print(Solution().isValidBST(node11))
    print(Solution().isValidBST(node21))
