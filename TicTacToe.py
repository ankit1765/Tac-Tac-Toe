#This program implements a one player TIC TAC TOE game.
#The program provides the user a choice of going first, or second,
#against the computer. The program develops "AI" by providing the computer
#with a set of instructions to follow so that it prioritizes winning first,
#and then blocking the user
#


import random
import time

def instruction ():
    print"\nWelcome to TIC-TAC-TOE"
    print"The board consists of a 3 X 3 BOARD with 9 possible position"
    print"Please review the numbers associated with the positions on the board"
    print"""
           _0_|_1_|_2_
           _3_|_4_|_5_
            6 | 7 | 8
                         """
################################################################################
def whogoesfirst ():
    answer = raw_input("Would you like to go first? (Y / N): ")

    while answer != "y" and answer != "n" and answer != "Y" and answer != "N":
        answer = raw_input("Would you like to go first? (Y / N): ")

    if answer.upper() == "Y":
        turn = 1
    else:
        turn = 0

    return turn #returns the string of player
################################################################################
def displayboard (board):
    print"\n\t_",board[0],"_|_",board[1],"_|_", board[2], "_"
    print  "\t_",board[3],"_|_",board[4],"_|_", board[5], "_"
    print  "\t ",board[6]," | ",board[7]," | ", board[8], " "
################################################################################
def dotcount ():
    print".",
    time.sleep(0.5)
    print".",
    time.sleep(0.5)
    print"."
################################################################################
def compdecision (board, compsymb, usersymb, turn):
    #In this table, the first 2 elements of each "row" are possible spots
    #where the computer must make an "obvious" decision, which is to choose the
    #3rd element position

    possibility =     [(board[0],board[1], 2), #1
                      (board[3],board[4], 5), #2
                      (board[6],board[7], 8), #3
                      (board[1],board[2], 0), #4
                      (board[4],board[5], 3), #5
                      (board[7],board[8], 6), #6
                      (board[0],board[3], 6), #7
                      (board[1],board[4], 7), #8
                      (board[2],board[5], 8), #9
                      (board[3],board[6], 0), #10
                      (board[4],board[7], 1), #11
                      (board[5],board[8], 2), #12
                      (board[0],board[4], 8), #13
                      (board[2],board[4], 6), #14
                      (board[6],board[4], 2), #15
                      (board[8],board[4], 0), #16
                      (board[0],board[8], 4), #17
                      (board[6],board[2], 4), #18
                      (board[0],board[6], 3), #19
                      (board[1],board[7], 4), #20
                      (board[2],board[8], 5), #21
                      (board[0],board[2], 1), #22
                      (board[6],board[8], 7), #23
                      (board[3],board[5], 4)] #24

    if turn == 1:
        possibility = possibility[::-1]
    if turn >= 2:
        possibility = [(board[5],board[8], 2), #12
                       (board[4],board[7], 1), #11
                       (board[0],board[4], 8), #13
                       (board[3],board[6], 0), #10
                       (board[2],board[4], 6), #14
                       (board[2],board[5], 8), #9
                       (board[6],board[4], 2), #15
                       (board[8],board[4], 0), #16
                       (board[2],board[8], 5), #21
                       (board[0],board[8], 4)] #17
        if turn == 3:
            possibility = possibility[::-1]

    row = -1
    for rows in possibility:
        row += 1
        count = 0
        for elements in rows:
            if elements == compsymb:
                count += 1
        if count == 2:
            return possibility[row][2]

    row = -1
    for rows in possibility:
        row += 1
        count = 0
        for elements in rows:
            if elements == usersymb:
                count += 1
        if count == 2:
            return possibility[row][2]

    return 1000
################################################################################
def checkwin (board):

    winning = ((board[0],board[1],board[2]),
               (board[3],board[4],board[5]),
               (board[6],board[7],board[8]),
               (board[0],board[3],board[6]),
               (board[1],board[4],board[7]),
               (board[2],board[5],board[8]),
               (board[0],board[4],board[8]),
               (board[2],board[4],board[6]),
               (board[2],board[4],board[6]),
               (board[0],board[1],board[2]),
               (board[3],board[4],board[5]),
               (board[6],board[7],board[8]))

    winner = "No Winner"

    for rows in winning:
        count = 0
        for elements in rows:
            if elements == "X":
                count += 1
        if count == 3:
            winner = "X"
            print"\nOh wow! You beat me! CONGRATS, YOU WIN!"
            return winner

    for rows in winning:
        count = 0
        for elements in rows:
            if elements == "O":
                count += 1
        if count == 3:
            winner = "O"
            print"\nAha! I got you there. I WIN"
            return winner

    count = 0
    for positions in board:
        if positions == "X" or positions == "O":
            count += 1
    if count == 9:
        winner = "TIE GAME!"
        print"\nIt's a draw! That was a good game. I want to do a rematch"
        return winner

    return winner

############################### MAIN BODY ##################################
def main():
    
    playagain = 0
    instruction() #PROVIDE INSTRUCTIONS TO USER

    while playagain == 0:

        board = [" ", " ", " ", " ", " ", " ", " ", " ", " "] #EMPTY BOARD
        check = checkwin (board) #CHECKS WINNER OR TIE. INITIALLY RETURNS NO WINNER
        whos_turn = whogoesfirst () #RETURN 1 IF PLAYER, RETURN 0 IF CP
        posused = [10,10,10,10,10,10,10,10,10,10,10,10,10,10, 10]
        #LIST OF POSITIONS USED. 10'S ARE PLACEHOLDERS. INITIALLY NO POSITIONS USED

        possiblepos = [0,1,2,3,4,5,6,7,8]

        if whos_turn == 1: #IF PLAYER IS "X" --> GOING FIRST
            while check == "No Winner":
                
                ################################ PLAYER TURN #######################
        
                pos = int(raw_input("\nEnter your choice of an unoccupied position? "))

                while pos in posused or pos not in possiblepos:
                    pos = int(raw_input("\nEnter your choice of an unoccupied position? "))

                board[pos] = "X" #PLACE X IN USERS CHOICE
                posused[pos] = pos #PUT THE POSITION ON POSUSED

                displayboard(board)

                check = checkwin (board) #CHECK WINNER OR TIED
                if check != "No Winner":
                    break

                dotcount() #COMPUTER IS THINKING AFFECT
                ############################### COMPUTER TURN ######################
                needtogenrandom = 1
                turn = 0
                #Priority winning (Looks for O's in a row first)
                obvipos = compdecision(board, "O", "X", turn)

                if obvipos < 9 and obvipos not in posused:
                    board[obvipos] = "O"
                    posused[obvipos] = obvipos
                    needtogenrandom = 0

                elif obvipos < 9 and obvipos in posused:

                    while obvipos < 9 and obvipos in posused and turn < 3:

                        turn += 1
                        obvipos = compdecision(board, "O", "X", turn)

                        if obvipos < 9 and obvipos not in posused:
                            board[obvipos] = "O"
                            posused[obvipos] = obvipos
                            needtogenrandom = 0
                            break

                if needtogenrandom == 1: #if nothing to win, try blocking
                #priority blocking
                #(Switch param 1 & 2, so it looks for X's in a row first)

                    turn = 0
                    obvipos = compdecision(board, "X", "O", turn)

                    if obvipos < 9 and obvipos not in posused:
                        board[obvipos] = "O"
                        posused[obvipos] = obvipos
                        needtogenrandom = 0

                    elif obvipos < 9 and obvipos in posused:

                        while obvipos < 9 and obvipos in posused and turn < 3:

                            turn += 1
                            obvipos = compdecision(board, "X", "O", turn)

                            if obvipos < 9 and obvipos not in posused:
                                board[obvipos] = "O"
                                posused[obvipos] = obvipos
                                needtogenrandom = 0
                                break

                #if no obvious answers, lets generate random pos
                if obvipos > 8 or needtogenrandom == 1:

                    comppos = random.randrange(9)
                    while comppos in posused:
                        comppos = random.randrange(9)

                    board[comppos] = "O"
                    posused[comppos] = comppos

                ####################### COMPUTER TURN OVER #########################
                displayboard(board)

                check = checkwin (board)
                if check != "No Winner":
                    break

        elif whos_turn == 0:

            while check == "No Winner":

                ############################### COMPUTER TURN ######################
                dotcount() #COMPUTER IS THINKING AFFECT
                needtogenrandom = 1
                turn = 0

                #Priority winning (Looks for O's in a row first)
                obvipos = compdecision(board, "O", "X", turn)

                if obvipos < 9 and obvipos not in posused:
                    board[obvipos] = "O"
                    posused[obvipos] = obvipos
                    needtogenrandom = 0

                elif obvipos < 9 and obvipos in posused:

                    while obvipos < 9 and obvipos in posused and turn < 3:

                        turn += 1
                        obvipos = compdecision(board, "O", "X", turn)

                        if obvipos < 9 and obvipos not in posused:
                            board[obvipos] = "O"
                            posused[obvipos] = obvipos
                            needtogenrandom = 0
                            break

                if needtogenrandom == 1:

                #if nothing to win, try blocking
                #priority blocking
                #(Switch param 1 & 2, so it looks for X's in a row first)

                    turn = 0
                    obvipos = compdecision(board, "X", "O", turn)

                    if obvipos < 9 and obvipos not in posused:
                        board[obvipos] = "O"
                        posused[obvipos] = obvipos
                        needtogenrandom = 0

                    elif obvipos < 9 and obvipos in posused:

                        while obvipos < 9 and obvipos in posused and turn < 3:

                            turn += 1
                            obvipos = compdecision(board, "X", "O", turn)

                            if obvipos < 9 and obvipos not in posused:
                                board[obvipos] = "O"
                                posused[obvipos] = obvipos
                                needtogenrandom = 0
                                break

                #No obvious choice, so lets generate random
                if obvipos > 8 or needtogenrandom == 1:

                    comppos = random.randrange(9)
                    while comppos in posused:
                        comppos = random.randrange(9)

                    board[comppos] = "O"
                    posused[comppos] = comppos

                ############################## COMPUTER TURN OVER ##################
                displayboard(board)

                check = checkwin (board)
                if check != "No Winner":
                    break
                ##############################PLAYER TURN ##########################

                pos = int(raw_input("\nEnter your choice of an unoccupied position? "))
                while pos in posused or pos not in possiblepos:
                    pos = int(raw_input("\nEnter your choice of an unoccupied position? "))

                board[pos] = "X" #PUT X ON USERS POSITION
                posused[pos] = pos #PUT POSITION IN POSUSED
                displayboard(board)

                check = checkwin (board) #CHECK WINNER
                if check != "No Winner":
                    break
                ##############################PLAYER TURN OVER#######################

        playagain = int(raw_input("\nENTER 0 FOR REMATCH, 1 TO QUIT: "))

        if playagain == 0:
            print"\n-----------------------------REMATCH-----------------------------\n"


main()
