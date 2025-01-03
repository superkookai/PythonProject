"""
1. Abstraction -- hide implementation from user, just use it
   [Constructor -- initialize an object]
2. Encapsulation -- encapsulate the data
3. Inheritance -- acquiring properties and functions from Parent class to Child class
    [Method overriding]
    [self -> refer to current object]
    [super -> refer to parent object]
4. Polymorphism -- to have many forms -- changing object at run time
"""

class Enemy:
    # Properties -> if have Parameters constructor no need to declare properties
    # type_of_enemy: str
    # health_points: int = 10
    # attack_damage: int = 1

    # Constructors
    # Empty or Default constructor created automatically if no define constructors
    # def __init__(self):
    #     pass
    def __init__(self):
        print("New enemy created without starting values")

    # Parameters constructor
    def __init__(self, type_of_enemy, health_points=10, attack_damage=1):
        self.__type_of_enemy = type_of_enemy # Private property
        self.health_points = health_points
        self.attack_damage = attack_damage

    # Getter and Setter
    def get_type_of_enemey(self):
        return self.__type_of_enemy

    # Functions
    def talk(self):
        print(f"I am {self.__type_of_enemy} be prepared to fight!")

    def walk_forward(self):
        print(f"{self.__type_of_enemy} walk closer to you!")

    def attack(self):
        print(f"{self.__type_of_enemy} attack for {self.attack_damage} damage!")

    def special_attack(self):
        print("Enemy has no special attack.")