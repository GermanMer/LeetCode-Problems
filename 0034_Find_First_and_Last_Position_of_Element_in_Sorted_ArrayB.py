#Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

#If target is not found in the array, return [-1, -1].

#You must write an algorithm with O(log n) runtime complexity.

#Example 1:
#Input: nums = [5,7,7,8,8,10], target = 8
#Output: [3,4]

#Example 2:
#Input: nums = [5,7,7,8,8,10], target = 6
#Output: [-1,-1]

#Example 3:
#Input: nums = [], target = 0
#Output: [-1,-1]

#Constraints:
#0 <= nums.length <= 105
#-109 <= nums[i] <= 109
#nums is a non-decreasing array.
#-109 <= target <= 109

# La siguiente solución que cumple con la complejidad de tiempo O(log n) utilizando una búsqueda binaria para encontrar las posiciones de inicio y fin del rango:

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeftIndex(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def findRightIndex(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        leftIndex = findLeftIndex(nums, target)
        rightIndex = findRightIndex(nums, target)

        # Check if the target is within the bounds
        if leftIndex <= rightIndex and leftIndex < len(nums) and nums[leftIndex] == target:
            return [leftIndex, rightIndex]
        else:
            return [-1, -1]

#Example 1:
nums = [5,7,7,8,8,10]
target = 8
#Output: [3,4]
print(Solution().searchRange(nums, target))

#Example 2:
nums = [5,7,7,8,8,10]
target = 6
#Output: [-1,-1]
print(Solution().searchRange(nums, target))

#Example 3:
nums = []
target = 0
#Output: [-1,-1]
print(Solution().searchRange(nums, target))

#Explicación del algoritmo:
#1) Función findLeftIndex: Encuentra el índice más a la izquierda del target. Utiliza una búsqueda binaria para reducir el rango de búsqueda y encuentra el primer índice donde target puede estar.
#2) Función findRightIndex: Encuentra el índice más a la derecha del target. Utiliza una búsqueda binaria similar a la anterior pero ajustando las condiciones para encontrar el último índice donde target puede estar.
#3) Comprobación final: Después de encontrar los índices de la izquierda y la derecha, se verifica si realmente contienen el target y se devuelve el rango correspondiente. Si no, se devuelve [-1, -1].

#Este enfoque garantiza una complejidad de tiempo O(log n) al utilizar búsqueda binaria en lugar de un enfoque lineal.
