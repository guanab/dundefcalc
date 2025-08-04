# DunDefCalc

DunDefCalc (short for Dungeon Defenders Calculator) is a simple commandline tool to calculate maximum stat potential of armor pieces and some other stuff in Dungeon Defenders.<br>
<br>
It works in a similar fashion to TBot in DDRnG community, but can run locally. Not all features of TBot are supported, but I can try to replicate them if there's enough interest.<br>
<br>
I made this app for personal use so I don't need to open Discord each time I want to check armor drops.<br>

## How to run

Download latest version from [Releases](https://github.com/guanab/dundefcalc/releases)

**Windows**
1. Install Python (https://www.python.org/downloads/)
2. Run dundefcalc.py with Python

**Linux**
1. Install python from your package manager
2. Run `python dundefcalc.py` in terminal

## Available commands

**Bonus**<br>
`bonus <main stat> [upgrades] [side1] [side2] [side3]`<br>
- Calculates the stat total your armor will reach when all upgrades are spent on main stat
- Only for ultimate or higher armor<br>

**Res**<br>
`res <res1> <res2> <res3> <res4> [main stat] [upgrades] [side1] [side2] [side3]`<br>
- Calculates the stat total your armor will reach when resistances are upgraded to 29 (41 with bonus) and rest of the upgrades are spent on main stat
- Can also be used with only resistance values to calculate amount of upgrades needed to reach max res
- Only for ultimate or higher armor<br>

**3res**<br>
`3res <res1> <res2> <res3> [mainstat] [upgrades] [side1] [side2] [side3]`<br>
- Same as res but calculates upgrades needed to reach 35 res (49 with bonus) on 3 resistances<br>

**Cap**<br>
`cap <main stat> <upgrades> [side1] [side2] [side3]`<br>
- Calculates how many stat caps (999) and total stats your item will reach<br>

**Diamond**<br>
`diamond <main stat> <upgrades> [side1] [side2] [side3]`<br>
- Calculates how many stat caps (800) and total stats your Diamond will reach<br>

**Lt**<br>
`lt <stat total>` or `lt <tower damage> <tower rate>`<br>
- Calculates how much tower damage and rate you should aim for for Lightning Towers<br>

**Cat**<br>
`cat <boost> <upgrades> [range]`<br>
- Calculates how much boost, range and targets your Propeller Cat will reach<br>

**Wizard**<br>
`wizard <damage> <upgrades> [attack rate] [projectile speed]`
- Calculates how much damage your Little Wizard will reach with capped attack rate and projectile speed
- Only for ultimate or higher Little Wizards<br>

## Known limitations / issues
- Res commands don't consider filler upgrades when upgrading past 23 and fail to inform user if the piece doesn't have enough total upgrades
- Lt command isn't 100% accurate. It uses a fixed ratio of 1.21 for damage / rate, which is reasonably accurate for endgame stats, but optimizers should check on a dummy
