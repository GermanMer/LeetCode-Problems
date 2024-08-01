#A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

#For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
#The next permutation of an array of integers is the next lexicographically greater permutation of its integer. More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

#For example, the next permutation of arr = [1,2,3] is [1,3,2].
#Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
#While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.

#Given an array of integers nums, find the next permutation of nums.
#The replacement must be in place and use only constant extra memory.

#Example 1:
#Input: nums = [1,2,3]
#Output: [1,3,2]

#Example 2:
#Input: nums = [3,2,1]
#Output: [1,2,3]

#Example 3:
#Input: nums = [1,1,5]
#Output: [1,5,1]

#Constraints:
#1 <= nums.length <= 100
#0 <= nums[i] <= 100

# Algoritmo "Next Permutation", que utiliza solo operaciones in-place y memoria constante.
# Explicación del algoritmo:
# 1) Buscar la primera posición i desde el final donde nums[i] < nums[i + 1].
    # Esto identifica el punto donde la secuencia deja de ser no creciente.
# 2) Si tal posición i se encuentra, buscar la posición j desde el final donde nums[j] > nums[i].
    #Esto encuentra el número justo mayor que nums[i] para intercambiar.
# 3) Intercambiar nums[i] y nums[j].
# 4) Revertir la secuencia desde i + 1 hasta el final de la lista para obtener la siguiente permutación mínima.
#Este método es eficiente, con una complejidad de tiempo de O(n) y una complejidad de espacio de O(1), ya que modifica la lista en su lugar sin necesidad de almacenamiento adicional.

from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        No devuelve nada, modifica nums in-place.
        """
        # Encontrar la primera posición decreciente desde el final
        i = len(nums) - 2  # Inicia desde el penúltimo elemento
        while i >= 0 and nums[i] >= nums[i + 1]:  # Busca hacia atrás mientras el orden decrece
            i -= 1

        # Si se encuentra dicha posición
        if i >= 0:
            # Encontrar el siguiente elemento mayor desde el final
            j = len(nums) - 1  # Inicia desde el último elemento
            while j >= 0 and nums[j] <= nums[i]:  # Busca hacia atrás hasta encontrar un número mayor que nums[i]
                j -= 1
            # Intercambiar los elementos
            nums[i], nums[j] = nums[j], nums[i]  # Realiza el intercambio

        # Revertir los elementos a la derecha del índice encontrado
        nums[i + 1:] = reversed(nums[i + 1:])  # Invierte la sublista desde i+1 hasta el final

# Ejemplo 1:
nums = [1, 2, 3]
Solution().nextPermutation(nums)
print(nums)  # Salida: [1, 3, 2]

# Ejemplo 2:
nums = [3, 2, 1]
Solution().nextPermutation(nums)
print(nums)  # Salida: [1, 2, 3]

# Ejemplo 3:
nums = [1, 1, 5]
Solution().nextPermutation(nums)
print(nums)  # Salida: [1, 5, 1]
