
statement = """Welcome to the XOX game. The one who makes XOX first wins. \
Player X starts the game. Good luck."""

print(statement)

chart =["_",  "_",  "_",    "_",  "_",  "_",    "_",  "_",  "_" ]

def print_chart():
    print(chart[0:3], end = "\n")
    print(chart[3:6], end = "\n")
    print(chart[6:9], end = "\n")

def x_player():
    number = int(input("Which number would you like to put X on?: "))
    chart[number-1] = "X"
    return chart

def o_player():
    number = int(input("Which number would you like to put O on?: "))
    chart[number-1] = "O"
    return chart

def check_win(player):
    if chart[0] == player and chart[1] == player and chart[2] == player:
        return 1

    elif chart[3] == player and chart[4] == player and chart[5] == player:
        return 1

    elif chart[6] == player and chart[7] == player and chart[8] == player:
        return 1    

    elif chart[0] == player and chart[3] == player and chart[6] == player:
        return 1

    elif chart[2] == player and chart[5] == player and chart[8] == player:
        return 1    

    elif chart[0] == player and chart[4] == player and chart[8] == player:
        return 1

    elif chart[2] == player and chart[4] == player and chart[6] == player:
        return 1

    return -1

def main_loop():
    print("\n[1][2][3]\n[4][5][6]\n[7][8][9]\n")
    while True:
        print_chart()
        x_player()
        print_chart()
        if check_win("X") == 1:
            print("X won!")
            break

        o_player()
        print_chart()
        if check_win("O") == 1:
            print("O won!")
            break

main_loop()
