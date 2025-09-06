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
        self.sick = False
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
            raise InvalidHappinessValueError(f"Happiness must be between 0-100, got {value}")
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

    def feed(self, amount=10):
        prev_hunger = self.hunger
        prev_energy = self.energy
        prev_happiness = self.happiness
        self.hunger = self._validate_0_100(self.hunger - amount, "hunger")
        energy_gain = max(1, amount // 2)
        self.energy = self._validate_0_100(self.energy + energy_gain, "energy")
        self.happiness = self._validate_0_100(self.happiness + 3, "happiness")
        self.stats["fed"] += 1
        print(f"{self.name} was fed. Hunger {prev_hunger}->{self.hunger}, Energy {prev_energy}->{self.energy}, Happiness {prev_happiness}->{self.happiness}")

    def play(self, effort=10):
        prev_energy = self.energy
        prev_happiness = self.happiness
        prev_hunger = self.hunger
        self.energy = self._validate_0_100(self.energy - effort, "energy")
        self.happiness = self._validate_0_100(self.happiness + 7, "happiness")
        self.hunger = self._validate_0_100(self.hunger + 5, "hunger")
        self.stats["played"] += 1
        print(f"{self.name} played. Energy {prev_energy}->{self.energy}, Happiness {prev_happiness}->{self.happiness}, Hunger {prev_hunger}->{self.hunger}")

    def sleep(self, duration=15):
        prev_energy = self.energy
        prev_hunger = self.hunger
        prev_happiness = self.happiness
        self.energy = self._validate_0_100(self.energy + duration, "energy")
        self.hunger = self._validate_0_100(self.hunger + 3, "hunger")
        delta_hap = random.choice([-10, -5, 0, 5, 10])
        self.happiness = self._validate_0_100(self.happiness + delta_hap, "happiness")
        self.stats["slept"] += 1
        print(f"{self.name} slept. Energy {prev_energy}->{self.energy}, Hunger {prev_hunger}->{self.hunger}, Happiness {prev_happiness}->{self.happiness}")

    def apply_event_kind(self, kind):
        if kind == "illness":
            prev_energy = self.energy
            prev_happiness = self.happiness
            self.energy = max(0, self.energy - 15)
            self.happiness = max(0, self.happiness - 10)
            self.sick = True
            self.stats["illness"] += 1
            print(f"Oh no! {self.name} got sick. Energy {prev_energy}->{self.energy}, Happiness {prev_happiness}->{self.happiness}")
        elif kind == "fatigue":
            prev_energy = self.energy
            self.energy = max(0, self.energy - 5)
            self.stats["fatigue"] += 1
            print(f"Oh no! {self.name} feels fatigued. Energy {prev_energy}->{self.energy}")
        elif kind == "cuddling":
            print(f"{self.name} is doing fine cuddling today!")
        return kind

    def random_event(self):
        kind = random.choice(["illness", "fatigue", "cuddling"])
        return self.apply_event_kind(kind)

    def next_day_events(self):
        self.sick = False
        pool = ["illness", "fatigue", "cuddling"]
        count = random.randint(1, 3)
        used = set()
        for _ in range(count):
            choices = [e for e in pool if e not in used]
            if not choices:
                break
            kind = random.choice(choices)
            used.add(kind)
            self.apply_event_kind(kind)
            if self.sick:
                break

    def show_stats(self):
        print(f"\n=== Stats for {self.name} ===")
        print(f"Fed:       {self.stats['fed']}")
        print(f"Played:    {self.stats['played']}")
        print(f"Slept:     {self.stats['slept']}")
        print(f"Illness:   {self.stats['illness']}")
        print(f"Fatigue:   {self.stats['fatigue']}")
        print(f"Current -> Hunger: {self.hunger}, Energy: {self.energy}, Happiness: {self.happiness}\n")