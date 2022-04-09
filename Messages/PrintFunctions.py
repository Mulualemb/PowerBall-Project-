from Gamble import Bet
from Utilities import *


#the game first message to the user,
user1 = Bet("a",0,0)
def startGame():
    print("welcome to the game! good luck")
    user1.setName(input("what your name:"))
    while True:
        try:
            user1.setAge(int(input(f"hello {user1.getName()}, how old are you?:")))
            break
        except ValueError:
            print("enter a number:")
    if user1.age >= 18 :
        while True:
            try:
                user1.setMoney(int(input(f"{user1.getName()} how much money, you want to gamble?:")))
                break
            except ValueError:
                print("enter a number please:")
    else:
        print(f"{user1.name} this game,is not for you!! bye bye"),exit()










# function start with input to verify age and money,user can role if he type 'y' other input exit the game
# after first role is complete the list will be deleted and redraw with new numbers.
def startGamble():
    startplay = input(f"{user1.name} insert 'y' to play, or any key to exit.\nplaying fee is 5$!!!\nthis is your total {user1.money}$ 'y' to start:")
    if user1.age >= 18 and user1.money > 4:
        while startplay == "y" and user1.money > 4:
            print(noBracketpluscolor(firstlist))
            print(noBracketpluscolor(secondlist))
            print(winning_amount(findme(firstlist, secondlist), findmetwo(firstlist, secondlist)))
            firstlist.clear()
            secondlist.clear()
            firstdraw(firstlist)
            firstdraw(secondlist)
            user1.money = user1.money - 5
            startplay = input(f"insert 'y' to play, or any key to exit.\n{user1.name} this is your total {user1.money}$:")
        else:
            print(f"thank you {user1.name} this is your total {user1.money}$ ")
    else:
        print(f"sorry {user1.name} u are not eligible")




# calculate and return the money you won,plus total amount with font
# running everything now, winning_amount function require two parameters
# and this two parameters each has its own two parameters
# example winning_amount(a,b),but a and b also have 2 parameters,will look like winning_amount(A(a,b),B(a,b))


def winning_amount(a, b):
    if a == 0 and b == 1:
        user1.money = user1.money + 4
        return Fore.BLUE+"===========\nyou won 4$ \n===========".upper()+Style.RESET_ALL
    elif a == 1 and b == 1:
        user1.money = user1.money + 4
        return Fore.BLUE+"===========\nyou won 4$\n===========".upper()+Style.RESET_ALL
    elif a == 2 and b == 1:
        user1.money = user1.money + 7
        return Fore.BLUE+"===========\nyou won 7$\n===========".upper()+Style.RESET_ALL
    elif a == 3 and b == "no":
        user1.money = user1.money + 7
        return Fore.BLUE+"===========\nyou won 7$\n===========".upper()+Style.RESET_ALL
    elif a == 3 and b == 1:
        user1.money = user1.money + 100
        return Fore.BLUE+"===========\nyou won 100$\n===========".upper()+Style.RESET_ALL
    elif a == 4 and b == "no":
        user1.money = user1.money + 100
        return Fore.BLUE+"===========\nyou won 100$\n===========".upper()+Style.RESET_ALL
    elif a == 4 and b == 1:
        user1.money = user1.money + 10000
        return Fore.BLUE+"===========\nyou won 10,000$\n===========".upper()+Style.RESET_ALL
    elif a == 5 and b == "no":
        user1.money = user1.money + 1000000
        return Fore.BLUE+"===========\nyou won 1,000,000$\n===========".upper()+Style.RESET_ALL
    elif a == 5 and b == 1:
        user1.money = user1.money + 324000000
        return Fore.BLUE+"===========\nyou won 324,000,000\n===========".upper()+Style.RESET_ALL
    else:
        return f"{user1.name} try again"




