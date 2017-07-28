'''
Array -- Easy

Given numRows, generate the first numRows of Pascal's triangle.

For example, given numRows = 5,
Return

[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
'''

class Solution(object):
    def generate(self, numRows):
        """
        :param numRows: int
        :return:List[List[int]]
        """
        if numRows < 1:
            return []
        result = [[1]]
        while numRows > 1:
            # zip():parallel iteration
            result.append([1] + [a + b for a, b in zip(result[-1], result[-1][1:])] + [1])
            numRows -= 1
        return result

if __name__ == "__main__":
    # assert Solution().generate(5) == [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    print(Solution().generate(5))
