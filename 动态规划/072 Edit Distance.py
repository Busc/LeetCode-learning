'''
String -- Hard

Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)

You have the following 3 operations permitted on a word:

a) Insert a character
b) Delete a character
c) Replace a character
'''

class Solution(object):
    def minDistance(self, word1, word2):
        """
        :param word1:string
        :param word2: string
        :return: int
        """
        cols1 = len(word1)
        rows2 = len(word2)
        dp = [[0 for __ in range(cols1+1)] for __ in range(rows2+1)]

        for j in range(cols1+1):
            dp[0][j] = j
        for i in range(rows2+1):
            dp[i][0] = i
        for i in range(1, rows2+1):
            for j in range(1, cols1+1):
                onemore = 1 if word1[j-1] != word2[i-1] else 0
                # 3 cases in the last operation:
                dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1, dp[i-1][j-1]+onemore)
        return dp[rows2][cols1]

if __name__ == "__main__":
    assert Solution().minDistance("", "a") == 1
    assert Solution().minDistance("faf", "efef") == 2