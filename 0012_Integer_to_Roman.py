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
        unidad = 1
        num_descompuesto = []
        while num > 0:
            digito = num % 10  # Extrae el último dígito
            num_descompuesto.append(digito * unidad)
            unidad = unidad * 10
            num = num // 10  # Elimina el último dígito

        num_descompuesto.reverse()
        result = ""
        for i in num_descompuesto:
            if i < 4:
                result = result + ("I" * i)
            elif i == 4:
                result = result + "IV"
            elif i == 5:
                result = result + "V"
            elif i > 5 and i < 9:
                result = result + "V" + ("I" * (i - 5))
            elif i == 9:
                result = result + "IX"
            elif i > 9 and i < 40:
                result = result + "X" * (i//10)
            elif i == 40:
                result = result + "XL"
            elif i == 50:
                result = result + "L"
            elif i > 50 and i < 90:
                result = result + "L" + ("X" * ((i - 50) // 10))
            elif i == 90:
                result = result + "XC"
            elif i > 90 and i < 400:
                result = result + "C" * (i//100)
            elif i == 400:
                result = result + "CD"
            elif i == 500:
                result = result + "D"
            elif i > 500 and i < 900:
                result = result + "D" + ("C" * ((i - 500) // 100))
            elif i == 900:
                result = result + "CM"
            elif i > 900 and i:
                result = result + "M" * (i//1000)
        return result

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
