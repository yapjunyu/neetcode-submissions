class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row, square, col = defaultdict(list), defaultdict(list), defaultdict(list)
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num != ".":
                    if num in row[r] or num in col[c] or num in square[(r//3, c//3)]:
                        return False
                    row[r].append(num)
                    col[c].append(num)
                    square[(r//3, c//3)].append(num)
        return True
        