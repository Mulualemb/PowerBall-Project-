from colorama import Fore, Style

# function to import numbers from 1 - 10:
def randomfunten():
    import random
    return random.randrange(1, 10)




# function to import numbers from 1 - 20
def randomfuntwenty():
    import random
    return random.randrange(1, 20)




# function to add random numbers to a list with no duplicate!
# the second if statement can be removed to allow the last number to have duplicates
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




# function to find matching last number in two list
# will be used to find the gold ball
def findmetwo(a, b):
    count = 0
    if a[len(a) - 1:] == b[len(a) - 1:]:
        count += 1
        return count
    else:
        return "no"




# function to find all matching numbers in two lists except skipping the last index
# will be used for checking white balls
def findme(a, b):
    countme = 0
    for i in a[:len(a) - 1]:
        for j in b[:len(b) - 1]:
            if i == j:
                countme += 1
    return countme




# this function will print a list without bracket and with colors
# first part sort the list except for the last index
# second part remove the brackets from the list and add colors
def noBracketpluscolor(a):
    b = sorted(a[:-1])
    s = ""
    for i in b:
        s = s + str(i) + " "
    return Fore.MAGENTA+s[:-1]+Style.RESET_ALL + " " + Fore.LIGHTYELLOW_EX+str(a[-1])+Style.RESET_ALL













#####tests######
# def testchangetest(a):
#     n = str
#     for i in (a):
#         n = str(n)+""+str(i)
#     return n
#
# test
# def tessummytotaltest(a,b):
#     a - b
#     while  a >= 5:
#         return "you have",a+"$"+"left"
#     else:
#         return "you have",a+"$"+"left its not enough to participate\ngoodbye"

    # test how to print all all numbers in a list except the last number
    # print(firstlist[:len(firstlist)-1])

    # test how to print only the last number in a list
    # print(firstlist[len(firstlist


