'''
Tree -- Hard

Given a binary tree, return the postorder traversal of its nodes' values.

For example:
Given binary tree {1,#,2,3},
   1
    \
     2
    /
   3
return [3,2,1].

Note: Recursive solution is trivial, could you do it iteratively?
'''

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :param root: TreeNode
        :return: List[int]
        """
        if not root:
            return []
        travResult = []
        stack = [(root, 'non')]
        while stack:
            root, flag = stack.pop()
            # 'non': node is not visited
            # 'once': node has been visited once
            if flag == 'non':
                stack.append((root, 'once'))
                if root.right:
                    stack.append((root.right, 'non'))
                if root.left:
                    stack.append((root.left, 'non'))
            else:
                travResult.append(root.val)
        return travResult

if __name__ == "__main__":
    # new node
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    # build connection
    node1.right = node2
    node2.left = node3
    # assert Solution().postorderTraversal(node1) == [3, 2, 1]
    print(Solution().postorderTraversal(node1))