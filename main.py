from itertools import product
import numpy as np

def count_bingo(board, numbers):
    mark_maps = np.full([len(board), len(board)], False).astype(bool)

    numbers += [0] # 0を追加
    for num in numbers:
        for i, j in product(range(len(board)), range(len(board))):
            if board[i][j] == num:
                mark_maps[i, j] = True
                break
    
    line_count = 0
    for i in range(len(board)):
        if all(mark_maps[i, :]): # 横判定
            line_count += 1
    
        if all(mark_maps[:, i]): # 縦判定
            line_count += 1

    # 斜め/右下
    pos_array = [[i, i] for i in range(len(board))]
    if all([mark_maps[pos[0], pos[1]] for pos in pos_array]):
        line_count += 1
    
    pos_array2 = [[i, len(board) - i - 1] for i in range(len(board))]
    if all([mark_maps[pos[0], pos[1]] for pos in pos_array2]):
        line_count += 1

    return line_count




N, K = [int(c) for c in input().split()]
board = [[int(c) for c in input().split()] for _ in range(N)]
numbers = [int(c) for c in input().split()]

print(count_bingo(board, numbers))
