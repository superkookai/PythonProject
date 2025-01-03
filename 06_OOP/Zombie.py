from Enemy import *
import random

class Zombie(Enemy):
    def __init__(self, health_points, attack_damage):
        super().__init__("Zombie",health_points,attack_damage)

    # Override method
    def talk(self):
        print("*Grumbling...*")

    # New Method only for Zombie class
    def spread_infection(self):
        print("Zombie try to spread infection!")

    def special_attack(self):
        did_special_attack_work = random.random() < 0.5
        if did_special_attack_work:
            self.attack_damage += 2
            print("Zombie generated 2 HP!")