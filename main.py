figury = ["1","2","3","4","5","6","7","8","9"]
plansza = [1,2,3,4,5,6,7,8,9]
runda = 1
wynik = "Null"

def initGame(wynik, runda):
    while wynik == "Null":
        print("Runda: " + str(runda))
        display()
        boardUpdate(runda,validField(runda))
        wynik = gameStatusChck()
        runda += 1
    checkWinner(wynik)

def display():
    for pole in plansza:
        if (pole % 3 == 0):
            print(figury[pole - 1])
        else:
            print(figury[pole - 1], end='\t')

def userInput(runda):

    if(runda%2==0):
        nrPola = input("Gracz O podaj pole: ")
    else:
        nrPola = input("Gracz X podaj pole: ")
    return nrPola

def boardUpdate(runda, userInput):
    if (runda % 2 == 0):
        figury[userInput-1] = "O"
    else:
        figury[userInput-1] = "X"

def gameStatusChck():
    if(not all(element == 'X' for element in figury[0:3]) and not all(element == 'O' for element in figury[0:3])):
        if(not all(element == 'X' for element in figury[3:6]) and not all(element == 'O' for element in figury[3:6])):
            if(not all(element == 'X' for element in figury[6:10]) and not all(element == 'O' for element in figury[6:10])):
                if (not all(element == 'X' for element in figury[::3]) and not all(element == 'O' for element in figury[::3])):
                    if (not all(element == 'X' for element in figury[2::3]) and not all(element == 'O' for element in figury[2::3])):
                        if (not all(element == 'X' for element in figury[::4]) and not all(element == 'O' for element in figury[::4])):
                            if (not all(element == 'X' for element in figury[2:8:2]) and not all(element == 'O' for element in figury[2:8:2])):
                                return "Null"
                            else:
                                return figury[2]
                        else:
                            return figury[0]
                    else:
                        return figury[2]
                else:
                    return figury[0]
            else:
                return figury[6]
        else:
            return figury[3]
    else:
        return figury[0]

def checkWinner(wynik):
    if(wynik != "Null"):
        print("Wygral gracz: " + wynik)
    else:
        print("Remis")

def validField(runda):
    while True:
        numInput = int(userInput(runda))
        print("Pole: " + figury[numInput - 1])
        if (figury[numInput - 1] == "X" or figury[numInput - 1] == "O"):
            print("Pole jest juz zajete")
        else:
            print("OK")
            return numInput

initGame(wynik, runda)