from Gamble import Gamble
from colorama import Fore, Back, Style
# function to import numbers from 1 - 10:
def randomfunten():
    import random
    return random.randrange(1, 10)


# function to import numbers from 1 - 20
def randomfuntwenty():
    import random
    return random.randrange(1, 20)


# function to add random numbers to a list with no duplicate!
firstlist = list()
secondlist = list()
def firstdraw(a):
    while len(a) < 5:
        x = randomfuntwenty()
        if x not in a:
            a.append(x)

    while len(a) != 6:
        c = randomfunten()
        if c not in a:
            a.append(c)


#call list functions
firstdraw(firstlist)
firstdraw(secondlist)




# function to find matching last number in a two list
def findmetwo(a, b):
    count = 0
    if a[len(a) - 1:] == b[len(a) - 1:]:
        count += 1
        return count
    else:
        return "no"


# function to find all matching numbers in a list except the last numbers
# will be used for checking white balls
def findme(a, b):
    countme = 0
    for i in a[:len(a) - 1]:
        for j in b[:len(b) - 1]:
            if i == j:
                countme += 1
    return countme



# calculate and return the money you earn
# running everything now, winning_amount function require two parameters
# and this two parameters each has its own two parameters
# example winning_amount(a,b),but a and b also have 2 parameters,so it will look like winning_amount(A(a,b),B(a,b))
# print(winning_amount(findme(firstlist, secondlist), findmetwo(firstlist, secondlist)))

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




# def summytotal(a,b):
#     a - b
#     while  a >= 5:
#         return "you have",a+"$"+"left"
#     else:
#         return "you have",a+"$"+"left its not enough to participate\ngoodbye"
