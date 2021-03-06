class Boss():
    """Enemy Class to raise errors and return the enemy's name"""
    def __init__(self):
        raise NotImplementedError("Do not create raw Enemy objects")

    def __str__(self):
        return self.name

    def is_alive(self):
        return self.hp > 0


class Goblin(Boss):
    """Boss Goblin with name, health points and damage"""
    def __init__(self, name):
        self.name = name
        self.maxhealth = 50
        self.health = self.maxhealth
        self.attack = 5
GoblinInGame = Goblin("Goblin")


class Tiger(Boss):
    """Boss  with name, health points and damage"""
    def __init__(self, name):
        self.name = name
        self.maxhealth = 200
        self.health = self.maxhealth
        self.attack = 30
TigerInGame = Tiger("Tiger")


class Dragon(Boss):
    """Boss  with name, health points and damage"""
    def __init__(self, name):
        self.name = name
        self.maxhealth = 300
        self.health = self.maxhealth
        self.attack = 25
DragonInGame = Dragon("Dragon")


class Dark_Turtle(Boss):
    """Boss  with name, health points and damage"""
    def __init__(self, name):
        self.name = name
        self.maxhealth = 1000
        self.health = self.maxhealth
        self.attack = 1
DarkTurtleInGame = Dark_Turtle("Dark Turtle")


class Phoenix(Boss):
    """Boss  with name, health points and damage"""
    def __init__(self, name):
        self.name = name
        self.maxhealth = 10
        self.health = self.maxhealth
        self.attack = 10
PhoenixInGame = Phoenix("Phoenix")


class Ripper(Boss):
    """Boss  with name, health points and damage"""
    def __init__(self, name):
        self.name = name
        self.maxhealth = 10
        self.health = self.maxhealth
        self.attack = 10
RipperInGame = Ripper("Ripper")


class Ghoul(Boss):
    """Boss  with name, health points and damage"""
    def __init__(self, name):
        self.name = name
        self.maxhealth = 10
        self.health = self.maxhealth
        self.attack = 10
GhoulInGame = Ghoul("Ghoul")


class Gold_Monkey(Boss):
    def __init__(self, name):
        self.name = name
        self.maxhealth = 10
        self.health = self.maxhealth
        self.attack = 10
GoldMonkeyInGame = Gold_Monkey("Gold Monkey")


class Gluttonous(Boss):
    def __init__(self, name):
        self.name = name
        self.maxhealth = 10
        self.health = self.maxhealth
        self.attack = 10
GluttonousInGame = Gluttonous("Gluttonous")


class White_Fox(Boss):
    def __init__(self, name):
        self.name = name
        self.maxhealth = 10
        self.health = self.maxhealth
        self.attack = 10
WhiteFoxInGame = White_Fox("White Fox")


class Goblin_Archer(Boss):
    def __init__(self, name):
        self.name = name
        self.maxhealth = 10
        self.health = self.maxhealth
        self.attack = 10
GoblinArcherInGame = Goblin_Archer("Goblin Archer")


class Void_Emperor(Boss):
    def __init__(self, name):
        self.name = name
        self.maxhealth =100
        self.health = self.maxhealth
        self.attack =1000000
VoidEmperorInGame = Void_Emperor("Void Emperor")
