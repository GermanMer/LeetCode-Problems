#Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

#A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.

#Example 1:
#Input: digits = "23"
#Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

#Example 2:
#Input: digits = ""
#Output: []

#Example 3:
#Input: digits = "2"
#Output: ["a","b","c"]

#Constraints:
#0 <= digits.length <= 4
#digits[i] is a digit in the range ['2', '9'].

class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        code = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        combinations = [""]

        for digit in digits: # Iterar sobre cada dígito en la cadena de entrada
            letters = code[digit] # Obtener las letras correspondientes al dígito actual
            combinations = [prefix + letter for prefix in combinations for letter in letters] # Generar nuevas combinaciones añadiendo cada letra a cada combinación existente

        return combinations

#Example 1:
digits = "23"
#Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(Solution().letterCombinations(digits))

#Example 2:
digits = ""
#Output: []
print(Solution().letterCombinations(digits))

#Example 3:
digits = "2"
#Output: ["a","b","c"]
print(Solution().letterCombinations(digits))

#Example 4:
#digits = "2345"
#Output: ["adgj", "adgk", "adgl", "adhj", "adhk", "adhl", "adij", "adik", "adil", "aegj", "aegk", "aegl", "aehj", "aehk", "aehl", "aeij", "aeik", "aeil", "afgj", "afgk", "afgl", "afhj", "afhk", "afhl", "afij", "afik", "afil", "bdgj", "bdgk", "bdgl", "bdhj", "bdhk", "bdhl", "bdij", "bdik", "bdil", "begj", "begk", "begl", "behj", "behk", "behl", "beij", "beik", "beil", "bfgj", "bfgk", "bfgl", "bfhj", "bfhk", "bfhl", "bfij", "bfik", "bfil", "cdgj", "cdgk", "cdgl", "cdhj", "cdhk", "cdhl", "cdij", "cdik", "cdil", "cegj", "cegk", "cegl", "cehj", "cehk", "cehl", "ceij", "ceik", "ceil", "cfgj", "cfgk", "cfgl", "cfhj", "cfhk", "cfhl", "cfij", "cfik", "cfil"]
#print(Solution().letterCombinations(digits))
