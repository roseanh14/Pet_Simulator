class Pet:
    def __init__(self, name, hunger, energy, happiness):
        self.name = name
        self.hunger = max(0,min(100,hunger))
        self.energy = max(0,min(100,energy))
        self.happiness = max(0,min(100,happiness))

    def feed(self):
        self.hunger = max(0, self.hunger -10)
    
    def play (self): 
        self.energy = max(0, self.energy - 10)
        self.happiness = max(0,self.happiness + 10)
    
    def sleep(self):
        self.energy = max(0, self.energy + 10)


my_pet = Pet("Joseph", 20 , 15, 10)
my_pet.feed()
my_pet.play()
my_pet.sleep()

    
print(my_pet.name)
 #print(my_pet.hunger)
 #print(my_pet.energy)
print(my_pet.happiness)


