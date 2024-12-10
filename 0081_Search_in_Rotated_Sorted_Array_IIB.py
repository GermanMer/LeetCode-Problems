# There is an integer array nums sorted in non-decreasing order (not necessarily with distinct values).

# Before being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,4,4,5,6,6,7] might be rotated at pivot index 5 and become [4,5,6,6,7,0,1,2,4,4].

# Given the array nums after the rotation and an integer target, return true if target is in nums, or false if it is not in nums.

# You must decrease the overall operation steps as much as possible.

# Example 1:
# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true

# Example 2:
# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false

# Constraints:
# 1 <= nums.length <= 5000
# -104 <= nums[i] <= 104
# nums is guaranteed to be rotated at some pivot.
# -104 <= target <= 104

# Follow up: This problem is similar to Search in Rotated Sorted Array, but nums may contain duplicates. Would this affect the runtime complexity? How and why?

# La solución anterior verifica correctamente si el objetivo está en el arreglo rotado usando el operador in. Sin embargo, aunque funciona, no es óptima para las restricciones dadas, ya que usar target in nums tiene una complejidad de tiempo O(n), lo que puede ser ineficiente, especialmente con el tamaño máximo del arreglo de 5000.
# Para mejorar la solución, puedes implementar un enfoque de búsqueda binaria modificada que tenga en cuenta el hecho de que el arreglo está rotado y puede contener duplicados. Esto te permitirá lograr una mejor complejidad de tiempo promedio de O(log n), aunque la complejidad en el peor caso aún puede degradarse a O(n) debido a los duplicados.
# Enfoque de búsqueda binaria:

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return True

            # Manejo de duplicados
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[left] <= nums[mid]:  # La mitad izquierda está ordenada
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # La mitad derecha está ordenada
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return False

# Example 1:
nums = [2,5,6,0,0,1,2]
target = 0
# Output: true
print(Solution().search(nums, target))

# Example 2:
nums = [2,5,6,0,0,1,2]
target = 3
# Output: false
print(Solution().search(nums, target))
