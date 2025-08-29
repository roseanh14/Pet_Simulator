from .pet import Pet


class Parrot(Pet):
    def __init__(self, name, hunger=50, energy=50, happiness=15, instincts=None):
        super().__init__(name, hunger, energy, happiness, instincts)

    def make_sound(self):
        print("Hello!")

    def repeat_word(self, word):
        print(word)
