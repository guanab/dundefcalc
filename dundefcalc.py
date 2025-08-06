"""
File: dundefcalc.py
Author: Guanab
Description: A commandline calculating tool for Dungeon Defenders
"""
__version__ = "v0.3.0-beta"

import math


class Armor:
    """
    A class for armor pieces
    Attributes: resistance (list), mainstat (int), upgrades (int),
                sidestat (list), ups_on_res (int)
    Methods: get_res_ups(), get_three_res_ups(), get_total(), get_total_bonus()
    """
    resistance = []  # expected 3-4 integers in range -18 to 35
    mainstat = 0  # expected non-zero integer
    upgrades = 0  # expected positive integer
    sidestat = []  # expected 0-3 non-zero integers
    ups_on_res = 0  # expected positive integer

    def get_res_ups(self):
        self.ups_on_res = 0
        i = 0
        while i < len(self.resistance):
            self.ups_on_res += ups_to_max_res(self.resistance[i])
            i += 1
        return self.ups_on_res

    def get_three_res_ups(self):
        self.ups_on_res = 0
        i = 0
        while i < len(self.resistance):
            if self.resistance[i] > 35:
                print("\nres value higher than expected, ignoring\n")
            if self.resistance[i] in range(30, 36):
                self.ups_on_res += 35 - self.resistance[i]
            else:
                self.ups_on_res += ups_to_max_res(self.resistance[i]) + 6
            i += 1
        return self.ups_on_res

    def get_total(self):
        if self.upgrades > 0:
            total = self.mainstat + self.upgrades - 1
            i = 0
            while i < len(self.sidestat):
                total += self.sidestat[i]
                i += 1
            return total
        else:
            return self.mainstat

    def get_total_bonus(self):
        if self.upgrades > 0:
            mainupped = self.mainstat + self.upgrades - self.ups_on_res - 1
            totalbonus = int(math.ceil(mainupped * 1.4))
            i = 0
            while i < len(self.sidestat):
                if self.sidestat[i] > 0:
                    totalbonus += int(math.ceil(self.sidestat[i] * 1.4))
                i += 1
            return totalbonus
        else:
            return int(math.ceil(self.mainstat * 1.4))


class StatStick:
    """
    A class for items that are used for raw stats
    Attributes: mainstat (int), upgrades (int), sidestat (list), cap (int)
    Methods: get_upped_stats()
    """
    mainstat = 0  # expected non-zero integer
    upgrades = 0  # expected positive integer
    sidestat = []  # expected 0-3 non-zero integers
    cap = 999  # expected positive integer

    def get_upped_stats(self):
        remainder = self.upgrades - 1
        uppedstats = []
        uppedstats.append(self.mainstat)
        if len(self.sidestat) > 0:
            uppedstats.extend(self.sidestat)
        i = 0
        while i < len(uppedstats):
            if uppedstats[i] < self.cap:
                uppedstats[i] += remainder
                if uppedstats[i] > self.cap:
                    remainder = uppedstats[i] - self.cap
                    uppedstats[i] = self.cap
                else:
                    remainder = 0
                    break
            i += 1
        uppedstats.append(remainder)
        return uppedstats


class Cat:
    """
    A class for propeller cat pet
    Attributes: boost (int), upgrades (int), range (int)
    Methods: get_upped_boost(), get_upped_range(), get_targets(), get_hero_stat()
    """
    boost = 0  # expected positive integer
    upgrades = 0  # expected positive integer
    range = 0  # expected positive integer

    def get_upped_boost(self):
        if self.upgrades >= 90:
            return int(self.boost + math.floor(self.upgrades / 3) - 3)
        else:
            return int(self.boost + math.floor(self.upgrades / 3) - (
                       math.floor(self.upgrades / 30)))

    def get_upped_range(self):
        range = int(self.range + math.floor(self.upgrades / 5) - math.floor(
                    self.upgrades / 15))
        if range >= 90:
            return 90
        else:
            return range

    def get_targets(self):
        if self.upgrades >= 90:
            return 4
        else:
            return int(math.floor(self.upgrades / 30) + 1)

    def get_hero_stat(self):
        return int(self.upgrades - math.floor(self.upgrades / 3) - (
                   self.get_upped_range() - self.range) - 1)


class Pet:
    """
    A class for melee and ranged damage pets
    Attributes: damage (int), damage_per_up (int), upgrades (int), rate (int),
                max_rate (int), procount (int), max_procount (int),
                prospeed (int)
    Methods: get_upped_damage()
    """
    damage = 0  # expected positive integer
    damage_per_up = 0  # expected positive integer
    upgrades = 0  # expected positive integer
    rate = 7  # expected positive integer
    max_rate = 7  # expected positive integer
    procount = 1  # expected positive integer
    max_procount = 1  # expected positive integer
    prospeed = 30000  # expected non-zero integer

    def set_damage(self, value):
        if value <= 0:
            raise ValueError("damage needs to be positive")
        self.damage = value

    def get_upped_damage(self):
        if self.rate >= self.max_rate:
            upsonrate = 0
        else:
            upsonrate = self.max_rate - self.rate
        if self.procount >= self.max_procount:
            upsonprocount = 0
        else:
            upsonprocount = self.max_procount - self.procount
        if self.prospeed >= 30000:
            upsonprospeed = 0
        else:
            upsonprospeed = ups_to_max_pro_speed(self.prospeed)
        upsspent = upsonrate + upsonprocount + upsonprospeed
        return self.damage + (
            self.damage_per_up * (self.upgrades - upsspent - 1)
        )


def res(arglist):
    """
    A command to calculate upgrades needed to maximize resistances on armor and
    the stat total it reaches after that
    Expects a list of 4-9 but not 5 numbers
    [res1, res2, res3, res4, main stat, upgrades, side1, side2, side3]
    """
    try:
        arglist = list_to_int(arglist)
    except Exception as e:
        print(f"\nerror: {e}\n")
        return
    a = Armor()
    a.resistance = arglist[0:3]
    upsneeded = a.get_res_ups()
    match len(arglist):
        case 4:
            print(f"\nyour piece will need \033[1m{upsneeded}\033[0m upgrades \
to hit max resistances\n")
        case 6 | 7 | 8 | 9:
            if only_pos_values(arglist[4:]) is False:
                print("\nnegative value entered where expecting positive\n")
                del a
                return
            a.mainstat = arglist[4]
            a.upgrades = arglist[5]
            if len(arglist) > 6:
                a.sidestat = arglist[6:]
            totalstats = a.get_total()
            totalbonus = a.get_total_bonus()
            print(f"\nafter spending \033[1m{upsneeded}\033[0m upgrades on \
resistances")
            print(f"your piece will reach \033[1m{totalstats}\033[0m, \
or \033[1m{totalbonus}\033[0m with set bonus\n")
        case _:
            print("\ninvalid arguments\n")
    del a


def threeres(arglist):
    """
    A command to calculate upgrades needed to upgrade 3 resistances to 35 on
    armor and the stat total it reaches after that
    Expects a list of 3-8 but not 4 numbers
    [res1, res2, res3, main stat, upgrades, side1, side2, side3]
    """
    try:
        arglist = list_to_int(arglist)
    except Exception as e:
        print(f"\nerror: {e}\n")
        return
    a = Armor()
    a.resistance = arglist[0:2]
    upsneeded = a.get_three_res_ups()
    match len(arglist):
        case 3:
            print(f"\nyour piece will need \033[1m{upsneeded}\033[0m upgrades \
to hit 35 res on 3 resistances\n")
        case 5 | 6 | 7 | 8:
            if only_pos_values(arglist[3:]) is False:
                print("\nnegative value entered where expecting positive\n")
                del a
                return
            a.mainstat = arglist[3]
            a.upgrades = arglist[4]
            if len(arglist) > 5:
                a.sidestat = arglist[5:]
            totalstats = a.get_total()
            totalbonus = a.get_total_bonus()
            print(f"\nafter spending \033[1m{upsneeded}\033[0m upgrades on \
resistances (3 x 35)")
            print(f"your piece will reach \033[1m{totalstats}\033[0m, \
or \033[1m{totalbonus}\033[0m with set bonus\n")
        case _:
            print("\ninvalid arguments\n")
    del a


def bonus(arglist):
    """
    A command to calculate what stat total a piece of armor can reach if no
    upgrades are spent on resistances
    Expects a list of 1-5 numbers [main stat, upgrades, side1, side2, side3]
    """
    try:
        arglist = list_to_int(arglist)
    except Exception as e:
        print(f"\nerror: {e}\n")
        return
    if only_pos_values(arglist) is False:
        print("\nnegative value entered where expecting positive\n")
        return
    a = Armor()
    a.mainstat = arglist[0]
    if len(arglist) > 1:
        a.upgrades = arglist[1]
    if len(arglist) > 2:
        a.sidestat = arglist[2:]
    totalstats = a.gettotal()
    totalbonus = a.gettotalbonus()
    print(f"\nyour piece will reach \033[1m{totalstats}\033[0m, \
or \033[1m{totalbonus}\033[0m with set bonus\n")
    del a


def cap(arglist):
    """
    A command to calculate how many stat caps and total stats an item will reach
    Expects a list of 2-5 numbers [main stat, upgrades, side1, side2, side3]
    """
    try:
        arglist = list_to_int(arglist)
    except Exception as e:
        print(f"\nerror: {e}\n")
        return
    if only_pos_values(arglist) is False:
        print("\nnegative value entered where expecting positive\n")
        return
    s = StatStick()
    s.mainstat = arglist[0]
    s.upgrades = arglist[1]
    if len(arglist) > 2:
        s.sidestat = arglist[2:]
    s.cap = 999
    uppedstats = []
    uppedstats.extend(s.get_upped_stats())
    total = sum(uppedstats[:-1])
    remainder = uppedstats[-1]
    print(f"\nyour item will reach \033[1m{total}\033[0m total stats")
    print(uppedstats[:-1])
    if remainder > 0:
        print(f"with {remainder} upgrades to spare\n")
    else:
        print("")
    del s


def diamond(arglist):
    """
    A command to calculate how many stat caps and total stats diamond will reach
    Expects a list of 2-5 numbers [main stat, upgrades, side1, side2, side3]
    """
    try:
        arglist = list_to_int(arglist)
    except Exception as e:
        print(f"\nerror: {e}\n")
        return
    if only_pos_values(arglist) is False:
        print("\nnegative value entered where expecting positive\n")
        return
    s = StatStick()
    s.mainstat = arglist[0]
    s.upgrades = arglist[1]
    if len(arglist) > 2:
        s.sidestat = arglist[2:]
    s.cap = 800
    uppedstats = []
    uppedstats.extend(s.get_upped_stats())
    total = sum(uppedstats[:-1])
    remainder = uppedstats[-1]
    print(f"\nyour diamond will reach \033[1m{total}\033[0m total stats")
    print(uppedstats[:-1])
    if remainder > 0:
        print(f"with {remainder} upgrades to spare\n")
    else:
        print("")
    del s


def lt(arglist):
    """
    A command to calculate how much tower damage and rate user should aim for
    with a provided stat total
    Expects a list of 1-2 numbers [stat total] or [tower damage, tower rate]
    """
    try:
        arglist = list_to_int(arglist)
    except Exception as e:
        print(f"\nerror: {e}\n")
        return
    if only_pos_values(arglist) is False:
        print("\nnegative value entered where expecting positive\n")
        return
    if len(arglist) == 1:
        stattotal = arglist[0]
    else:
        stattotal = arglist[0] + arglist[1]
    dmg = int(round(stattotal * 1.21 / 2.21))
    rate = stattotal - dmg
    print(f"\nwith a stat total of \033[1m{stattotal}\033[0m,")
    print(f"aim for roughly \033[1m{dmg}\033[0m damage and \033[1m{rate}\
\033[0m rate\n")


def cat(arglist):
    """
    A command to calculate how much boost, range and targets a propeller cat
    will reach
    Expects a list of 2-3 numbers [boost, upgrades, range]
    """
    try:
        arglist = list_to_int(arglist)
    except Exception as e:
        print(f"\nerror: {e}\n")
        return
    if only_pos_values(arglist) is False:
        print("\nnegative value entered where expecting positive\n")
        return
    c = Cat()
    c.boost = arglist[0]
    c.upgrades = arglist[1]
    totalboost = c.get_upped_boost()
    targets = c.get_targets()
    if len(arglist) > 2:
        c.range = arglist[2]
        range = c.get_upped_range()
        hero = c.get_hero_stat()
        print(f"\nyour cat will reach \033[1m{totalboost}\033[0m boost, \
\033[1m{range}\033[0m range and \033[1m{targets}\033[0m targets")
        print(f"you will have {hero} points to spend on hero stats")
    else:
        c.range = 0
        rangeups = c.get_upped_range()
        hero = c.get_hero_stat()
        print(f"\nyour cat will reach \033[1m{totalboost}\033[0m boost and \
\033[1m{targets}\033[0m targets")
        print(f"you will have {rangeups} points to spend on range and \
{hero} on hero stats\n")
    del c


def wizard(arglist):
    """
    A command to calculate how much damage a little wizard pet will reach with
    capped attack rate and projectile speed
    Expects a list of 2-4 numbers [damage, upgrades, rate, prospeed]
    """
    try:
        arglist = list_to_int(arglist)
    except Exception as e:
        print(f"\nerror: {e}\n")
        return
    if only_pos_values(arglist) is False:
        print("\nnegative value entered where expecting positive\n")
        return
    p = Pet()
    p.damage = arglist[0]
    p.upgrades = arglist[1]
    if len(arglist) > 2:
        p.rate = arglist[2]
    else:
        p.rate = 7
    p.max_rate = 7
    if len(arglist) > 3:
        p.prospeed = arglist[3]
    else:
        p.prospeed = 30000
    p.procount = 1
    p.max_procount = 1
    p.damage_per_up = 112
    damage = p.get_upped_damage()
    print(f"\nyour wizard will reach \033[1m{damage}\033[0m damage\n")
    del p


def ups_to_max_res(resvalue):
    """
    A function to calculate how many upgrades are needed to upgrade a provided
    resistance value to 29
    Expects a non-zero number in the range of -18 to 29
    Returns an integer
    """
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


def ups_to_max_pro_speed(prospeed):
    """
    A function to calculate how many upgrades are needed to upgrade a provided
    projectile speed to 30000
    Expects a number
    Returns an integer
    """
    prospeed = int(prospeed)
    if prospeed >= 30000:
        return 0
    elif prospeed >= 4800:
        return int(math.ceil((30000 - prospeed) / 1200))
    else:
        ups = 0
        while prospeed < 30000:
            quarter = int(math.floor(abs(prospeed) * 0.25))
            if quarter < 100:
                quarter = 100
            if quarter > 1200:
                quarter = 1200
            prospeed += quarter
            ups += 1
        return ups


def list_to_int(stringlist):
    """
    A function to convert all provided list values to integers
    Expects a list of numbers
    Returns a list of integers
    """
    if type(stringlist) is not list:
        raise TypeError("type is not list")
    intlist = []
    i = 0
    while i < len(stringlist):
        try:
            intlist.insert(i, int(stringlist[i]))
        except ValueError as e:
            raise ValueError("cannot convert to integer") from e
        i += 1
    if len(intlist) == 0:
        raise ValueError("list is empty")
    else:
        return intlist


def only_pos_values(arglist):
    """
    A function to check if all values in a provided list are positive
    Expects a list of numbers
    Returns a boolean
    """
    i = 0
    while i < len(arglist):
        if arglist[i] < 0:
            return False
        i += 1
    return True


def main():
    """
    Main function
    Asks the user for input and runs a related command if it exists
    Loops until 'exit' is inputted
    """
    print("please input your command")
    print("available commands: res, 3res, bonus, cap, diamond, lt, cat, wizard\
, exit")
    userinput = input()
    if userinput.strip() == "":
        print("\nempty input\n")
        return
    inputlist = userinput.split()
    argcount = len(inputlist) - 1
    arglist = []
    if argcount > 0:
        arglist = inputlist[1:]

    match inputlist[0].lower():
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
        case "bonus":
            if argcount < 1 or argcount > 5:
                print("\ninvalid arguments\n")
            else:
                bonus(arglist)
        case "cap":
            if argcount < 2 or argcount > 5:
                print("\ninvalid arguments\n")
            else:
                cap(arglist)
        case "diamond":
            if argcount < 2 or argcount > 5:
                print("\ninvalid arguments\n")
            else:
                diamond(arglist)
        case "lt":
            if argcount < 1 or argcount > 2:
                print("\ninvalid arguments\n")
            else:
                lt(arglist)
        case "cat":
            if argcount < 2 or argcount > 3:
                print("\ninvalid arguments\n")
            else:
                cat(arglist)
        case "wizard":
            if argcount < 2 or argcount > 4:
                print("\ninvalid arguments\n")
            else:
                wizard(arglist)
        case "exit":
            print("\nending program\n")
            quit()
        case _:
            print("\ninvalid command\n")


if __name__ == "__main__":
    print("DunDefCalc " + __version__)
    while True:
        main()
