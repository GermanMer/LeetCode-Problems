# The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

# By listing and labeling all of the permutations in order, we get the following sequence for n = 3:
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"

# Given n and k, return the kth permutation sequence.

# Example 1:
# Input: n = 3, k = 3
# Output: "213"

# Example 2:
# Input: n = 4, k = 9
# Output: "2314"

# Example 3:
# Input: n = 3, k = 1
# Output: "123"

# Constraints:
# 1 <= n <= 9
# 1 <= k <= n!

# Esta solución es mucho más eficiente, ya que evita la generación de todas las permutaciones y opera en tiempo O(n^2) en el peor de los casos.

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Crear una lista de números disponibles
        numbers = list(range(1, n + 1))
        # Ajustar k a índice basado en 0
        k -= 1
        # Crear una lista para la respuesta
        result = []
        # Calcular factoriales
        factorial = [1] * (n + 1)
        for i in range(1, n + 1):
            factorial[i] = factorial[i - 1] * i

        # Generar la k-ésima permutación
        for i in range(n):
            idx = k // factorial[n - 1 - i]  # Determinar el índice del número actual
            result.append(str(numbers[idx]))  # Añadir el número al resultado
            numbers.pop(idx)  # Eliminar el número usado
            k %= factorial[n - 1 - i]  # Actualizar k

        return ''.join(result)

# Example 1:
n = 3
k = 3
# Output: "213"
print(Solution().getPermutation(n, k))

# Example 2:
n = 4
k = 9
# Output: "2314"
print(Solution().getPermutation(n, k))

# Example 3:
n = 3
k = 1
# Output: "123"
print(Solution().getPermutation(n, k))
