# 2D-Clash-of-Clans

A miniature 2D version of Clash of Clans that works on CLI

## Installation and running

1. Run the following command to install all the required libraries \
   `pip3 install -r requirements.txt`
2. To run the game, \
   `cd src` \
   `python3 main.py`
3. Ensure that your terminal is in full screen.


## Controls

- `w` move King up
- `a` move King left
- `s` move King down
- `d` move King right
- `r` use Rage spell
- `h` use Heal spell
- `b` select Barabarian
- `n` select Archer
- `m` select Balloon
- `1` spawn troop at top left corner
- `2` spawn troop at Bottom left corner
- `3` spawn troop at Bottom Right corner
## Features

### Inheritance

`Barbarian` and `King` classes are inherited from the `Character` class. `Hut`, `Cannon` and `TownHall` are inherited from the `Building` class.

### Polymorphism

Functions such as `attack`, `move`, etc are common for multiple objects.

### Encapsulation

Multiple classes and objects are used.

### Abstraction

Many functions such as `printBoard`, `updateGame`, etc are abstracted.
