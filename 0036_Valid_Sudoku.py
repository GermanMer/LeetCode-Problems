#Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

#Each row must contain the digits 1-9 without repetition.
#Each column must contain the digits 1-9 without repetition.
#Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

#Note:
#A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#Only the filled cells need to be validated according to the mentioned rules.

#Example 1:
#Input: board =
#[["5","3",".",".","7",".",".",".","."]
#,["6",".",".","1","9","5",".",".","."]
#,[".","9","8",".",".",".",".","6","."]
#,["8",".",".",".","6",".",".",".","3"]
#,["4",".",".","8",".","3",".",".","1"]
#,["7",".",".",".","2",".",".",".","6"]
#,[".","6",".",".",".",".","2","8","."]
#,[".",".",".","4","1","9",".",".","5"]
#,[".",".",".",".","8",".",".","7","9"]]
#Output: true

#Example 2:
#Input: board =
#[["8","3",".",".","7",".",".",".","."]
#,["6",".",".","1","9","5",".",".","."]
#,[".","9","8",".",".",".",".","6","."]
#,["8",".",".",".","6",".",".",".","3"]
#,["4",".",".","8",".","3",".",".","1"]
#,["7",".",".",".","2",".",".",".","6"]
#,[".","6",".",".",".",".","2","8","."]
#,[".",".",".","4","1","9",".",".","5"]
#,[".",".",".",".","8",".",".","7","9"]]
#Output: false
#Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

#Constraints:
#board.length == 9
#board[i].length == 9
#board[i][j] is a digit 1-9 or '.'.

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        h = True
        v = True
        c = True

        #h
        for i in board:
            stack = []
            for x in i:
                if x == ".":
                    continue
                elif x not in stack:
                    stack.append(x)
                    #print(x)
                else:
                    h = False

        #v
        indice = -1
        for y in range(9):
            indice = indice + 1
            for z in board:
                stack = []
                if z[indice] == ".":
                    continue
                elif z[indice] not in stack:
                    stack.append(z[indice])
                    #print(z[indice])
                else:
                    v = False

        #c
        os = -3
        of = 0
        for r in range(3):
            os = os + 3
            of = of + 3

            ps = -3
            pf = 0
            for w in range(3):
                ps = ps + 3
                pf = pf + 3

                stack = []
                for o in board[os:of]:
                    for p in o[ps:pf]:
                        if p == ".":
                            continue
                        elif p not in stack:
                            stack.append(p)
                            #print(p)
                        else:
                            c = False

        if h is True and v is True and c is True:
            return True
        else:
            return False

#Example 1:
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
#Output: true
print(Solution().isValidSudoku(board))

#Example 2:
board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
#Output: false
print(Solution().isValidSudoku(board))
