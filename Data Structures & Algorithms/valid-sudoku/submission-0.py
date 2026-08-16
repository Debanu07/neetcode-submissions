class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        boxes=[set() for _ in range(9)]
        for r in range(9):
            for c in range(9):
                if board[r][c]==".":
                    continue
                num=board[r][c]
                box=(r//3)*3+(c//3)
                if num in boxes[box] or num in rows[r] or num in cols[c]:
                    return False
                boxes[box].add(num)
                rows[r].add(num)
                cols[c].add(num)
        return True