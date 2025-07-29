# Dungeon Defenders Calculator v0.1.0
# Made by Guanab

import math


def res(arglist):
    arglist = listtoint(arglist)
    if type(arglist) is not list:
        return
    upsneeded = 0
    i = 0
    while i < 4:
        upsneeded += upstomax(arglist[i])
        i += 1
    match len(arglist):
        case 4:
            print(f"\nyour piece will need \033[1m{upsneeded}\033[0m upgrades \
to hit max resistances\n")
        case 6 | 7 | 8 | 9:
            mainstat = arglist[4]
            upgrades = arglist[5]
            totalstats = mainstat + upgrades - upsneeded - 1
            totalbonus = int(math.ceil(totalstats * 1.4))
            i = 6
            while i < len(arglist):
                sidestat = arglist[i]
                totalstats += sidestat
                totalbonus += int(math.ceil(sidestat * 1.4))
                i += 1
            print(f"\nafter spending \033[1m{upsneeded}\033[0m upgrades on \
resistances")
            print(f"your piece will reach \033[1m{totalstats}\033[0m, \
or \033[1m{totalbonus}\033[0m with set bonus\n")
        case _:
            print("\ninvalid arguments\n")


def bonus(arglist):
    arglist = listtoint(arglist)
    if type(arglist) is not list:
        return
    mainstat = arglist[0]
    if len(arglist) > 1:
        upgrades = arglist[1]
        totalstats = mainstat + upgrades - 1
        totalbonus = int(math.ceil(totalstats * 1.4))
        i = 2
        while i < len(arglist):
            sidestat = arglist[i]
            totalstats += sidestat
            totalbonus += int(math.ceil(sidestat * 1.4))
            i += 1
    else:
        totalstats = mainstat
        totalbonus = int(math.ceil(mainstat * 1.4))
    print(f"\nyour piece will reach \033[1m{totalstats}\033[0m, \
or \033[1m{totalbonus}\033[0m with set bonus\n")


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
    print("available commands: res, bonus, exit")
    userinput = input()
    if userinput.strip() == "":
        print("\nempty input\n")
        return
    inputlist = userinput.split()
    argcount = len(inputlist) - 1

    match inputlist[0]:
        case "res":
            if argcount < 4 or argcount == 5 or argcount > 9:
                print("\ninvalid arguments\n")
            else:
                res(inputlist[1:])
        case "bonus":
            if argcount < 1 or argcount > 5:
                print("\ninvalid arguments\n")
            else:
                bonus(inputlist[1:])
        case "exit":
            print("\nending program\n")
            quit()
        case _:
            print("\ninvalid command\n")


if __name__ == "__main__":
    while True:
        main()
