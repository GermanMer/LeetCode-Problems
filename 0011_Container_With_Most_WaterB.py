#You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
#Find two lines that together with the x-axis form a container, such that the container contains the most water.
#Return the maximum amount of water a container can store.
#Notice that you may not slant the container.

#Example 1:
#Input: height = [1,8,6,2,5,4,8,3,7]
#Output: 49
#Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

#Example 2:
#Input: height = [1,1]
#Output: 1

#Constraints:
#n == height.length
#2 <= n <= 105
#0 <= height[i] <= 104

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # Calcula el área con las líneas en las posiciones 'left' y 'right'
            width = right - left
            current_height = min(height[left], height[right])
            current_area = width * current_height

            # Actualiza el área máxima si es mayor que la actual
            max_area = max(max_area, current_area)

            # Mueve el puntero de la línea más baja
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

#Example 1:
height = [1,8,6,2,5,4,8,3,7]
#Output: 49
print(Solution().maxArea(height))

#Example 2:
height = [1,1]
#Output: 1
print(Solution().maxArea(height))

#Explicación:
#Inicialización: Se inician dos punteros, left al principio de la lista y right al final de la lista.
#Cálculo del área: Se calcula el área entre las líneas en las posiciones left y right como el producto del ancho (diferencia de índices) y la altura mínima entre las dos líneas.
#Actualización del área máxima: Se actualiza max_area si el área calculada es mayor.
#Movimiento de los punteros: Se mueve el puntero de la línea más baja (si height[left] < height[right], se incrementa left, de lo contrario, se decrementa right) para intentar encontrar una combinación de líneas que contengan más agua.
#Retorno del resultado: Después de recorrer la lista, se retorna max_area.
