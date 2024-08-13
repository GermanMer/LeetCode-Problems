#Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

#You must write an algorithm with O(log n) runtime complexity.

#Example 1:
#Input: nums = [1,3,5,6], target = 5
#Output: 2

#Example 2:
#Input: nums = [1,3,5,6], target = 2
#Output: 1

#Example 3:
#Input: nums = [1,3,5,6], target = 7
#Output: 4

#Constraints:
#1 <= nums.length <= 104
#-104 <= nums[i] <= 104
#nums contains distinct values sorted in ascending order.
#-104 <= target <= 104

#Para cumplir con el requisito de 𝑂(log 𝑛), debemos usar una búsqueda binaria.
#Aquí está la solución corregida utilizando búsqueda binaria:

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Inicializa los punteros izquierdo y derecho para la búsqueda binaria
        left, right = 0, len(nums) - 1

        # Mientras el puntero izquierdo no sobrepase al derecho
        while left <= right:
            # Calcula el índice medio
            mid = (left + right) // 2

            # Si el elemento en el índice medio es igual al objetivo, devuelve el índice medio
            if nums[mid] == target:
                return mid
            # Si el elemento en el índice medio es menor que el objetivo, busca en la mitad derecha
            elif nums[mid] < target:
                left = mid + 1
            # Si el elemento en el índice medio es mayor que el objetivo, busca en la mitad izquierda
            else:
                right = mid - 1

        # Si no se encuentra el objetivo, devuelve la posición donde debería insertarse
        return left

#Example 1:
nums = [1,3,5,6]
target = 5
#Output: 2
print(Solution().searchInsert(nums, target))

#Example 2:
nums = [1,3,5,6]
target = 2
#Output: 1
print(Solution().searchInsert(nums, target))

#Example 3:
nums = [1,3,5,6]
target = 7
#Output: 4
print(Solution().searchInsert(nums, target))
