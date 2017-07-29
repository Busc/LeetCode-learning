'''
Array -- Medium

A robot is located at the top-left corner of a m x n grid.

The robot can only move either down or right at any point in time.
The robot is trying to reach the bottom-right corner of the grid.

How many possible unique paths are there?

Note: m and n will be at most 100.
'''

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :param m:int
        :param n:int
        :return:int
        """
        #  m x n grid
        dp = [[1 for __ in range(n)] for __ in range(m)]
        for i in range(1, n):
            for j in range(1, m):
                dp[j][i] = dp[j-1][i]+dp[j][i-1]
        return dp[m-1][n-1]

if __name__ == "__main__":
    # assert Solution().uniquePaths(3, 7) == 28
    print(Solution().uniquePaths(3, 7))