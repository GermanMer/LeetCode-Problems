#There is an integer array nums sorted in ascending order (with distinct values).

#Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

#Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

#You must write an algorithm with O(log n) runtime complexity.

#Example 1:
#Input: nums = [4,5,6,7,0,1,2], target = 0
#Output: 4

#Example 2:
#Input: nums = [4,5,6,7,0,1,2], target = 3
#Output: -1

#Example 3:
#Input: nums = [1], target = 0
#Output: -1

#Constraints:
#1 <= nums.length <= 5000
#-104 <= nums[i] <= 104
#All values of nums are unique.
#nums is an ascending array that is possibly rotated.
#-104 <= target <= 104


# La siguiente solución que cumple con la complejidad de tiempo O(log n) utilizando una búsqueda binaria modificada para arrays rotados:

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Determine which part is sorted
            if nums[left] <= nums[mid]:  # Left part is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:  # Right part is sorted
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

#Example 1:
nums = [4,5,6,7,0,1,2]
target = 0
#Output: 4
print(Solution().search(nums, target))

#Example 2:
nums = [4,5,6,7,0,1,2]
target = 3
#Output: -1
print(Solution().search(nums, target))

#Example 3:
nums = [1]
target = 0
#Output: -1
print(Solution().search(nums, target))

#Explicación del algoritmo:
#1) Inicialización: Se inicializan dos punteros, left y right, al principio y al final del array, respectivamente.
#2) Bucle de búsqueda: Mientras left sea menor o igual a right, se calcula el índice medio mid.
#3) Verificación del objetivo: Si nums[mid] es igual al target, se devuelve mid.
#4) Determinación de la parte ordenada:
    #Si nums[left] <= nums[mid], la parte izquierda está ordenada.
        #Si target está en el rango de nums[left] a nums[mid], se ajusta right a mid - 1.
        #De lo contrario, se ajusta left a mid + 1.
    #Si nums[left] > nums[mid], la parte derecha está ordenada.
        #Si target está en el rango de nums[mid] a nums[right], se ajusta left a mid + 1.
        #De lo contrario, se ajusta right a mid - 1.
#5) Si no se encuentra el objetivo, se devuelve -1.

#Esta solución asegura una complejidad de tiempo O(log n) al dividir continuamente el espacio de búsqueda a la mitad.
