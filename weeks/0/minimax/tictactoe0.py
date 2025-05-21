# Tic Tac Toe using Minimax, No Alpha-Beta Pruning
import copy

player = "X" # player to play
opponent = "O" # opponent
board = [
    [" ", " ", " "], 
    [" ", " ", " "], 
    [" ", " ", " "]
] # board as a list of characters

def print_board(board):
    """Prints the board in a readable format."""
    print("------")
    for row in board:
        for cell in row:
            print(cell, end=" ")
        print()
    print("------")

def pl(s):
    """Returns the player to play next."""
    flat = [cell for row in s for cell in row]
    x_count = flat.count("X")
    o_count = flat.count("O")
    return "X" if x_count == o_count else "O"

def actions(s):
    """
    Returns the possible actions for the player.
    In a format of list[(row, column), (row, column), ...].
    """
    return [(i, j) for i in range(3) for j in range(3) if s[i][j] == " "]

def result(s, a):
    """
    Returns the result of applying action a to state s.
    In a format of list[(row, column), (row, column), ...].
    """
    i, j = a
    new_s = copy.deepcopy(s)
    new_s[i][j] = pl(s)
    return new_s

def terminal(s):
    # Rows, columns, diagonals
    for i in range(3):
        if s[i][0] == s[i][1] == s[i][2] != " ":
            return True
        if s[0][i] == s[1][i] == s[2][i] != " ":
            return True
    if s[0][0] == s[1][1] == s[2][2] != " ":
        return True
    if s[0][2] == s[1][1] == s[2][0] != " ":
        return True
    if all(cell != " " for row in s for cell in row):
        return True
    return False

def utility(s):
    for i in range(3):
        if s[i][0] == s[i][1] == s[i][2] != " ":
            return 1 if s[i][0] == player else -1
        if s[0][i] == s[1][i] == s[2][i] != " ":
            return 1 if s[0][i] == player else -1
    if s[0][0] == s[1][1] == s[2][2] != " ":
        return 1 if s[0][0] == player else -1
    if s[0][2] == s[1][1] == s[2][0] != " ":
        return 1 if s[0][2] == player else -1
    return 0

def value(s):
    """ Value of a board, assumes player is X """
    if terminal(s):
        return utility(s)
    turn = pl(s)
    if turn == player:
        return max(value(result(s, move)) for move in actions(s))
    else:
        return min(value(result(s, move)) for move in actions(s))

def best(s):
    """ assumes player is X """
    possible_moves = actions(s)
    move_values = []
    for move in possible_moves:
        move_val = value(result(s, move))
        move_values.append(move_val)
    # X is maximizing player
    return possible_moves[move_values.index(max(move_values))]

def user_readable_actions(s):
    possible_moves = actions(s)
    user_readable = []
    for move in possible_moves:
        user_readable.append(str(move[0] * 3 + move[1]))
    return user_readable

while True:
    # Do best move
    move = best(board)
    board[move[0]][move[1]] = player
    print_board(board)
    if terminal(board):
        print("Game over!")
        break

    # Let opponent (user) choose move
    opponent_move = input("Your move. Choose (0-8) ")
    if opponent_move not in user_readable_actions(board):
        while True:
            opponent_move = input("Invalid move. Choose (0-8) ")
            if opponent_move in user_readable_actions(board):
                break
    machine_readable_opponent_move = (int(opponent_move) // 3, int(opponent_move) % 3)
    board[machine_readable_opponent_move[0]][machine_readable_opponent_move[1]] = opponent
    print_board(board)
    if terminal(board):
        if utility(board) == 1:
            print("You lose...")
            print("Shake it off, Try again!")
            print("\t--Magnus Carlsen")
        elif utility(board) == -1:
            print("You win!")
            print("Congratulations! This AI is the best, and you defeated it!")
        else:
            print("It's a tie!")
            print("You played well! Try again, maybe you can win next time!")
        break

