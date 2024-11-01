# Given two binary strings a and b, return their sum as a binary string.

# Example 1:
# Input: a = "11", b = "1"
# Output: "100"

# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"

# Constraints:
# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

# Suma binaria:
# 0 + 0 = 0
# 0 + 1 = 1
# 1 + 0 = 1
# 1 + 1 = 10 (es decir, pones 0 y llevas 1 a la siguiente columna)
# 1 + 1 + 1 (si también hay un acarreo) = 11 (pones 1 y llevas 1)

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Aseguramos que ambas cadenas tengan la misma longitud
        max_len = max(len(a), len(b))
        bin1 = a.zfill(max_len) # La función .zfill() se utiliza para rellenar una cadena con ceros ('0') a la izquierda, de modo que la longitud total de la cadena alcance un número especificado.
        bin2 = b.zfill(max_len)

        resultado = []
        carry = 0

        # Sumar de derecha a izquierda
        for i in range(max_len - 1, -1, -1):
            bit1 = int(bin1[i])
            bit2 = int(bin2[i])
            total = bit1 + bit2 + carry

            # El nuevo bit es total % 2
            resultado.append(str(total % 2))
            # El carry es total // 2
            carry = total // 2

        # Si hay un carry final, lo añadimos
        if carry:
            resultado.append(str(carry))

        # Devolvemos el resultado invertido y convertido a cadena
        return ''.join(resultado[::-1])

# Example 1:
a = "11"
b = "1"
# Output: "100"
print(Solution().addBinary(a, b))

# Example 2:
a = "1010"
b = "1011"
# Output: "10101"
print(Solution().addBinary(a, b))
