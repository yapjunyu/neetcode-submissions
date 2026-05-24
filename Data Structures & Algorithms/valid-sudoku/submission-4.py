class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 3 hashmaps for the rows, columns and squares 
        # key to indentify square need to be a combination of row // 3, col // 3
        rows, cols, squares = defaultdict(set),  defaultdict(set),  defaultdict(set)
        for row in range(len(board)):
            for col in range(len(board[row])):
                val = board[row][col]
                if val == ".":
                    continue
                if val not in rows[row] and val not in cols[col] and val not in squares[(row // 3, col //3)]:
                    rows[row].add(val)
                    cols[col].add(val)
                    squares[(row //3, col //3)].add(val)
                else:
                    return False
        return True
                
        