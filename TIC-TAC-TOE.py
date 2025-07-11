#TIC-TAC-TOE AI
#Developed by Pavithra Praveen as part of CodSoft AI Internship


import math

#Function to show the board
def show_board(brd):
    for row in brd:
        print(" | ".join(row))
        print("-" * 5)

#Function to check winner
def check_winner(brd):
    # Check rows
    for row in brd:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]
    #Check columns
    for c in range(3):
        if brd[0][c] == brd[1][c] == brd[2][c] and brd[0][c] != " ":
            return brd[0][c]
    #Check diagonals
    if brd[0][0] == brd[1][1] == brd[2][2] and brd[0][0] != " ":
        return brd[0][0]
    if brd[0][2] == brd[1][1] == brd[2][0] and brd[0][2] != " ":
        return brd[0][2]
    return None

#Check if all cells are filled
def is_draw(brd):
    for row in brd:
        for cell in row:
            if cell == " ":
                return False
    return True

#Minimax logic for AI
def minimax(brd, is_ai):
    winner = check_winner(brd)
    if winner == "O":
        return 1
    elif winner == "X":
        return -1
    elif is_draw(brd):
        return 0

    if is_ai:
        best = -math.inf
        for i in range(3):
            for j in range(3):
                if brd[i][j] == " ":
                    brd[i][j] = "O"
                    score = minimax(brd, False)
                    brd[i][j] = " "
                    best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(3):
            for j in range(3):
                if brd[i][j] == " ":
                    brd[i][j] = "X"
                    score = minimax(brd, True)
                    brd[i][j] = " "
                    best = min(best, score)
        return best

#AI move logic
def find_best_move(brd):
    best_score = -math.inf
    move = None
    for i in range(3):
        for j in range(3):
            if brd[i][j] == " ":
                brd[i][j] = "O"
                score = minimax(brd, False)
                brd[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

#Main function
def start_game():
    brd = [[" " for _ in range(3)] for _ in range(3)]
    print("Tic Tac Toe Game\nYou are X | AI is O\n")
    show_board(brd)

    while True:
        #Player move
        while True:
            try:
                #I wrote this part to handle user input
                r = int(input("Enter row (0-2): "))
                c = int(input("Enter column (0-2): "))
                if brd[r][c] == " ":
                    brd[r][c] = "X"
                    break
                else:
                    print("This spot is taken, try again.")
            except:
                print("Invalid input. Please enter numbers 0 to 2.")

        show_board(brd)

        if check_winner(brd):
            print("You win!")
            break
        if is_draw(brd):
            print("Match Drawn.")
            break

        #AI move
        ai_r, ai_c = find_best_move(brd)
        brd[ai_r][ai_c] = "O"
        print("\nAI played:")
        show_board(brd)

        if check_winner(brd):
            print("AI wins!")
            break
        if is_draw(brd):
            print("Match Drawn.")
            break

#Start the game
start_game()
