class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            row_hashset = set()
            for j in range(9):
                if board[i][j] == ".":
                    continue
                num = int(board[i][j])
                if num not in row_hashset:
                    row_hashset.add(num)
                else:
                    return False
        
        for j in range(9):
            col_hashset = set()
            for i in range(9):
                if board[i][j] == ".":
                    continue
                num = int(board[i][j])
                if num not in col_hashset:
                    col_hashset.add(num)
                else: 
                    return False
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                box_hashset = set()
                for box_row in range(3):
                    for box_col in range(3):
                        num = board[box_row + i][box_col + j]
                        if num == ".":
                            continue
                        if num in box_hashset:
                            return False
                        box_hashset.add(num)
        
        return True


        






        