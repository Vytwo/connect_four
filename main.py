
import colorama
from colorama import Fore
import art #zmagovalni napisi
import os #clear/ocisti screen
import sys
colorama.init(autoreset=True) #barvni text


#matrix
board = [
    [" "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "],
    [" "," "," "," "," "," "," "],
]
valid_choices = ["1","2","3","4","5","6","7"]
end = False
current = "blue"
yellow_four = f"{Fore.YELLOW}O{Fore.WHITE}{Fore.YELLOW}O{Fore.WHITE}{Fore.YELLOW}O{Fore.WHITE}{Fore.YELLOW}O{Fore.WHITE}"
blue_four = f"{Fore.BLUE}O{Fore.WHITE}{Fore.BLUE}O{Fore.WHITE}{Fore.BLUE}O{Fore.WHITE}{Fore.BLUE}O{Fore.WHITE}"


def switch(current):
    os.system("cls")
    if current == "yellow":
        return "blue"
    if current == "blue":
        return "yellow"
#
def display(board):
    for i in board:
        print("|" + "|".join(i) + "|")
    print(" 1 2 3 4 5 6 7")


#poteze modrega/rumenega
def handleturn(current):
    global board
    display(board)
    temp = -1
    player_input = None
    print(f"\tIt is {current}'s turn")
    while player_input not in valid_choices:
        player_input = input("Enter your choice:")
    player_input = int(player_input) - 1
    while True:
        if temp == -7:
            handleturn(current)
        if board[temp][player_input] == " ":
            if current == "yellow":
                board[temp][player_input] = f"{Fore.YELLOW}O{Fore.WHITE}"
            if current == "blue":
                board[temp][player_input] = f"{Fore.BLUE}O{Fore.WHITE}"
            break 
        else:
            temp -= 1

#preveri ali je kdo zmagal    
def check():
    global board
    global end
    for i in range(6):
        for j in range(7):
            
            #horizontali
            if j+3 <= 6:
                if board[i][j] + board[i][j+1] + board[i][j+2] + board[i][j+3] == yellow_four:
                    end = True
                    os.system("cls")
                    art.tprint("Yellow won")
                if board[i][j] + board[i][j+1] + board[i][j+2] + board[i][j+3] == blue_four:
                    end = True
                    os.system("cls")
                    art.tprint("Blue won")
            
            #vertikalni
            if i+3 <= 5:
                if board[i][j] + board[i+1][j] + board[i+2][j] + board[i+3][j] == yellow_four:
                    end = True
                    os.system("cls")
                    art.tprint("Yellow won")
                if board[i][j] + board[i+1][j] + board[i+2][j] + board[i+3][j] == blue_four:
                    end = True
                    os.system("cls")
                    art.tprint("Blue won")
            
            #gor leva-spodaj  desna
            if i+3 <= 5 and j+3 <=6:
                if board[i][j] + board[i+1][j+1] + board[i+2][j+2] + board[i+3][j+3] == yellow_four:
                    end = True
                    os.system("cls")
                    art.tprint("Yellow won")
                if board[i][j] + board[i+1][j+1] + board[i+2][j+2] + board[i+3][j+3] == blue_four:
                    end = True
                    os.system("cls")
                    art.tprint("Blue won")
            
            #spodaj leva-gor desna
            if i-3 >= 0 and j+3 <=6:
                if board[i][j] + board[i-1][j+1] + board[i-2][j+2] + board[i-3][j+3] == yellow_four:
                    end = True
                    os.system("cls")
                    art.tprint("Yellow won")
                if board[i][j] + board[i-1][j+1] + board[i-2][j+2] + board[i-3][j+3] == blue_four:
                    end = True
                    os.system("cls")
                    art.tprint("Blue won")



def main(current):
    global end
    while not end:
        current = switch(current) #menjava
        handleturn(current)
        check()

if __name__ == "__main__":
    try:
        main(current)
    except KeyboardInterrupt: #Ctrl + D
        sys.exit()
    display(board)
