'''
Array -- Easy

Given an index k, return the kth row of the Pascal's triangle.

For example, given k = 3,
Return [1,3,3,1].

Note:
Could you optimize your algorithm to use only O(k) extra space?
'''

class Solution(object):
    def getRow(self, rowIndex):
        """
        :param rowIndex: int
        :return: List[int]
        """
        # rowIndex is indexed from 0.
        # kth row:space k+1
        result = [1] * (rowIndex + 1)
        for i in range(2, rowIndex+1):
            for j in range(1, i):
                result[i-j] += result[i-j-1]
        return result

if __name__ == "__main__":
    print(Solution().getRow(3))