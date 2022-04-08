class Bet:
    def __init__(self,name,age,money):
        self.name = name
        self.age = age
        self.money = money
    def getName(self):
        return self.name

    def getMoney(self):
        return self.money

    def getAge(self):
        return self.age

    def setName(self,name):
        self.name = name
        return name

    def setMoney(self,money):
        self.money = money
        return money

    def setAge(self,age):
        self.age = age
        return age

    def __str__(self):
        return str(self.name)+" "+str(self.age)+" "+str(self.money)





