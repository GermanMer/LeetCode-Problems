#Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

#Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.

#Example 1:
#Input: num1 = "2", num2 = "3"
#Output: "6"

#Example 2:
#Input: num1 = "123", num2 = "456"
#Output: "56088"

#Constraints:
#1 <= num1.length, num2.length <= 200
#num1 and num2 consist of digits only.
#Both num1 and num2 do not contain any leading zero, except the number 0 itself.

# Para multiplicar dos números representados como cadenas sin usar conversiones directas a enteros, puedes usar el método tradicional de multiplicación manual que se enseña en la escuela. La idea es realizar la multiplicación de cada dígito y luego sumar los resultados teniendo en cuenta las posiciones.

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Manejar casos especiales
        if num1 == "0" or num2 == "0":
            return "0"

        # Preparar una lista para almacenar los resultados de las multiplicaciones parciales
        m, n = len(num1), len(num2)
        pos = [0] * (m + n)

        # Realizar la multiplicación manual
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # Multiplicar los dígitos
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                # Posiciones en la lista de resultados
                p1, p2 = i + j, i + j + 1
                # Sumar el producto al resultado actual
                sum_ = mul + pos[p2]
                # Actualizar la posición con la unidad del resultado
                pos[p2] = sum_ % 10
                # Actualizar la posición anterior con el acarreo
                pos[p1] += sum_ // 10

        # Convertir el resultado a una cadena y eliminar ceros a la izquierda
        result = ''.join(map(str, pos))
        return result.lstrip('0')  # Eliminar ceros a la izquierda

#Example 1:
num1 = "2"
num2 = "3"
#Output: "6"
print(Solution().multiply(num1, num2))

#Example 2:
num1 = "123"
num2 = "456"
#Output: "56088"
print(Solution().multiply(num1, num2))
