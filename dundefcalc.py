# Dungeon Defenders Calculator v0.1.0
# Made by Guanab

import math


class Armor:
    res1 = 0
    res2 = 0
    res3 = 0
    res4 = 0
    mainstat = 0
    upgrades = 0
    side1 = 0
    side2 = 0
    side3 = 0
    upsonres = 0

    def getresups(self):
        return upstomax(self.res1) + upstomax(self.res2) + upstomax(self.res3) \
            + upstomax(self.res4)

    def getthreeresups(self):
        return upstomax(self.res1) + upstomax(self.res2) + upstomax(self.res3) \
            + 18

    def gettotal(self):
        if self.upgrades > 0:
            return self.mainstat + self.upgrades + self.side1 + self.side2 + \
                self.side3 - self.upsonres - 1
        else:
            return self.mainstat

    def gettotalbonus(self):
        if self.upgrades > 0:
            totalstats = self.mainstat + self.upgrades - self.upsonres - 1
            totalbonus = int(math.ceil(totalstats * 1.4))
            if self.side1 > 0:
                totalstats += self.side1
                totalbonus += int(math.ceil(self.side1 * 1.4))
            if self.side2 > 0:
                totalstats += self.side2
                totalbonus += int(math.ceil(self.side2 * 1.4))
            if self.side3 > 0:
                totalstats += self.side3
                totalbonus += int(math.ceil(self.side3 * 1.4))
            return totalbonus
        else:
            return int(math.ceil(self.mainstat * 1.4))


def res(arglist):
    arglist = listtoint(arglist)
    if type(arglist) is not list:
        return
    a = Armor()
    a.res1 = arglist[0]
    a.res2 = arglist[1]
    a.res3 = arglist[2]
    a.res4 = arglist[3]
    upsneeded = a.getresups()
    match len(arglist):
        case 4:
            print(f"\nyour piece will need \033[1m{upsneeded}\033[0m upgrades \
to hit max resistances\n")
        case 6 | 7 | 8 | 9:
            a.mainstat = arglist[4]
            a.upgrades = arglist[5]
            a.upsonres = upsneeded
            if len(arglist) > 6:
                a.side1 = arglist[6]
            if len(arglist) > 7:
                a.side2 = arglist[7]
            if len(arglist) > 8:
                a.side3 = arglist[8]
            totalstats = a.gettotal()
            totalbonus = a.gettotalbonus()
            print(f"\nafter spending \033[1m{upsneeded}\033[0m upgrades on \
resistances")
            print(f"your piece will reach \033[1m{totalstats}\033[0m, \
or \033[1m{totalbonus}\033[0m with set bonus\n")
        case _:
            print("\ninvalid arguments\n")
    del a


def threeres(arglist):
    arglist = listtoint(arglist)
    if type(arglist) is not list:
        return
    a = Armor()
    a.res1 = arglist[0]
    a.res2 = arglist[1]
    a.res3 = arglist[2]
    upsneeded = a.getthreeresups()
    match len(arglist):
        case 3:
            print(f"\nyour piece will need \033[1m{upsneeded}\033[0m upgrades \
to hit 35 res on 3 resistances\n")
        case 5 | 6 | 7 | 8:
            a.mainstat = arglist[3]
            a.upgrades = arglist[4]
            a.upsonres = upsneeded
            if len(arglist) > 5:
                a.side1 = arglist[5]
            if len(arglist) > 6:
                a.side2 = arglist[6]
            if len(arglist) > 7:
                a.side3 = arglist[7]
            totalstats = a.gettotal()
            totalbonus = a.gettotalbonus()
            print(f"\nafter spending \033[1m{upsneeded}\033[0m upgrades on \
resistances (3 x 35)")
            print(f"your piece will reach \033[1m{totalstats}\033[0m, \
or \033[1m{totalbonus}\033[0m with set bonus\n")
        case _:
            print("\ninvalid arguments\n")
    del a


def bonus(arglist):
    arglist = listtoint(arglist)
    if type(arglist) is not list:
        return
    a = Armor()
    a.mainstat = arglist[0]
    if len(arglist) > 1:
        a.upgrades = arglist[1]
    if len(arglist) > 2:
        a.side1 = arglist[2]
    if len(arglist) > 3:
        a.side2 = arglist[3]
    if len(arglist) > 4:
        a.side3 = arglist[4]
    totalstats = a.gettotal()
    totalbonus = a.gettotalbonus()
    print(f"\nyour piece will reach \033[1m{totalstats}\033[0m, \
or \033[1m{totalbonus}\033[0m with set bonus\n")
    del a


def lt(arglist):
    arglist = listtoint(arglist)
    if type(arglist) is not list:
        return
    if len(arglist) == 1:
        stattotal = arglist[0]
    else:
        stattotal = arglist[0] + arglist[1]
    rate = int(stattotal / 2.21)
    dmg = stattotal - rate
    print(f"\nwith a stat total of \033[1m{stattotal}\033[0m,")
    print(f"aim for roughly \033[1m{dmg}\033[0m damage and \033[1m{rate}\
\033[0m rate\n")


def upstomax(resvalue):
    resvalue = int(resvalue)
    match resvalue:
        case 23 | 24 | 25 | 26 | 27 | 28 | 29:
            return 29 - resvalue
        case 20 | 21 | 22:
            return 29 - resvalue - 2
        case 19:
            return 7
        case 17 | 18:
            return 8
        case 15 | 16:
            return 9
        case 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14:
            return 14 - resvalue + 10
        case 0:
            print("\nres value 0, ignoring\n")
            return 0
        case -1 | -2 | -3 | -4 | -5 | -6 | -7 | -8 | -9 | -10 | -11 | -12:
            return 23 - resvalue
        case -13 | -14:
            return 36
        case -15 | -16:
            return 37
        case -17 | -18:
            return 38
        case _:
            if resvalue > 29:
                print("\nres value higher than expected, ignoring\n")
            else:
                print("\nres value lower than expected, ignoring\n")
            return 0


def listtoint(strlist):
    if type(strlist) is not list:
        return False
    intlist = []
    i = 0
    while i < len(strlist):
        try:
            intlist.insert(i, int(strlist[i]))
        except ValueError:
            print("\ncannot convert to integer\n")
            return False
        i += 1
    if len(intlist) == 0:
        return False
    else:
        return intlist


def main():
    print("please input your command")
    print("available commands: res, 3res, bonus, lt, exit")
    userinput = input()
    if userinput.strip() == "":
        print("\nempty input\n")
        return
    inputlist = userinput.split()
    argcount = len(inputlist) - 1
    arglist = []
    if argcount > 0:
        arglist = listtoint(inputlist[1:])
        if type(arglist) is not list:
            return

    match inputlist[0]:
        case "res":
            if argcount < 4 or argcount == 5 or argcount > 9:
                print("\ninvalid arguments\n")
            else:
                res(arglist)
        case "3res":
            if argcount < 3 or argcount == 4 or argcount > 8:
                print("\ninvalid arguments\n")
            else:
                threeres(arglist)
        case "lt":
            if argcount < 1 or argcount > 2:
                print("\ninvalid arguments\n")
            else:
                lt(arglist)
        case "bonus":
            if argcount < 1 or argcount > 5:
                print("\ninvalid arguments\n")
            else:
                bonus(arglist)
        case "exit":
            print("\nending program\n")
            quit()
        case _:
            print("\ninvalid command\n")


if __name__ == "__main__":
    while True:
        main()
