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
        # Agregar un 0 al final para garantizar que se vacíe la pila al final
        heights.append(0)
        stack = []  # Pila para almacenar índices de las barras
        max_area = 0

        for i in range(len(heights)):
            # Mientras la pila no esté vacía y la altura actual sea menor que la altura en el índice en la pila
            while stack and heights[i] < heights[stack[-1]]:
                h = heights[stack.pop()]  # Altura del rectángulo formado por el índice pop
                w = i if not stack else i - stack[-1] - 1  # El ancho depende de la diferencia entre los índices
                max_area = max(max_area, h * w)  # Calculamos el área y actualizamos el área máxima

            stack.append(i)  # Agregamos el índice actual a la pila

        return max_area

# Example 1:
heights = [2,1,5,6,2,3]
# Output: 10
print(Solution().largestRectangleArea(heights))

# Example 2:
heights = [2,4]
# Output: 4
print(Solution().largestRectangleArea(heights))
