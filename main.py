class Pet:
    def __init__(self, name, hunger, energy):
        self.name = name
        self.hunger = max(0,min(100,hunger))
        self.energy = max(0,min(100,energy))

my_pet = Pet("Joseph", 20 , 15)

print(my_pet.name)
print(my_pet.hunger)
print(my_pet.energy)