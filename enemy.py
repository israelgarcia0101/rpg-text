class Enemy:
    def __init__(self, name):
        self.name = name
        self.health = 75
        self.damage = 18
    def take_damage(self, amount):
        self.health -= amount
    def is_alive(self):
        return self.health > 0