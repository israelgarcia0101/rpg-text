from player import Player
from events import events
from enemy import Enemy
import random
import os

os.system("cls")

player = Player(input("enter your name: "))
enemy = Enemy("monster")

os.system("cls")

class Navigation:
    def showOptions(self):
        print("MENU:")
        print("1. explore")
        print("2. check stats")
        print("3. inventory")
        print("4. shop")
        print("5. exit game")

        option = self.retrieveOption()
        if option == 1:
            os.system("cls")
            game = Game()
            game.exploreEvents()
            self.askContinue(game)
        elif option == 2:
            os.system("cls")
            player.show_stats()
            self.BackToMenu()
        elif option == 3:
            os.system("cls")
            self.inventory_interface()

    def askContinue(self, game):
        choice1 = input("want to continue exploring? y/n: ")
        if choice1 == "y":
            os.system("cls")
            game.exploreEvents()
            self.askContinue(game)
        elif choice1 == "n":
            os.system("cls")
            self.showOptions()
        else:
            print("invalid, try again")
            self.askContinue(game)

    def retrieveOption(self):
        try:
            return int(input("choice: "))
        except:
            print("invalid option")

    def inventory_interface(self):
        print("INVENTORY: ")
        for item in player.inventory:
            print(item)
        if "potion - heals 25HP" in player.inventory:
            choice2 = input("use potion? y/n: ")
            if choice2 == "y":
                if player.health < 100:
                    old_health = player.health
                    player.inventory.remove("potion - heals 25HP")
                    os.system("cls")
                    player.heal(25)
                    if player.health > 100:
                        player.health = 100
                    print('you used "potion"')
                    if player.health < 100:
                        print("your health went from", old_health, "to", player.health)
                        self.BackToMenu()
                    if player.health == 100:
                        print("HP maxed out!")
                        self.BackToMenu()
                else:
                    os.system("cls")
                    print("HP already maxed.")
                    self.BackToMenu()
            elif choice2 == "n":
                os.system("cls")
                self.BackToMenu()
        else:
            self.BackToMenu()
    def BackToMenu(self):
        input("back to menu (input anything): ")
        os.system("cls")
        self.showOptions()


class Game:
    def exploreEvents(self):
        event = random.choice(events)
        if event == events[0]:
            self.fight()
        if event == events[1]:
            coins1 = random.randint(5, 50)
            print("You found", coins1, "coins!")
            player.add_coins(coins1)
        if event == events[2]:
            print("You found a potion!")
            player.inventory.append("potion - heals 25HP")
        if event == events[3]:
            print("nothing but the wind...")

    def fight(self):
        self.fightInterface()
        while enemy.is_alive() and player.is_alive:
            choice4 = self.retreiveoption2()
            if choice4 == 1:
                self.attack()
            if choice4 == 2:
                print("check")
            if choice4 == 3:
                print("check")

    def retreiveoption2(self):
        try:
           return int(input("choice: "))
        except:
            print("invalid input")

    def attack(self):
        roll = random.randint(1, 100)
        if roll == 67:
            os.system("cls")
            print("BLACK FLASH!!!")
            enemy.take_damage(100)
            print("enemy vaporized.")
        elif 1 <= roll <= 10:
            os.system("cls")
            print("you attacked the enemy...")
            print("Critical hit!")
            enemy.take_damage(45)
            print("you dealt 45 DMG!")
        else:
            os.system("cls")
            print("you attacked the enemy...")
            enemy.take_damage(15)
            print("you dealt 15 DMG!")
        self.backToFight()
    def fightInterface(self):
        print("A monster blocked your way!!")
        print("your hp:", player.health)
        print("monster hp:", enemy.health)
        print("what do you wish to do?")
        print("1. attack")
        print("2. potion")
        print("3. run")

    def backToFight(self):
        input("continue (input anything): ")
        os.system("cls")
        self.fightInterface()
