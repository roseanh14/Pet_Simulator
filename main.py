class Pet:
    def __init__(self, name, hunger= 50 , energy = 50  ,happiness = 15 , instincts = None):
        self.name = name
        self.hunger = max(0,min(100,hunger))
        self.energy = max(0,min(100,energy))
        self.happiness = max(0,min(100,happiness))
        self.instincts = list(instincts) if instincts is not None else []

    def feed(self):
        self.hunger = max(0, self.hunger -10)
    
    def play (self): 
        self.energy = max(0, self.energy - 10)
        self.happiness = max(0,self.happiness + 10)
    
    def sleep(self):
        self.energy = max(0, self.energy + 10)

    def __str__(self):
        instincts_formatted = ", ".join(self.instincts)
        return (f"Pet : {self.name}\n"
               f"Hunger: {self.hunger}\n"
               f"Energy: {self.energy}\n"
               f"Happiness: {self.happiness}\n"
               f"Instincts: {instincts_formatted}")

my_pet = Pet("Joseph", 20 , 15, 10, ["hunt", "climb", "purr"])
my_pet.feed()
my_pet.play()
my_pet.sleep()

    
print(my_pet.name)
 #print(my_pet.hunger)
 #print(my_pet.energy)
print(my_pet.happiness)
print(my_pet.instincts)


pet_default = Pet("Mia",hunger = 50, energy = 50, happiness=20 ,instincts=["purr", "climb"])
print(pet_default)

pet_default = Pet("Mai", happiness=20, instincts=["meow", "sip"])
print(pet_default)