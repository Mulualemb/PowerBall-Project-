# from Gamble import Gamble
# from Functions import *
# # the game first message to the user,print a list of the winning numbers.
# # the lists first 5 numbers are sorted and with a different color than the last index
#
#
# def startGame():
#     user1 = Gamble(0,0)
#     user1.setAge(int(input("how old are you?:")))
#     if user1.age >= 18 :
#         user1.setMoney(int(input("how much money you want to gamble?:")))
#         sorted(secondlist[:len(firstlist) - 1]), firstlist[-1]
#         print("this are the lucky numbersof the day.\n======================\n",
#               Fore.LIGHTMAGENTA_EX + str(sorted(secondlist[:len(firstlist) - 1])) + Style.RESET_ALL,
#               Fore.YELLOW + str(secondlist[-1]) + Style.RESET_ALL, "\n======================""")
#     else:
#         print("this game,is not for you!! bye bye")
#         exit()
#         tryme = input("if you want to play enter 'y'\nany other input will end the game!\nenter 'y' to continue:")
#         while  tryme == "y":
#             tryme = input("if you want to play enter 'y'\nany other input will end the game!\nenter 'y' to continue:")
#
#
#             print("goodbye")
#             exit()
#             #this will print the amount of white/purple balls
#             print("you found", findme(firstlist, secondlist), "white balls\nand", findmetwo(firstlist, secondlist), "purple ball")
#
#
#
# # calculate and return the money you earn
# # running everything now, winning_amount function require two parameters
# # and this two parameters each has its own two parameters
# # example winning_amount(a,b),but a and b also have 2 parameters,so it will look like winning_amount
# def winning_amount(a, b):
#     if a == 0 and b == 1:
#         return "you won 4$"
#     elif a == 1 and b == 1:
#         return "you won 4$"
#     elif a == 2 and b == 1:
#         return "you won 7$"
#     elif a == 3 and b == "no":
#         return "you won 7$"
#     elif a == 3 and b == 1:
#         return "you won 100$"
#     elif a == 4 and b == "no":
#         return "you won 100$"
#     elif a == 4 and b == 1:
#         return "you won 10,000$"
#     elif a == 5 and b == "no":
#         return "you won 1,000,000$"
#     elif a == 5 and b == 1:
#         return "you won 324,000,000$"
#     else:
#         return "try again"
#
#
#
#
# # test print all all numbers in a list except the last number
# # print(firstlist[:len(firstlist)-1])
#
# # test how to print only the last number in a list
# # print(firstlist[len(firstlist