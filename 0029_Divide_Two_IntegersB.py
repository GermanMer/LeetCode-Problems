#Given two integers dividend and divisor, divide two integers without using multiplication, division, and mod operator.

#The integer division should truncate toward zero, which means losing its fractional part. For example, 8.345 would be truncated to 8, and -2.7335 would be truncated to -2.

#Return the quotient after dividing dividend by divisor.

#Note: Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem, if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the quotient is strictly less than -231, then return -231.

#Example 1:
#Input: dividend = 10, divisor = 3
#Output: 3
#Explanation: 10/3 = 3.33333.. which is truncated to 3.

#Example 2:
#Input: dividend = 7, divisor = -3
#Output: -2
#Explanation: 7/-3 = -2.33333.. which is truncated to -2.

#Constraints:
#-231 <= dividend, divisor <= 231 - 1
#divisor != 0

class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constantes para el rango de un entero de 32 bits
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        # Manejo de casos de overflow
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        # Determinar el signo del resultado
        negative = (dividend < 0) != (divisor < 0)

        # Trabajar con valores absolutos
        dividend, divisor = abs(dividend), abs(divisor)

        # Inicializar el contador
        quotient = 0
        # Restar divisor de dividend hasta que el dividend sea menor que el divisor
        while dividend >= divisor:
            # Inicializar variables para el conteo exponencial
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            # Restar el múltiplo encontrado del dividend
            dividend -= temp
            # Agregar el múltiplo al resultado
            quotient += multiple

        # Aplicar el signo al resultado
        if negative:
            quotient = -quotient

        # Asegurar que el resultado está en el rango de 32 bits
        return min(max(quotient, INT_MIN), INT_MAX)

#Example 1:
dividend = 10
divisor = 3
#Output: 3
print(Solution().divide(dividend, divisor))

#Example 2:
dividend = 7
divisor = -3
#Output: -2
print(Solution().divide(dividend, divisor))
