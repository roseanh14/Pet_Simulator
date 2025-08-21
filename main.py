from pet import Pet
from animals.dog import Dog
from animals.cat import Cat
from animals.parrot import Parrot
from exceptions import InvalidHungerValueError

# my_pet = Pet("Joseph", 20 , 15, 10, ["hunt", "climb", "purr"])
# my_pet.feed()
# my_pet.play()
# my_pet.sleep()


# print(my_pet.name)
# print(my_pet.hunger)
# print(my_pet.energy)
# print(my_pet.happiness)
# print(my_pet.instincts)


# pet_default = Pet("Mia",hunger = 50, energy = 50, happiness=20 ,instincts=["purr", "climb"])
# print(pet_default)

# pet_default = Pet("Mai", happiness=20, instincts=["meow", "sip"])
# rint(pet_default)

# my_pet = Pet("Mia")

# my_pet.hunger = 5
# print(my_pet.hunger)

# my_pet.hunger = 150
# print(my_pet.hunger)

pets = [Dog("REX"), Cat("MIA"), Parrot("MAI")]


def interact_with_pets(pets):
    for x in pets:
        x.make_sound()
        if isinstance(x, Parrot):
            x.repeat_word("Polly wants a cracker!")


def main():
    interact_with_pets(pets)

    # testing exceptions
    try:
        p = Pet("MIA")
        p.hunger = 150
    except InvalidHungerValueError as e:
        print("Catched:", e)


if __name__ == "__main__":
    main()


# my_dog = Dog("REX")
# my_dog.make_sound()


# my_cat = Cat("MIA")
# my_cat.make_sound()

# my_parrot = Parrot("MAI")
# my_parrot.make_sound()
