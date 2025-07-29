# DunDefCalc

DunDefCalc (short for Dungeon Defenders Calculator) is a simple commandline tool to calculate maximum stat potential of armor pieces.<br>
It works in a similar fashion to TBot in DDRnG community, but can run locally. Not all features of TBot are supported, but I can try to replicate them if there's enough interest.<br>
I made this app for personal use so I don't need to open Discord each time I want to check armor drops.

## How to run
**Windows**
1. install Python (https://www.python.org/downloads/)
2. run dundefcalc.py with Python

**Linux**
1. install python from your package manager
2. run `python dundefcalc.py` in terminal

## Available commands
- **bonus** mainstat upgrades side1 side2 side3
    - calculates the stat total your armor will reach if main stat is upgraded to the maximum
- **res** res1 res2 res3 res4 mainstat upgrades side1 side2 side3
    - calcluates the stat total your armor will reach when resistances are upgraded to 29 and rest of the upgrades are spent on main stat
    - can also be used with only resistance values to calculate amount of upgrades needed to reach max res

## Known limitations / issues
- res command doesn't work with 3 or fewer resistance values, you always need 4 res values. you can insert 0 to ignore that res value though
- res command doesn't consider filler upgrades when upgrading past 23 and fails to inform user if the piece doesn't have enough total upgrades
- calculated set bonus sometimes differs by 1-2 points compared to TBot (probably a rounding issue)
