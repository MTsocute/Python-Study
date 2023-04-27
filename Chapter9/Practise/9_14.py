from random import randint


class Die():
    def __init__(self, sides = 6) -> None:
        self.sides = sides

    def roll_die(self):
        for i in range(0,10):
            print(randint(1, self.sides))

die_6 = Die()
die_6.roll_die()