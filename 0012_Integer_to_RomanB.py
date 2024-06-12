#Seven different symbols represent Roman numerals with the following values:

#Symbol  Value
#I       1
#V       5
#X       10
#L       50
#C       100
#D       500
#M       1000

#Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:
    #If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
    #If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
    #Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.

#Given an integer, convert it to a Roman numeral.

#Example 1:
#Input: num = 3749
#Output: "MMMDCCXLIX"
#Explanation:
#3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
# 700 = DCC as 500 (D) + 100 (C) + 100 (C)
#  40 = XL as 10 (X) less of 50 (L)
#   9 = IX as 1 (I) less of 10 (X)
#Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places

#Example 2:
#Input: num = 58
#Output: "LVIII"
#Explanation:
#50 = L
# 8 = VIII

#Example 3:
#Input: num = 1994
#Output: "MCMXCIV"
#Explanation:
#1000 = M
# 900 = CM
#  90 = XC
#   4 = IV

#Constraints:
#1 <= num <= 3999

class Solution:
    def intToRoman(self, num: int) -> str:
        # Se define una lista val que contiene los valores numéricos de los símbolos romanos en orden decreciente.
        val = [
            1000, 900, 500, 400,
            100, 90, 50, 40,
            10, 9, 5, 4,
            1
        ]
        # Esta lista syb contiene los símbolos romanos correspondientes a los valores en la lista val. Ambos están alineados, es decir, val[i] corresponde a syb[i].
        syb = [
            "M", "CM", "D", "CD",
            "C", "XC", "L", "XL",
            "X", "IX", "V", "IV",
            "I"
        ]
        roman_num = ''
        i = 0   # Se inicializa el índice i en 0. Este índice se usará para recorrer las listas val y syb.
        while num > 0:
            for _ in range(num // val[i]):  # "num // val[i]" calcula cuántas veces val[i] puede ser restado de num sin que num se vuelva negativo.
                roman_num += syb[i]         # En cada iteración del bucle for, se añade el símbolo romano correspondiente syb[i] a roman_num.
                num -= val[i]               # Se resta val[i] de num
            i += 1                          # Se incrementa el índice i en 1 para pasar al siguiente valor
        return roman_num

#Example 1:
num = 3749
#Output: "MMMDCCXLIX"

print(Solution().intToRoman(num))
#Example 2:
num = 58
#Output: "LVIII"
print(Solution().intToRoman(num))

#Example 3:
num = 1994
#Output: "MCMXCIV"
print(Solution().intToRoman(num))
#Explanation:
# 1) val[0] es 1000, así que 1994 // 1000 es 1.
    # Añadimos "M" a roman_num, ahora roman_num es "M".
    # Restamos 1000 de num, ahora num es 994.
# 2) val[1] es 900, así que 994 // 900 es 1.
    # Añadimos "CM" a roman_num, ahora roman_num es "MCM".
    # Restamos 900 de num, ahora num es 94.
# 3) val[2] y val[3] (500 y 400) no se pueden restar de 94, así que pasamos al siguiente.
# 4) val[4] es 100, no se puede restar de 94, así que pasamos al siguiente.
# 5) val[5] es 90, así que 94 // 90 es 1.
    # Añadimos "XC" a roman_num, ahora roman_num es "MCMXC".
    # Restamos 90 de num, ahora num es 4.
# 6) val[6] y val[7] (50 y 40) no se pueden restar de 4, así que pasamos al siguiente.
# 7) val[8], val[9], y val[10] (10, 9, y 5) no se pueden restar de 4, así que pasamos al siguiente.
# 8) val[11] es 4, así que 4 // 4 es 1.
    # Añadimos "IV" a roman_num, ahora roman_num es "MCMXCIV".
    # Restamos 4 de num, ahora num es 0.
