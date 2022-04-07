class Gamble:
    def __init__(self,age,money):
        self.age = age
        self.money = money

    def getMoney(self):
        return self.money

    def getAge(self):
        return self.age

    def setMoney(self,money):
        self.money = money
        return money

    def setAge(self,age):
        self.age = age
        return age

    def __str__(self):
        return str(self.age)+" "+str(self.money)





