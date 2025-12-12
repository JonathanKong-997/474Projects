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
    elif coords[1] > 10+coords[0]:
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
    """Simple heuristic for triangular board. Does not call global
    get_legal_moves to avoid board-shape indexing issues.
    """
    opponent = 3 - player
    score = 0

    # Material (piece difference)
    my_pieces = count_value(board, player)
    opp_pieces = count_value(board, opponent)
    score += 10 * (my_pieces - opp_pieces)

    # Corner values (only if valid on this board)
    corners = [(0, 9), (height - 1, 0), (height - 1, width - 1)]
    rows = len(board)
    cols = len(board[0]) if rows > 0 else 0
    for r, c in corners:
        if 0 <= r < rows and 0 <= c < cols and board[r][c] != -1:
            if board[r][c] == player:
                score += 50
            elif board[r][c] == opponent:
                score -= 50

    # Edge control heuristic
    edges_player = edges_opponent = 0
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == -1:
                continue
            # consider bottom row and left/right triangle boundaries as edges
            if r == rows - 1 or c == 0 or c == (10 + r):
                if board[r][c] == player:
                    edges_player += 1
                elif board[r][c] == opponent:
                    edges_opponent += 1
    score += 5 * (edges_player - edges_opponent)

    # Late-game parity bonus
    empty = count_value(board, 0)
    if empty < 12:
        score += 2 * (my_pieces - opp_pieces)

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
    

# ==========================================
# 4. GAME PLAY / UI
# ==========================================

def print_board_readable(board):
    # Adapted for triangular board: width x height (20x10)
    cols = len(board[0])
    rows = len(board)
    print("\n   " + "".join([f"{c:2}" for c in range(cols)]))  # Column headers
    print("   " + "-" * (cols * 2))
    for r in range(rows):
        row_str = f"{r:2}|"  # Row header
        for c in range(cols):
            val = board[r][c]
            if val == -1:
                row_str += "  "  # Hide invalid squares
            elif val == 0:
                row_str += " ."
            elif val == 1:
                row_str += " X"  # Player 1
            elif val == 2:
                row_str += " O"  # Player 2
        print(row_str)
    print()

def play_game():
    print("Initializing Octagon Reversi...")
    # 1. Initialize the empty triangular board (height=10, width=20)
    board = [[-1] * width for _ in range(height)]

    # Define triangular playable rows (increasing playable cells per row)
    extras = list(range(height))  # 0,1,2,...,height-1
    for r in range(height):
        playable = 2 + 2 * extras[r]
        left = (width - playable) // 2
        right = left + playable - 1
        for c in range(width):
            if left <= c <= right:
                board[r][c] = 0

    # 2. Set Starting Position (placed near the triangular center)
    mid_row_top = height // 2 - 1
    mid_row_bottom = height // 2
    # compute center columns for those rows
    playable_top = 2 + 2 * extras[mid_row_top]
    left_top = (width - playable_top) // 2
    center_top = left_top + playable_top // 2

    playable_bottom = 2 + 2 * extras[mid_row_bottom]
    left_bottom = (width - playable_bottom) // 2
    center_bottom = left_bottom + playable_bottom // 2

    # Place four starting pieces in a small cross around the triangle center
    board[mid_row_top][center_top] = 2
    board[mid_row_top][center_top + 1] = 1
    board[mid_row_bottom][center_bottom] = 1
    board[mid_row_bottom][center_bottom + 1] = 2

    human_player = 1  # You are X
    bot_player = 2    # Bot is O

    turn = 1  # 1 starts

    while True:
        print_board_readable(board)

        # Local, board-shape-robust legal-move scanner (shadows global)
        def local_get_legal_moves(bd, player):
            other_player = 3 - player
            legal = set()
            rows = len(bd)
            cols = len(bd[0]) if rows > 0 else 0

            def on_board(rr, cc):
                return 0 <= rr < rows and 0 <= cc < cols and bd[rr][cc] != -1

            for rr in range(rows):
                for cc in range(cols):
                    if bd[rr][cc] != 0:
                        continue
                    valid = False
                    for dr, dc in directions:
                        r2, c2 = rr + dr, cc + dc
                        # first cell must be opponent
                        if not on_board(r2, c2) or bd[r2][c2] != other_player:
                            continue
                        # advance through opponents
                        while on_board(r2, c2) and bd[r2][c2] == other_player:
                            r2 += dr
                            c2 += dc
                        if on_board(r2, c2) and bd[r2][c2] == player:
                            valid = True
                            break
                    if valid:
                        legal.add((rr, cc))
            return legal

        legal_moves = local_get_legal_moves(board, turn)

        # Check for Game Over (Neither player can move)
        if not legal_moves and not local_get_legal_moves(board, 3 - turn):
            print("GAME OVER")
            p1_score = count_value(board, 1)
            p2_score = count_value(board, 2)
            print(f"Final Score - You: {p1_score} | Bot: {p2_score}")
            if p1_score > p2_score:
                print("You Win!")
            elif p2_score > p1_score:
                print("Bot Wins!")
            else:
                print("Draw!")
            break

        # Check for Pass
        if not legal_moves:
            print(f"Player {turn} has no moves! Passing...")
            turn = 3 - turn
            continue

        if turn == human_player:
            print(f"Your Turn (X). Legal moves: {list(legal_moves)}")
            while True:
                try:
                    user_input = input("Enter row and col (e.g., '3 5'): ")
                    if not user_input:
                        continue
                    r, c = map(int, user_input.split())
                    if (r, c) in legal_moves:
                        board = apply_move(board, turn, (r, c))
                        break
                    else:
                        print("Illegal move. Try again.")
                except ValueError:
                    print("Invalid format. Use 'row col'.")
        else:
            print("Bot (O) is thinking...")
            # Use local scanner for bot move selection (avoid global minimax/get_legal_moves)
            bot_legal = local_get_legal_moves(board, turn)
            if not bot_legal:
                print("Bot has no move (passing).")
                turn = 3 - turn
                continue

            # Bot: prefer using the provided global `get_legal_moves` implementation.
            try:
                bot_legal = get_legal_moves(board, turn)
            except Exception as exc:
                print(f"Warning: global get_legal_moves failed ({exc}); falling back to local scanner.")
                bot_legal = local_get_legal_moves(board, turn)

            if not bot_legal:
                print("Bot has no move (passing).")
                turn = 3 - turn
                continue

            # Use provided heuristic to choose the best move among legal options.
            best_move_choice = None
            best_score = None
            best_result_board = None
            for mv in bot_legal:
                candidate = apply_move(board, turn, mv)
                if candidate is None:
                    continue
                # Primary ranking: heuristic(candidate, bot_player)
                # Secondary tie-break: material count (number of bot pieces)
                h = heuristic(candidate, bot_player)
                t = count_value(candidate, bot_player)
                # form tuple for comparison
                score = (h, t)
                if best_score is None or score > best_score:
                    best_score = score
                    best_move_choice = mv
                    best_result_board = candidate

            if best_move_choice is None:
                # defensive: no valid candidate moves (shouldn't happen), pass
                print("No valid bot moves after validation; passing.")
                turn = 3 - turn
                continue
            print(f"Bot plays at: {best_move_choice} (heuristic={best_score[0]}, pieces={best_score[1]})")
            board = best_result_board

        turn = 3 - turn

if __name__ == "__main__":
    play_game()
