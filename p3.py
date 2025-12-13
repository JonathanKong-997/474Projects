import sys
import math

width = 20 #originally 14
height = 10 #originally 8

rows = [
    [(0, x) for x in range(9, 11)],
    [(1, x) for x in range(8, 12)],
    [(2, x) for x in range(7, 13)],
    [(3, x) for x in range(6, 14)],
    [(4, x) for x in range(5, 15)],
    [(5, x) for x in range(4, 16)],
    [(6, x) for x in range(3, 17)],
    [(7, x) for x in range(2, 18)],
    [(8, x) for x in range(1, 19)],
    [(9, x) for x in range(0, 20)],
]

columns = [
    [(x, 2) for x in range(7, 10)],
    [(x, 3) for x in range(6, 10)],
    [(x, 4) for x in range(5, 10)],
    [(x, 5) for x in range(4, 10)],
    [(x, 6) for x in range(3, 10)],
    [(x, 7) for x in range(2, 10)],
    [(x, 8) for x in range(1, 10)],
    [(x, 9) for x in range(0, 10)],
    [(x, 10) for x in range(0, 10)],
    [(x, 11) for x in range(1, 10)],
    [(x, 12) for x in range(2, 10)],
    [(x, 13) for x in range(3, 10)],
    [(x, 14) for x in range(4, 10)],
    [(x, 15) for x in range(5, 10)],
    [(x, 16) for x in range(6, 10)],
    [(x, 17) for x in range(7, 10)],
]
def valid_location(coords):
    if coords[0] < 0:
        return False
    #max col is 10 for row 0, 11 for row 1, etc
    elif coords[1] > 10+coords[0] or coords[1] > 9-coords[0]:
        return False
    return True
"""
diagonals = [
    [(2, 7), (3, 8), (4, 9)],
    [(3, 7), (4, 8), (5, 9)],
    [(14, 9), (15, 8), (16, 7)],
    [(15, 9), (16, 8), (17, 7)],

    [(3, 6), (4, 7), (5, 8), (6, 9)],
    [(4, 6), (5, 7), (6, 8), (7, 9)],
    [(12, 9), (13, 8), (14, 7), (15, 6)],
    [(13, 9), (14, 8), (15, 7), (16, 6)],

    [(4, 5), (5, 6), (6, 7), (7, 8), (8, 9)],
    [(5, 5), (6, 6), (7, 7), (8, 8), (9, 9)],
    [(10, 9), (11, 8), (12, 7), (13, 6), (14, 5)],
    [(11, 9), (12, 8), (13, 7), (14, 6), (15, 5)],

    [(5, 4), (6, 5), (7, 6), (8, 7), (9, 8), (10, 9)],
    [(6, 4), (7, 5), (8, 6), (9, 7), (10, 8), (11, 9)],
    [(8, 9), (9, 8), (10, 7), (11, 6), (12, 5), (13, 4)],
    [(9, 9), (10, 8), (11, 7), (12, 6), (13, 5), (14, 4)],

    [(6, 3), (7, 4), (8, 5), (9, 6), (10, 7), (11, 8), (12, 9)],
    [(6, 9), (7, 8), (8, 7), (9, 6), (10, 5), (11, 4), (12, 3)],
    [(7, 3), (8, 4), (9, 5), (10, 6), (11, 7), (12, 8), (13, 9)],
    [(7, 9), (8, 8), (9, 7), (10, 6), (11, 5), (12, 4), (13, 3)],

    [(4, 9), (5, 8), (6, 7), (7, 6), (8, 5), (9, 4), (10, 3), (11, 2)],
    [(5, 9), (6, 8), (7, 7), (8, 6), (9, 5), (10, 4), (11, 3), (12, 2)],
    [(7, 2), (8, 3), (9, 4), (10, 5), (11, 6), (12, 7), (13, 8), (14, 9)],
    [(8, 2), (9, 3), (10, 4), (11, 5), (12, 6), (13, 7), (14, 8), (15, 9)],

    [(2, 9), (3, 8), (4, 7), (5, 6), (6, 5), (7, 4), (8, 3), (9, 2), (10, 1)],
    [(3, 9), (4, 8), (5, 7), (6, 6), (7, 5), (8, 4), (9, 3), (10, 2), (11, 1)],
    [(8, 1), (9, 2), (10, 3), (11, 4), (12, 5), (13, 6), (14, 7), (15, 8), (16, 9)],
    [(9, 1), (10, 2), (11, 3), (12, 4), (13, 5), (14, 6), (15, 7), (16, 8), (17, 9)],

    [(0, 9), (1, 8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3), (7, 2), (8, 1), (9, 0)],
    [(1, 9), (2, 8), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3), (8, 2), (9, 1), (10, 0)],
    [(9, 0), (10, 1), (11, 2), (12, 3), (13, 4), (14, 5), (15, 6), (16, 7), (17, 8), (18, 9)],
    [(10, 0), (11, 1), (12, 2), (13, 3), (14, 4), (15, 5), (16, 6), (17, 7), (18, 8), (19, 9)]
]
"""
diagonals = []
for i in range(20):
    diagonals.append([])
    current = (9, i)
    while valid_location(current):
        diagonals[-1].append(current)
        current = (current[0] - 1, current[1] + 1)
    current = (9, i)
    while valid_location(current):  
        diagonals[-1].append(current)
        current = (current[0] - 1, current[1] - 1)

allLines = rows + columns + diagonals

def get_legal_moves(board, player):
    other_player = 3 - player
    legal_moves = set()
    for line in allLines:
        #print(f"testing line {line}")
        for i in range(len(line)):
            #print(f"i = {i}")
            if board[line[i][0]][line[i][1]] == 0 and line[i] not in legal_moves:
                #check if you could possibly play here; line has to be some number of other_player followed by player, no 0s allowed
                added = False
                #check 1: go forwards in the line if there are 2+ spaces remaining and next space can be flipped
                if i < len(line) - 2 and board[line[i+1][0]][line[i+1][1]] == other_player:
                    # go forwards in the line
                    for j in range(i+1, len(line)):
                        if board[line[j][0]][line[j][1]] == player:
                            added = True
                            legal_moves.add(line[i])
                            break
                        elif board[line[j][0]][line[j][1]] == 0:
                            break
                #check 2: if it wasn't already deemed legal, try going backwards
                if not added and i >= 2 and board[line[i-1][0]][line[i-1][1]] == other_player:
                    for j in range(i-1, -1, -1):
                        if board[line[j][0]][line[j][1]] == player:
                            added = True
                            legal_moves.add(line[i])
                            break
                        elif board[line[j][0]][line[j][1]] == 0:
                            break
    return legal_moves

directions = [
        (1, 0), (-1, 0), (0, 1), (0, -1),
        (1, 1), (-1, -1), (1, -1), (-1, 1)
]

def apply_move(board, player, position):
   # Validate the given position by scanning only from that position
    r, c = position
    opponent = 3 - player

    def is_on_board_local(row, col):
        return 0 <= row < height and 0 <= col < width and board[row][col] != -1

    # quick checks: must be on board and empty
    if not is_on_board_local(r, c) or board[r][c] != 0:
        return None

    total_flips = []
    for dr, dc in directions:
        flips = []
        row, col = r + dr, c + dc
        # collect contiguous opponent pieces in this direction
        while is_on_board_local(row, col) and board[row][col] == opponent:
            flips.append((row, col))
            row += dr
            col += dc
        # only valid if there's at least one opponent piece and it is terminated by player's piece
        if flips and is_on_board_local(row, col) and board[row][col] == player:
            total_flips.extend(flips)

    # if no flips in any direction, move is illegal
    if not total_flips:
        return None

    # apply move and flips on a copy
    new_board = [row[:] for row in board]
    new_board[r][c] = player
    for fr, fc in total_flips:
        new_board[fr][fc] = player
    return new_board

def count_value(board, value):
    unfilled = 0
    for row in board:
        unfilled += row.count(value)
    return unfilled

def evaluate_terminal(board, player):
    return count_value(board, player)

def minimax(board, player, maximizing_player, alpha, beta, depth):
    legal_moves = get_legal_moves(board, player)
    
    if depth == 0:
        return heuristic(board, maximizing_player), None
    
    #no legal moves for current player, skips
    if not legal_moves:
        opponent_moves = get_legal_moves(board, 3 - player)
        if not opponent_moves:
            return evaluate_terminal(board, maximizing_player), None
        return minimax(board, 3 - player, maximizing_player, alpha, beta, depth - 1)
    #maximize current player board
    if player == maximizing_player:
        best_score = -10**9
        best_move = None
        for move in legal_moves:
            new_board = apply_move(board, player, move)
            score, _ = minimax(new_board, 3 - player, maximizing_player, alpha, beta, depth - 1)
            if score > best_score:
                best_score = score
                best_move = move
            alpha = max(alpha, best_score)
            if beta <= alpha:
                break
        return best_score, best_move
    #minimize current player board (opponent's perspective)
    else:
        best_score = 10**9
        best_move = None
        for move in legal_moves:
            new_board = apply_move(board, player, move)
            score, _ = minimax(new_board, 3 - player, maximizing_player, alpha, beta, depth - 1)
            if score < best_score:
                best_score = score
                best_move = move
            beta = min(beta, best_score)
            if beta <= alpha:
                break
        return best_score, best_move

def heuristic(board, player):
    opponent = 3 - player
    score = 0

    corner_adjacent = {
    (9, 0): [(8, 1), (9, 1)],
    (9, 19): [(8, 18), (9, 18)],
    (0, 9): [(1, 8), (1, 9), (1, 10)],
    (0, 10): [(1, 9), (1, 10), (1, 11)]
    }

    for corner, adj_squares in corner_adjacent.items():
        r_c, c_c = corner
        if board[r_c][c_c] == 0:
            for r_a, c_a in adj_squares:
                if valid_location((r_a, c_a)):
                    if board[r_a][c_a] == player:
                        score -= 25  # small bonus for stable adjacent
                    elif board[r_a][c_a] == opponent:
                        score += 25
        else:
            if board[r_c][c_c] == player:
                score += 100
            else:
                score -= 100
    # Edge control heuristic
    edges_player = edges_opponent = 0
    for r in range(height):
        for c in range(width):
            if board[r][c] == -1:
                continue
            # consider bottom row and left/right triangle boundaries as edges
            if r == rows - 1 or c == 0 or c == (10 + r):
                if board[r][c] == player:
                    edges_player += 1
                elif board[r][c] == opponent:
                    edges_opponent += 1
    score += 20 * (edges_player - edges_opponent)

    #Mobility
    my_moves = len(get_legal_moves(board, player))
    opp_moves = len(get_legal_moves(board, opponent))
    score += 5 * (my_moves - opp_moves)

    my_pieces = count_value(board, player)
    opp_pieces = count_value(board, opponent)

    # Late-game parity bonus
    empty = count_value(board, 0)
    if empty < 25:
        score += 2 * (my_pieces - opp_pieces)
    else:
        score -= (my_pieces - opp_pieces)
    return score

def translate_coords(move):
    new_row = move[0] + 1
    new_col = move[1] + 1
    new_col -= 9-move[0]
    return [new_row, new_col]

def best_move(board, player):
    if count_value(board, 0) < 10:
        _, move = minimax(board, player, player, -10**9, 10**9, 20)
        return move
    else:
        _, move = minimax(board, player, player, -10**9, 10**9, 4)
        return move
    

# 1 = yours, 2 = opponents
if __name__ == "__main__":
    board = [ [-1] * width for _ in range(height) ]
    extras = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    vals = []
    while len(vals) < 110:
        vals += list(map(int, input().split()))
    
    k = 0
    for r in range(height):
        playable = 2 + 2 * extras[r]
        left = (width - playable) // 2
        right = left + playable - 1
        
        for c in range(width):
            if left <= c <= right:
                board[r][c] = vals[k]
                k += 1

    #print(board)
    best = translate_coords(best_move(board, 1))
    print(str(best[0]) + " " + str(best[1]))
