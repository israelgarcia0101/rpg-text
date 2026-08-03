class Player:
    def __init__(self, name):
        self.name = name
        self.health = 60
        self.coins = 0
        self.inventory = []
    def take_damage(self, amount):
        self.health -= amount
    def heal(self, amount):
        self.health += amount
    def add_coins(self, amount):
        self.coins += amount
    def is_alive(self):
        return self.health > 0
    def show_stats(self):
        print("name:", self.name)
        print("HP:", self.health)
        print("coins:", self.coins)