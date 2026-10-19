class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # keep hmap of rows, cols, and squares
        rmap, cmap, smap = defaultdict(list), defaultdict(list), defaultdict(list)
        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == ".":
                    continue
                square = (row // 3, col // 3)
                if val in rmap[row] or val in cmap[col] or val in smap[square]:
                    print(smap)
                    return False
                smap[square].append(val)
                rmap[row].append(val)
                cmap[col].append(val)
        return True
                

        