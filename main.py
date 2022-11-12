fields = ["1","2","3","4","5","6","7","8","9"]
board = [1,2,3,4,5,6,7,8,9]
round = 1
winner = "Null"

def init_game(winner, round):
    while winner == "Null":
        print("Round: " + str(round))
        display()
        board_update(round,valid_field(round))
        winner = game_status_chck()
        round += 1
    check_winner(winner)

def display():
    for pole in board:
        if (pole % 3 == 0):
            print(fields[pole - 1])
        else:
            print(fields[pole - 1], end='\t')

def user_input(round):

    if(round%2==0):
        field_number = input("Player O enter the field: ")
    else:
        field_number = input("Player X enter the field: ")
    return field_number

def board_update(round, user_input):
    if (round % 2 == 0):
        fields[user_input-1] = "O"
    else:
        fields[user_input-1] = "X"

def game_status_chck():
    if(not all(element == 'X' for element in fields[0:3]) and not all(element == 'O' for element in fields[0:3])):
        if(not all(element == 'X' for element in fields[3:6]) and not all(element == 'O' for element in fields[3:6])):
            if(not all(element == 'X' for element in fields[6:10]) and not all(element == 'O' for element in fields[6:10])):
                if (not all(element == 'X' for element in fields[::3]) and not all(element == 'O' for element in fields[::3])):
                    if (not all(element == 'X' for element in fields[2::3]) and not all(element == 'O' for element in fields[2::3])):
                        if (not all(element == 'X' for element in fields[::4]) and not all(element == 'O' for element in fields[::4])):
                            if (not all(element == 'X' for element in fields[2:8:2]) and not all(element == 'O' for element in fields[2:8:2])):
                                return "Null"
                            else:
                                return fields[2]
                        else:
                            return fields[0]
                    else:
                        return fields[2]
                else:
                    return fields[0]
            else:
                return fields[6]
        else:
            return fields[3]
    else:
        return fields[0]

def check_winner(winner):
    if(winner != "Null"):
        print("Player " + winner + " won!")
    else:
        print("Draw!!!")

def valid_field(round):
    while True:
        numInput = int(user_input(round))
        if (fields[numInput - 1] == "X" or fields[numInput - 1] == "O"):
            print("This field is already taken!")
        else:
            return numInput

init_game(winner, round)