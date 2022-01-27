"""
Tic Tac Toe Player. Compete with optimally playing AI. Impossible to win. Possible to tie
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
    """
    board_list = [item for elem in board for item in elem]    # Flatten the board to singluar list
    if not (X in board_list): return X                        # Inital state check when x starts
    if (board_list.count(O) < board_list.count(X)): return O  # Count number of X and O and determine next player
    else: return X                                            # By default X starts


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = []
    for i in range(0,3):
        for j in range(0,3):
            if board [i][j] == EMPTY:
                actions.append((i,j))
    actions = set(actions)
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i,j = action
    new = copy.deepcopy(board)

    if (new[i][j] != EMPTY): 
        raise Exception("Invalid Action")
    else:
        new[i][j] = player(board)
    return new


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    # Checking rows
    for i in range(0,3):
        if board[i].count(X) == 3: return X
        elif board[i].count(O) == 3: return O

    # Cheking columns (enjoy this manual code)
    column1 = [board[0][0],board[1][0],board[2][0]]
    column2 = [board[0][1],board[1][1],board[2][1]]
    column3 = [board[0][2],board[1][2],board[2][2]]
    columns = [column1, column2, column3]

    for column in columns:
        if column.count(X) == 3: return X
        elif column.count(O) == 3: return O

    # Cheking diagonals
    diagonal1 = [board[0][0],board[1][1],board[2][2]]
    diagonal2 = [board[0][2],board[1][1],board[2][0]]
    diagonals = [diagonal1, diagonal2]

    for diag in diagonals:
        if diag.count(X) == 3: return X
        elif diag.count(O) == 3: return O

    # Either no winner or draw
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if (winner(board) == X or winner(board) == O): return True   # If there is a winner
    elif not actions(board): return True                         # If there are no empty spaces
    else: return False                                           # No winner or board not full


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if (winner(board) == X): return 1
    elif (winner(board) == O): return -1
    else: return 0


def minmax_value(board, player):
    """
    Helper function for minimax function
    """
    if terminal(board): return utility(board)

    if (player == X):
        v = -math.inf
        for action in actions(board):
            v = max(v, minmax_value(result(board, action), O))
        return v
    else:
        v = math.inf
        for action in actions(board):
            v = min(v, minmax_value(result(board, action), X))
        return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    move = None

    # X is in turn
    if player(board) == X:
        v = -math.inf
        for action in actions(board):
            updated = minmax_value(result(board,action), O)
            if (updated > v):
                v = updated
                move = action

    # O is in turn
    else:
        v = math.inf
        for action in actions(board):
            updated = minmax_value(result(board,action), X)
            if (updated < v):
                v = updated
                move = action

    return move