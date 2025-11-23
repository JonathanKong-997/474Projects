import sys
import math
# I am in a group with Jonathan Kong, Arthur Perng, and Rishi 
#program should look through all legal moves of a player 

#cells are horizontal, vertical
#cells are column, row

#Look - up table
rows = [
    [(0, x) for x in range(3, 11)],
    [(1, x) for x in range(2, 12)],
    [(2, x) for x in range(1, 13)],
    [(3, x) for x in range(0, 14)],
    [(4, x) for x in range(0, 14)],
    [(5, x) for x in range(1, 13)],
    [(6, x) for x in range(2, 12)],
    [(7, x) for x in range(3, 11)],
]
columns = [
    [(x, 0) for x in range(3, 5)],
    [(x, 1) for x in range(2, 6)],
    [(x, 2) for x in range(1, 7)],
    [(x, 3) for x in range(8)],
    [(x, 4) for x in range(8)],
    [(x, 5) for x in range(8)],
    [(x, 6) for x in range(8)],
    [(x, 7) for x in range(8)],
    [(x, 8) for x in range(8)],
    [(x, 9) for x in range(8)],
    [(x, 10) for x in range(8)],
    [(x, 11) for x in range(1, 7)],
    [(x, 12) for x in range(2, 6)],
    [(x, 13) for x in range(3, 5)],
]
diagonals = [
    [(4, 0), (5, 1), (6, 2), (7, 3)],
    [(3, 0), (4, 1), (5, 2), (6, 3), (7, 4)],
    [(3, 1), (4, 2), (5, 3), (6, 4), (7, 5)],
    [(2, 1), (3, 2), (4, 3), (5, 4), (6, 5), (7, 6)],
    [(2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)],
    [(1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)],
    [(1, 3), (2, 4), (3, 5), (4, 6), (5, 7), (6, 8), (7, 9)],
    [(0, 3), (1, 4), (2, 5), (3, 6), (4, 7), (5, 8), (6, 9), (7, 10)],
    [(0, 4), (1, 5), (2, 6), (3, 7), (4, 8), (5, 9), (6, 10)],
    [(0, 5), (1, 6), (2, 7), (3, 8), (4, 9), (5, 10), (6, 11)],
    [(0, 6), (1, 7), (2, 8), (3, 9), (4, 10), (5, 11)],
    [(0, 7), (1, 8), (2, 9), (3, 10), (4, 11), (5, 12)],
    [(0, 8), (1, 9), (2, 10), (3, 11), (4, 12)],
    [(0, 9), (1, 10), (2, 11), (3, 12), (4, 13)],
    [(0, 10), (1, 11), (2, 12), (3, 13)],

    [(0, 3), (1, 2), (2, 1), (3, 0)],
    [(0, 4), (1, 3), (2, 2), (3, 1), (4, 0)],
    [(0, 5), (1, 4), (2, 3), (3, 2), (4, 1)],
    [(0, 6), (1, 5), (2, 4), (3, 3), (4, 2), (5, 1)],
    [(0, 7), (1, 6), (2, 5), (3, 4), (4, 3), (5, 2)],
    [(0, 8), (1, 7), (2, 6), (3, 5), (4, 4), (5, 3), (6, 2)],
    [(0, 9), (1, 8), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3)],
    [(0, 10), (1, 9), (2, 8), (3, 7), (4, 6), (5, 5), (6, 4), (7, 3)],
    [(1, 10), (2, 9), (3, 8), (4, 7), (5, 6), (6, 5), (7, 4)],
    [(1, 11), (2, 10), (3, 9), (4, 8), (5, 7), (6, 6), (7, 5)],
    [(2, 11), (3, 10), (4, 9), (5, 8), (6, 7), (7, 6)],
    [(2, 12), (3, 11), (4, 10), (5, 9), (6, 8), (7, 7)],
    [(3, 12), (4, 11), (5, 10), (6, 9), (7, 8)],
    [(3, 13), (4, 12), (5, 11), (6, 10), (7, 9)],
    [(4, 13), (5, 12), (6, 11), (7, 10)]
]

allLines = rows+columns+diagonals

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
                #check 2: if it wasn't already deemed legal, try going backwards
                if not added and i >= 2 and board[line[i-1][0]][line[i-1][1]] == other_player:
                    for j in range(i-1, -1, -1):
                        if board[line[j][0]][line[j][1]] == player:
                            added = True
                            legal_moves.add(line[i])
                            break
    return legal_moves

empty_squares = {0:3, 1:2, 2:1, 3:0, 4:0, 5:1, 6:2, 7:3}
def translate_coords(coords):
    # Translates the coordinates from what would be on a grid to the output format asked.
    # In the output format, (1, 1) refers to the leftmost green square in the first row. This would be (0, 3) in our model.
    new_row = coords[0] + 1
    new_col = coords[1] - empty_squares[coords[0]] + 1
    return (new_row, new_col)

directions = [
        (1, 0), (-1, 0), (0, 1), (0, -1),
        (1, 1), (-1, -1), (1, -1), (-1, 1)
]

def apply_move(board, player, position):

    legal_moves = get_legal_moves(board, player)
    if position not in legal_moves:
        return None  

    new_board = [row[:] for row in board]
    opponent = 3 - player

    r, c = position
    new_board[r][c] = player

    def is_on_board(row, col):
        return 0 <= row < 8 and 0 <= col < 14 and new_board[row][col] != -1

    for dr, dc in directions:
        flips = []
        row, col = r + dr, c + dc
        while is_on_board(row, col) and new_board[row][col] == opponent:
            flips.append((row, col))
            row += dr
            col += dc
        if flips and is_on_board(row, col) and new_board[row][col] == player:
            for fr, fc in flips:
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

def stable(board, player):
    pass

def heuristic(board, player): 
    #MAJORITY OF THE GRADE
    value = 0
    my_moves = len(get_legal_moves(board, player))
    opp_moves = len(get_legal_moves(board, 3 - player))

    corners = [(0,3), (0, 10), (3, 0), (4,0), (3,13), (4,13), (7,3), (7, 10)]
    my_corners = 0
    opp_corners = 0
    for (r,c) in corners:
        if board[r][c] == player:
            my_corners += 1
        elif board[r][c] == 3 - player:
            opp_corners += 1

    my_frontier = 0
    opp_frontier = 0

    for r in range(8):
        for c in range(14):
            if board[r][c] <= 0: continue
            is_frontier = any(
                0 <= r+dr < 8 and 0 <= c+dc < 14 and board[r+dr][c+dc] == 0
                for (dr,dc) in directions
            )
            if is_frontier:
                if board[r][c] == player:
                    my_frontier += 1
                elif board[r][c] == 3-player:
                    opp_frontier += 1
    
    mine = count_value(board, player)
    theirs = count_value(board, 3 - player)

    value += 100 * (my_moves - opp_moves)
    value += 150 * (my_corners - opp_corners)
    value -= 50 * (my_frontier - opp_frontier)
    value += (mine - theirs)
    return value

def best_move(board, player):
    if count_value(board, 0) < 14:
        _, move = minimax(board, player, player, -10**9, 10**9, 20)
        return move
    else:
        _, move = minimax(board, player, player, -10**9, 10**9, 4)
        return move

# 1 = yours, 2 = opponents
if __name__ == "__main__":
    board = [ [-1] * 14 for _ in range(8) ]
    extras = [0,1,2,3,3,2,1,0]

    vals = []
    while len(vals) < 88:
        vals += list(map(int, input().split()))
    
    k = 0
    for r in range(8):
        playable = 8 + 2 * extras[r]
        left = (14 - playable) // 2
        right = left + playable - 1
        
        for c in range(14):
            if left <= c <= right:
                board[r][c] = vals[k]
                k += 1
    
    best = translate_coords(best_move(board, 1))
    print(str(best[0]) + " " + str(best[1]))
