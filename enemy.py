import random

class Enemy:
    def __init__(self, name):
        self.name = name
        self.health = random.randint(50, 100)
        self.damage = random.randint(5, 25)
    def take_damage(self, amount):
        self.health -= amount
    def is_alive(self):
        return self.health > 0
