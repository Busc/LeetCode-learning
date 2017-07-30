'''
Array -- Medium

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
'''

class Solution(object):
    def minPathSum(self, grid):
        """
        :param grid:List[List[int]]
        :return: int
        """
        rows = len(grid)
        cols = len(grid[0])
        # one-dimensional
        dp = [0 for __ in range(cols)]

        dp[0] = grid[0][0]
        for j in range(1, cols):
            dp[j] = dp[j-1]+grid[0][j]

        for i in range(1, rows):
            dp[0] += grid[i][0]
            for j in range(1, cols):
                dp[j] = min(dp[j], dp[j-1])+grid[i][j]
        return dp[-1]



if __name__ == "__main__":
    # assert Solution().minPathSum([
    #     [1, 2, 4],
    #     [2, 4, 1],
    #     [3, 2, 1]]) == 9
    print(Solution().minPathSum([[1, 2, 4], [2, 4, 1], [3, 2, 1]]))