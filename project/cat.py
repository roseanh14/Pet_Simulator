from pet import Pet

class Cat(Pet):
    def __init__(self, name, hunger=50, energy=50, happiness=15, instincts=None):
        super().__init__(name, hunger, energy, happiness, instincts)
    
    def make_sound(self):
        print("Meow!")
