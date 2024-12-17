# Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

# Example 1:
# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10 units.

# Example 2:
# Input: heights = [2,4]
# Output: 4

# Constraints:
# 1 <= heights.length <= 105
# 0 <= heights[i] <= 104

from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 1:
            return [heights[0]]
        elif len(heights) == 2:
            return min(heights) * 2
        else:
            indices = [0, 0]
            alturas = [indices[0], 0]

            indice_actual = 1
            for i in heights[1:]:
                if i <= alturas[0]:
                    indices[1] = indice_actual
                else:
                    alturas[1] = alturas[0]
                    indices[1] = indice_actual + 1
                    alturas[0] = i
                    indices[0] = indice_actual

                #print("indice actual", indice_actual)
                #print("indices", indices)
                #print("alturas", alturas)

                indice_actual = indice_actual + 1

            return min(alturas) * (indices[1] - indices[0])

# Example 1:
heights = [2,1,5,6,2,3]
# Output: 10
print(Solution().largestRectangleArea(heights))

# Example 2:
heights = [2,4]
# Output: 4
print(Solution().largestRectangleArea(heights))
