from Enemy import *
from Zombie import *
from Orge import *
from Hero import *
from Weapon import *

# zombie = Enemy()
# zombie.type_of_enemy = "Zombie"
# print(f"{zombie.type_of_enemy} has {zombie.health_points} points and damage attack of {zombie.attack_damage}")
#
# zombie.talk()
# zombie.walk_forward()
# zombie.attack()

# big_zombie = Enemy("Big Zombie")
# now type_of_enemy is private, we cannot access outside class -> use Getter instead
# print(f"{big_zombie.type_of_enemy} has {big_zombie.health_points} points and damage attack of {big_zombie.attack_damage}")

# big_zombie.talk()
# big_zombie.walk_forward()
# big_zombie.attack()
#
# # Use Getter
# print(big_zombie.get_type_of_enemey())

# zombie = Zombie(10,1)
# print(zombie.get_type_of_enemey())
# zombie.talk() # override method
# zombie.walk_forward() # inherit method
# zombie.spread_infection() # method of Zombie class
#
# print("#### Orge")
# orge = Orge(15,2)
# print(orge.get_type_of_enemey())
# orge.talk()
# print(f"{orge.get_type_of_enemey()} has {orge.health_points} points and damage attack of {orge.attack_damage}")

## Polymorphism
# def battle(e: Enemy):
#     e.talk()
#     e.attack()
#
# anonymous = Enemy("Anonymous")
# zombie = Zombie(10,1)
# orge = Orge(15,2)
#
# enemies: [Enemy] = []
# enemies.append(anonymous)
# enemies.append(zombie)
# enemies.append(orge)
#
# for enemy in enemies:
#     battle(enemy)
#     print()

## Battle field!
def battle(e1: Enemy, e2: Enemy):
    e1.talk()
    e2.talk()

    while e1.health_points > 0 and e2.health_points > 0:
        print("----------------")
        e1.special_attack()
        e2.special_attack()
        print(f"{e1.get_type_of_enemey()}: {e1.health_points} HP left")
        print(f"{e2.get_type_of_enemey()}: {e2.health_points} HP left")
        e2.attack()
        e1.health_points -= e2.attack_damage
        e1.attack()
        e2.health_points -= e1.attack_damage

    if e1.health_points > 0:
        print(f"{e1.get_type_of_enemey()} win!")
    else:
        print(f"{e2.get_type_of_enemey()} win!")

# zombie = Zombie(10,1)
# orge = Orge(20,3)
# battle(zombie,orge)

## Hero Battle
def hero_battle(hero: Hero, enemy: Enemy):

    while hero.health_points > 0 and enemy.health_points > 0:
        print("----------------")
        print(f"Hero : {hero.health_points} HP left")
        print(f"{enemy.get_type_of_enemey()}: {enemy.health_points} HP left")
        enemy.special_attack()
        enemy.attack()
        hero.health_points -= enemy.attack_damage
        hero.attack()
        enemy.health_points -= hero.attack_damage

    if hero.health_points > 0:
        print("Hero win!")
    else:
        print(f"{enemy.get_type_of_enemey()} win!")

weapon = Weapon("Sword",5)
hero = Hero(10,1)
hero.weapon = weapon
hero.equip_weapon()

zombie = Zombie(10,1)

hero_battle(hero,zombie)