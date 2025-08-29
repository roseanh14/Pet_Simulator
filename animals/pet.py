from exceptions import (
    InvalidHungerValueError,
    InvalidEnergyValueError,
    InvalidHappinessValueError,
)
import random


class Pet:
    def __init__(self, name, hunger=50, energy=50, happiness=15, instincts=None):
        self._name = name
        self._instincts = list(instincts) if instincts is not None else []
        self.hunger = hunger
        self.energy = energy
        self.happiness = happiness

        self.stats = {
            "fed": 0,
            "played": 0,
            "slept": 0,
            "illness": 0,
            "fatigue": 0,
        }

    @property
    def name(self):
        return self._name

    @property
    def hunger(self):
        return self._hunger

    @hunger.setter
    def hunger(self, value):
        if not 0 <= value <= 100:
            raise InvalidHungerValueError(f"Hunger must be between 0-100, got {value}")
        self._hunger = value

    @property
    def energy(self):
        return self._energy

    @energy.setter
    def energy(self, value):
        if not 0 <= value <= 100:
            raise InvalidEnergyValueError(f"Energy must be between 0-100, got {value}")
        self._energy = value

    @property
    def happiness(self):
        return self._happiness

    @happiness.setter
    def happiness(self, value):
        if not 0 <= value <= 100:
            raise InvalidHappinessValueError(
                f"Happiness must be between 0-100, got {value}"
            )
        self._happiness = value

    @property
    def instincts(self):
        return list(self._instincts)


    def _validate_0_100(self, value, field="value"):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{field} must be a number")
        if value != value:
            raise ValueError(f"{field} cant be NaN.")

        if value < 0:
            return 0
        if value > 100:
            return 100
        return int(value)

    def random_event(self):
        event = random.choice(["illness", "sleep", "cuddling"])

        if event == "illness":
            self.energy = max(0, self.energy - 15)
            self.happiness = max(0, self.happiness - 10)
            print(f"Oh no!  {self.name} got sick. Energy -15, Happiness -10 ")

        elif event == "sleep":
            self.energy = max(0, self.energy - 5)
            print(f"Oh no! {self.name} feels sleepy! Energy - 5")

        else:
            print(f"{self.name} is doing fine cuddling today!")

    def feed(self, amount=10):
        self.hunger = self._validate_0_100(self.hunger - amount, "hunger")
        self.happiness = self._validate_0_100(self.happiness + 3, "happiness")
        self.stats["fed"] += 1
        print(f"{self.name} was fed. Hunger -{amount}, Happiness +3")

    def play(self, effort=10):
        self.energy = self._validate_0_100(self.energy - effort, "energy")
        self.happiness = self._validate_0_100(self.happiness + 7, "happiness")
        self.hunger = self._validate_0_100(self.hunger + 5, "hunger")
        self.stats["played"] += 1
        print(f"{self.name} played. Energy -{effort}, Happiness +7, Hunger +5")

    def sleep(self, duration=15):
        self.energy = self._validate_0_100(self.energy + duration, "energy")
        self.hunger = self._validate_0_100(self.hunger + 3, "hunger")
        self.stats["slept"] += 1
        print(f"{self.name} slept. Energy +{duration}, Hunger +3")
    
    def random_event(self):
        event = random.choice(["illness", "fatigue", "cuddling"])
        if event == "illness":
            self.energy = max(0, self.energy - 15)
            self.happiness = max(0, self.happiness - 10)
            self.stats["illness"] += 1
            print(f"Oh no! {self.name} got sick. Energy -15, Happiness -10")
        elif event == "fatigue":
            self.energy = max(0, self.energy - 5)
            self.stats["fatigue"] += 1
            print(f"Oh no! {self.name} feels fatigued! Energy -5")
        else:
            print(f"{self.name} is doing fine cuddling today!")

    def show_stats(self):
        print(f"\n=== Stats for {self.name} ===")
        print(f"Fed:       {self.stats['fed']}")
        print(f"Played:    {self.stats['played']}")
        print(f"Slept:     {self.stats['slept']}")
        print(f"Illness:   {self.stats['illness']}")
        print(f"Fatigue:   {self.stats['fatigue']}")
        print(f"Current -> Hunger: {self.hunger}, Energy: {self.energy}, Happiness: {self.happiness}\n")
