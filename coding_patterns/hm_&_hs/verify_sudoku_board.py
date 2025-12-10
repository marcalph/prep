from typing import List

def verify_sudoku_board(board: List[List[int]]) -> bool:
    # Write your code here
    from collections import defaultdict
    rowz, colz,  squarz = defaultdict(set),defaultdict(set),defaultdict(set)
    for i in range(len(board)):
        for j in range(len(board[0])):
            if (val:=board[i][j]) !=0:
                if val in rowz[i]:
                    return False
                rowz[i].add(board[i][j])
                if val in colz[j]:
                    return False
                colz[j].add(board[i][j])
                if val in squarz[(i // 3) * 3 + (j // 3)]:
                    return False
                squarz[(i // 3) * 3 + (j // 3)].add(board[i][j])
    return True