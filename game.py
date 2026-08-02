from player import Player
from events import events
from enemy import Enemy
import random
import os

player = Player(input("enter your name: "))
enemy = Enemy("monster")
class Navigation:
    def showOptions(self):
        print("MENU:")
        print("1. explore")
        print("2. check stats")
        print("3. inventory")
        print("4. shop")
        print("5. exit game")

        option = self.retrieveOption()
        if option == 2:
            os.system("cls")
            player.show_stats()
            input("back to menu (input anything): ")
            os.system("cls")
            self.showOptions()
        elif option == 1:
            os.system("cls")
            game = Game()
            game.exploreEvents()
            self.askContinue(game)

    def askContinue(self, game):
        choice1 = input("want to continue? y/n: ")
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



class Game:
    def exploreEvents(self):
            event = random.choice(events)
            if event == events[0]:
                print("A monster blocked your way!!")
                print("your hp:", player.health, "monster hp:", enemy.health)
            if event == events[1]:
                coins1 = random.randint(5, 50)
                print("You found", coins1, "coins!")
                player.coins += coins1
            if event == events[2]:
                print("You found a potion")
            if event == events[3]:
                print("nothing but the wind...")