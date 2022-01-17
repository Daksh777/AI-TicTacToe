print("Possible moves are: \n")
print(' 1 |  2  | 3 ')
print('-------------')
print(' 4 |  5  | 6 ')
print('-------------')
print(' 7 |  8  | 9 ')

board = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

player = "O"
bot = "X"

def PrintBoard(board):
    print(f' {board[1]} |  {board[2]}  | {board[3]} ')
    print('-------------')
    print(f' {board[4]} |  {board[5]}  | {board[6]} ')
    print('-------------')
    print(f' {board[7]} |  {board[8]}  | {board[9]} ')

print("\nCurrent board: \n")
PrintBoard(board)

def SpaceIsFree(position):
    if board[position] == ' ':
        return True
    else:
        return False

def GameIsDraw():
    for key in board.keys():
        if board[key] == " ":
            return False
    else:
        return True

def GameIsWon():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False

def WinnerIs(user):
    if (board[1] == board[2] and board[1] == board[3] and board[1] == user):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == user):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == user):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == user):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == user):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == user):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == user):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == user):
        return True
    else:
        return False

def InsertLetter(position, letter):
    if SpaceIsFree(position):
        board[position] = letter
        if GameIsDraw():
            PrintBoard(board)
            print("\nDraw")
            exit()

        elif GameIsWon():
            if letter == "X":
                print("Computer plays: ")
                PrintBoard(board)
                print("\nComputer wins")
                exit()
            else:
                PrintBoard(board)
                print("\nUser wins")
                exit()
    else:
        position = int(input("Position not free, try again: "))
        InsertLetter(position, letter)
        return
    
def Player1Move():
    position = int(input("Enter position for O: "))
    print("\n")
    InsertLetter(position, player)
    PrintBoard(board)
    print("\n")
    return

def minimax(board, isMaximizing):
    if WinnerIs(bot):
        return 1
    elif WinnerIs(player):
        return -1
    elif GameIsDraw():
        return 0

    if isMaximizing:
        bestScore = -800
        for key in board.keys():
            if board[key] == ' ':
                board[key] = bot
                score = minimax(board, False)
                board[key] = ' '
                if score > bestScore:
                    bestScore = score
        return bestScore

    else:
        bestScore = 800
        for key in board.keys():
            if board[key] == ' ':
                board[key] = player
                score = minimax(board, True)
                board[key] = ' '
                if score < bestScore:
                    bestScore = score
        return bestScore


def CompMove():
    bestScore = -800
    bestMove = 0
    for key in board.keys():
        if board[key] == ' ':
            board[key] = bot
            score = minimax(board, False)
            board[key] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = key
    
    InsertLetter(bestMove, bot)
    print("Computer plays: ")
    print("\n")
    PrintBoard(board)
    print("\n")
    return
    

while not GameIsWon():
    CompMove()
    Player1Move()