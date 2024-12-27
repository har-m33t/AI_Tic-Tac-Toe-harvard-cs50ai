"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    If the function returns False, it is X's turn, and True if it is O's turn
    """
    x = 0
    o = 0
    for row in board:
        x += row.count(X)
        o += row.count(O)
    return O if x > o else X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    moves = set()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                moves.add((i, j))
    return moves


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    copy_board = copy.deepcopy(board)
    if player(copy_board) == X:
        symbol = X
    else:
        symbol = O
    if (action[0] < 0 or action[0] > 2) or (action[1] < 0 or action[1] > 2):
        raise Exception('Out of bounds move')
    if copy_board[action[0]][action[1]] == EMPTY:
        copy_board[action[0]][action[1]] = symbol
    else:
        raise Exception('Space is Already Filled')
    return copy_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if utility(board) == 1:
        return X
    elif utility(board) == -1:
        return O
    else:
        return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    over = True
    for row in board:
        if EMPTY in row:
            over = False
    if check_win(board, X) or check_win(board, O):
        over = True
    return over


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if check_win(board, X):
        return 1
    elif check_win(board, O):
        return -1
    else:
        return 0


def check_win(board, symbol):
    """
    Checks if there is three in row of a symbol
    """
    # Checks Horizontally
    for i in range(len(board)):
        if board[i][0] == symbol and (board[i][0] == board[i][1] and board[i][0] == board[i][2]):
            return True
    # Checks Vertically
    for j in range(len(board)):
        if board[0][j] == symbol and (board[0][j] == board[1][j] and board[0][j] == board[2][j]):
            return True
    # Checks Diagonals
    if board[0][0] == symbol and (board[0][0] == board[1][1] and board[0][0] == board[2][2]):
        return True
    if board[2][0] == symbol and (board[2][0] == board[1][1] and board[2][0] == board[0][2]):
        return True
    return False


def minimax(board, alpha=-math.inf, beta=math.inf):
    """
    Returns the optimal action for the current player on the board.
    """
    best_move = None
    if not terminal(board):
        if player(board) == X:
            best_score = -math.inf
            for action in actions(board):
                v = min_value(result(board, action), alpha, beta)
                if v > best_score:
                    best_move = action
                    best_score = v
                alpha = max(alpha, best_score)
                if beta <= alpha:
                    break
        else:
            best_score = math.inf
            for action in actions(board):
                v = max_value(result(board, action), alpha, beta)
                if v < best_score:
                    best_move = action
                    best_score = v
                beta = min(beta, best_score)
                if beta <= alpha:
                    break
    return best_move


def max_value(board, alpha, beta):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_value(result(board, action), alpha, beta))
        alpha = max(alpha, v)
        if beta <= alpha:
            break

    return v


def min_value(board, alpha, beta):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_value(result(board, action), alpha, beta))
        beta = min(beta, v)
        if beta <= alpha:
            break
    return v
