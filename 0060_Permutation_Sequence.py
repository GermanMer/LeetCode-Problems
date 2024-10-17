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

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        num = []
        count = 0
        permutations = []
        resultado = ""

        for i in range(n):
            count += 1
            num.append(count)

        #print(num)

        def backtrack(path, restantes):
            # Si no quedan números restantes, añade la permutación actual al resultado
            if not restantes:
                permutations.append(path)
                # Itera sobre los números restantes
            for i in range(len(restantes)):
                # Realiza un seguimiento de la ruta actual y los números restantes
                backtrack(path + [restantes[i]], restantes[:i] + restantes[i+1:])

        backtrack([], num)  # Inicia el backtracking con una ruta vacía y todos los números
        for i in permutations[k - 1]:
            resultado = resultado + str(i)

        #print(type(resultado))

        return resultado

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
