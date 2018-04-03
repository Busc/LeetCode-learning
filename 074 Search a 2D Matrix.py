'''
Array -- Medium

same as Problem-240(Search a 2D Matrix II)

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

  1) Integers in each row are sorted from left to right.
  2) The first integer of each row is greater than the last integer of the previous row.
'''

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # edge case：matrix is empty
        if matrix:
            rowNum = len(matrix)
            colNum = len(matrix[0])
            row = 0
            col = colNum - 1
            while row < rowNum and col >= 0:
                if target == matrix[row][col]:
                    return True
                elif target > matrix[row][col]:
                    row += 1
                else:
                    col -= 1
        return False
