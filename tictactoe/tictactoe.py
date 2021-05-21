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
    x_moves = sum(x.count("X") for x in board)
    o_moves = sum(x.count("O") for x in board)
    if not terminal(board):
      if x_moves > o_moves :
        return O
      else :
        return X
    else:
        return None

    """
    Returns player who has the next turn on a board.
    """




def actions(board):

    set_of_actions = set()

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                set_of_actions.add((i, j))
    return set_of_actions


def result(board, action):

    if terminal(board):
        raise ValueError("Game over.")
    elif action not in actions(board):
        raise ValueError("Invalid action.")
    else:
        player_who_moves = player(board)
        result_board = copy.deepcopy(board)
        (i, j) = action
        result_board[i][j] = player_who_moves


    return result_board





def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    A = board[0]
    B = board[1]
    C = board[2]

    if A.count("X") == 3 or B.count("X") == 3 or C.count("X") == 3:
        return X
    elif A.count("O") == 3 or B.count("O") == 3 or C.count("O") == 3:
        return O
    elif A[0] == B[0] and A[0] == C[0]:
        if A[0] == X:
            return X
        elif A[0] == O:
            return O
    elif A[1] == B[1] and A[1] == C[1]:
        if A[1] == X:
            return X
        elif A[1] == O:
            return O
    elif A[2] == B[2] and A[2] == C[2]:
        if A[2] == X:
            return X
        elif A[2] == O:
            return O
    elif A[0] == B[1] and A[0] == C[2]:
        if A[0] == X:
            return X
        elif A[0] == O:
            return O
    elif A[2] == B[1] and A[2] == C[0]:
        if A[2] == X:
            return X
        elif A[2] == O:
            return O
    else:
        return None




def terminal(board):

    empty_count= sum(x.count(EMPTY) for x in board)
    if empty_count == 0 or winner(board) is not None:
        return True
    else:
        return False

    """
    Returns True if game is over, False otherwise.
    """



def utility(board):

   if terminal(board) is True:
     if winner(board) == X:
       return 1
     elif winner(board) == O:
       return -1
     else:
       return 0



def maxValue(board):
       if terminal(board):
           return utility(board)
       v = -math.inf
       for action in actions(board):
           v = max(v, minValue(result(board, action)))

       return v


def minValue(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, maxValue(result(board, action)))

    return v


def minimax(board):
       """
       Returns the optimal action for the current player on the board.
       """
       player_moving = player(board)


       if board == [[EMPTY] * 3] * 3:
           return (0, 0)

       if player_moving == X:
           value = -math.inf
           selected_action = None
           for action in actions(board):
               minValueResult = minValue(result(board, action))
               if minValueResult > value:
                   value = minValueResult
                   selected_action = action
       elif player_moving == O:
           value = math.inf
           selected_action = None
           for action in actions(board):
               maxValueResult = maxValue(result(board, action))
               if maxValueResult < value:
                   value = maxValueResult
                   selected_action = action

       return selected_action










