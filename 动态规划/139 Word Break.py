'''
Medium

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

UPDATE (2017/1/4):
The wordDict parameter had been changed to a list of strings (instead of a set of strings). Please reload the code definition to get the latest changes.
'''

class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        :param s:str
        :param wordDict:List[str]
        :return:bool
        """
        length = len(s)
        dp = [False] * (length+1)
        dp[0] = True
        for i in range(length):
            for j in range(i, -1, -1):
                if dp[j] and s[j:i+1] in wordDict:
                    dp[i+1] = True
                    break
        return dp[length]


if __name__ == "__main__":
    print(Solution().wordBreak("leetcode", ["leet", "code"]))

