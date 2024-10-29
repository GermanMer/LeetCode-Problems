# Given a string s, return whether s is a valid number.

# For example, all the following are valid numbers: "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789", while the following are not valid numbers: "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53".

# Formally, a valid number is defined using one of the following definitions:
# An integer number followed by an optional exponent.
# A decimal number followed by an optional exponent.
# An integer number is defined with an optional sign '-' or '+' followed by digits.
# A decimal number is defined with an optional sign '-' or '+' followed by one of the following definitions:
# Digits followed by a dot '.'.
# Digits followed by a dot '.' followed by digits.
# A dot '.' followed by digits.
# An exponent is defined with an exponent notation 'e' or 'E' followed by an integer number.

# The digits are defined as one or more digits.

# Example 1:
# Input: s = "0"
# Output: true

# Example 2:
# Input: s = "e"
# Output: false

# Example 3:
# Input: s = "."
# Output: false

# Constraints:
# 1 <= s.length <= 20

import re  # Importamos el módulo de expresiones regulares

class Solution:
    def isNumber(self, s: str) -> bool:
        # Definimos la expresión regular que describe un número válido
        # La expresión se descompone de la siguiente manera:
        # ^                       : Inicio de la cadena
        # [+-]?                   : Opcionalmente un signo '+' o '-'
        # (                       : Comienzo de un grupo
        #   (\d+(\.\d*)?|\.\d+)   : Parte entera o decimal
        #   |                     : O
        #   \d+                  : Solo dígitos
        # )                       : Fin del grupo
        # [eE][+-]?\d+?         : Parte exponencial (e o E, opcionalmente seguido de + o -, seguido de dígitos)
        # $                       : Fin de la cadena

        pattern = r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$'

        # Usamos el método fullmatch para verificar si toda la cadena coincide con el patrón
        return re.fullmatch(pattern, s) is not None

# Example 1:
s = "0"
# Output: true
print(Solution().isNumber(s))

# Example 2:
s = "e"
# Output: false
print(Solution().isNumber(s))

# Example 3:
s = "."
# Output: false
print(Solution().isNumber(s))
