class Animal:
    __type_of_animal: str
    __legs_of_animal: int

    ## Python does not care about Types pass to parameters!!!
    def __init__(self, type_of_animal, legs_of_animal):
        self.__type_of_animal = type_of_animal
        self.__legs_of_animal = legs_of_animal
        print(f"{self.__type_of_animal} has {self.__legs_of_animal} legs. Created!")