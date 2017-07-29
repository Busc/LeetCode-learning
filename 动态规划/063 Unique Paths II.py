'''
Array -- Medium

Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.
'''
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :param obstacleGrid:List[List[int]]
        :return: int
        """
        # 'start' has an obstacle
        if obstacleGrid[0][0] == 1:
            return 0
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        # rows x cols grid
        dp = [[0 for __ in range(cols)] for __ in range(rows)]
        dp[0][0] = 1
        for i in range(1, rows):
            dp[i][0] = dp[i-1][0] if obstacleGrid[i][0] == 0 else 0
        for j in range(1, cols):
            dp[0][j] = dp[0][j-1] if obstacleGrid[0][j] == 0 else 0
        # unique paths
        for i in range(1, rows):
            for j in range(1, cols):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j]+dp[i][j-1]
        return dp[rows-1][cols-1]

if __name__ == "__main__":
    # assert Solution().uniquePathsWithObstacles([
    #     [0, 0, 0],
    #     [0, 1, 0],
    #     [0, 0, 0]
    # ]) == 2
    print(Solution().uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))