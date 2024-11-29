# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].

# You may return the answer in any order.

# Example 1:
# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

# Example 2:
# Input: n = 1, k = 1
# Output: [[1]]
# Explanation: There is 1 choose 1 = 1 total combination.

# Constraints:
# 1 <= n <= 20
# 1 <= k <= n

from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        if n == 1:
            return [[1]]

        result = []

        temp = []
        num = 0
        for i in range(n):
            num += 1
            temp.append(num)
        #print(temp)

        for x in temp[:-1]:
            for y in temp[temp.index(x) + 1 :]:
                par = [x]
                for z in range(k-1):
                    par.append(y)
                    try:
                        y = temp[temp.index(y) + 1]
                    except:
                        break
                if len(par) == k:
                    result.append(par)

        return result

# Example 1:
n = 4
k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
print(Solution().combine(n, k))

# Example 2:
n = 1
k = 1
# Output: [[1]]
print(Solution().combine(n, k))

# Example 3:
# n = 4
# k = 3
# Output: [[1, 2, 3], [1, 2, 4], [1, 3, 4], [2, 3, 4]]
# print(Solution().combine(n, k))
