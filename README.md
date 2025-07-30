# DunDefCalc

DunDefCalc (short for Dungeon Defenders Calculator) is a simple commandline tool to calculate maximum stat potential of armor pieces and some other stuff in Dungeon Defenders.<br>
<br>
It works in a similar fashion to TBot in DDRnG community, but can run locally. Not all features of TBot are supported, but I can try to replicate them if there's enough interest.<br>
<br>
I made this app for personal use so I don't need to open Discord each time I want to check armor drops.<br>

## How to run

Download latest version from [Releases](https://github.com/guanab/dundefcalc/releases)

**Windows**
1. install Python (https://www.python.org/downloads/)
2. run dundefcalc.py with Python

**Linux**
1. install python from your package manager
2. run `python dundefcalc.py` in terminal

## Available commands

**bonus**<br>
`bonus mainstat upgrades side1 side2 side3`<br>
- calculates the stat total your armor will reach when all upgrades are spent on main stat<br>

**res**<br>
`res res1 res2 res3 res4 mainstat upgrades side1 side2 side3`<br>
- calculates the stat total your armor will reach when resistances are upgraded to 29 (41 with bonus) and rest of the upgrades are spent on main stat
- can also be used with only resistance values to calculate amount of upgrades needed to reach max res<br>

**3res**<br>
`3res res1 res2 res3 mainstat upgrades side1 side2 side3`<br>
- same as res but calculates upgrades needed to reach 35 res (49 with bonus) on 3 resistances<br>

**lt**<br>
`lt stattotal` or `lt tdamage trate`<br>
- calculates how much tower damage and rate you should aim for for lightning towers<br>

**cat**<br>
`cat boost upgrades range`<br>
- calculates how much boost, range and targets your cat will reach<br>

## Known limitations / issues
- res commands don't consider filler upgrades when upgrading past 23 and fail to inform user if the piece doesn't have enough total upgrades
- lt command isn't 100% accurate. it uses a fixed ratio of 1.21 for damage / rate, which is reasonably accurate for endgame stats, but optimizers should check on a dummy
