'''
Tree -- Medium

Given a binary tree, return the preorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,2,3].

Note: Recursive solution is trivial, could you do it iteratively?
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :param root: TreeNode
        :return: List[int]
        """
        travResult = []
        stack = []
        while root or stack:
            if not root:
                root = stack.pop()
            travResult.append(root.val)
            # save all 'right'
            if root.right:
                stack.append(root.right)
            root = root.left
        return travResult

if __name__ == "__main__":
    # new node
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    # build connection
    node1.right = node2
    node2.left = node3
    # assert Solution().preorderTraversal(node1) == [1, 2, 3]
    print(Solution().preorderTraversal(node1))