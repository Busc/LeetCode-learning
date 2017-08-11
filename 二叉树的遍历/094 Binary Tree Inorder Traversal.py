'''
Tree -- Medium

Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [1,3,2].

Note: Recursive solution is trivial, could you do it iteratively?
'''


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :param root: TreeNode
        :return: List[int]
        """
        travResult = []
        stack = []
        while root or stack:
            # trace back to the 'bottom' layer
            while root:
                stack.append(root)
                root = root.left
            # stack: father + leftchild
            if stack:
                root = stack.pop()
                travResult.append(root.val)
                # visit the right subtree
                root = root.right
        return travResult

if __name__ == "__main__":
    # new node
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    # build connection
    node1.right = node2
    node2.left = node3
    # assert Solution().inorderTraversal(node1) == [1, 3, 2]
    print(Solution().inorderTraversal(node1))