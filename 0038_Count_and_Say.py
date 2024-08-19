#The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
#countAndSay(1) = "1"
#countAndSay(n) is the run-length encoding of countAndSay(n - 1).
#Run-length encoding (RLE) is a string compression method that works by replacing consecutive identical characters (repeated 2 or more times) with the concatenation of the character and the number marking the count of the characters (length of the run). For example, to compress the string "3322251" we replace "33" with "23", replace "222" with "32", replace "5" with "15" and replace "1" with "11". Thus the compressed string becomes "23321511".

#Given a positive integer n, return the nth element of the count-and-say sequence.

#Example 1:
#Input: n = 4
#Output: "1211"
#Explanation:
#countAndSay(1) = "1"
#countAndSay(2) = RLE of "1" = "11"
#countAndSay(3) = RLE of "11" = "21"
#countAndSay(4) = RLE of "21" = "1211"

#Example 2:
#Input: n = 1
#Output: "1"
#Explanation:
#This is the base case.

#Constraints:
#1 <= n <= 30

#Follow up: Could you solve it iteratively?

class Solution:
    def countAndSay(self, n: int) -> str:
        # Si n es 1, simplemente devolvemos "1", ya que es el caso base.
        if n == 1:
            return "1"

        # Inicializamos la secuencia con el primer término, que es "1".
        prev = "1"

        # Este bucle se ejecuta desde 2 hasta n (incluyendo n).
        # Se utiliza para generar cada término de la secuencia a partir del anterior.
        for i in range(2, n + 1):
            # Inicializamos la cadena actual que construiremos.
            curr = ""
            # Contador para las repeticiones de caracteres consecutivos.
            count = 1

            # Este bucle recorre la cadena anterior (prev) desde el segundo carácter hasta el final.
            for j in range(1, len(prev)):
                # Si el carácter actual es igual al anterior, incrementamos el contador.
                if prev[j] == prev[j - 1]:
                    count += 1
                else:
                    # Si el carácter actual es diferente, añadimos el contador y el carácter anterior a la cadena actual.
                    curr += str(count) + prev[j - 1]
                    # Reiniciamos el contador para el nuevo carácter.
                    count = 1

            # Añadimos el último grupo de caracteres contados a la cadena actual.
            curr += str(count) + prev[-1]
            # Actualizamos prev para la siguiente iteración.
            prev = curr

        # Devolvemos el término n-ésimo de la secuencia.
        return prev

#Example 1:
n = 4
#Output: "1211"
print(Solution().countAndSay(n))

#Example 2:
n = 1
#Output: "1"
print(Solution().countAndSay(n))
