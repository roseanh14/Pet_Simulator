from animals.pet import Pet
from animals.dog import Dog
from animals.cat import Cat
from animals.parrot import Parrot
import inquirer
import random

def show_status(pet: Pet):
    print(f"\n=== {pet.name} ===")
    print(f"Hunger: {pet.hunger} | Energy: {pet.energy} | Happiness: {pet.happiness}\n")

def choose_pet(pets):
    if len(pets) == 1:
        return pets[0]
    answer = inquirer.prompt([
        inquirer.List(
            'pet',
            message="Pick a pet",
            choices=[p.name for p in pets],
        )
    ])
    chosen = answer['pet']
    for p in pets:
        if p.name == chosen:
            return p

def menu(pets):
    current = choose_pet(pets)

    actions = [
        ("Feed the pet", "feed"),
        ("Play with the pet", "play"),
        ("Let the pet sleep", "sleep"),
        ("Advance to the next day (random events)", "next_day"),
        ("Show current pet status", "status"),
        ("Show pet statistics", "stats"),
        ("Switch pet", "switch"),
        ("Exit", "exit"),
    ]

    while True:
        answer = inquirer.prompt([
            inquirer.List(
                'action',
                message=f"What do you want to do with {current.name}?",
                choices=[label for (label, _) in actions],
            )
        ])
        key = dict(actions)[answer['action']]

        if key == "feed":
            current.feed()
            show_status(current)
        elif key == "play":
            current.play()
            show_status(current)
        elif key == "sleep":
            current.sleep()
            show_status(current)
        elif key == "next_day":
            # „den“ = 1–3 náhodné události
            for _ in range(random.randint(1, 3)):
                current.random_event()
            show_status(current)
        elif key == "status":
            show_status(current)
        elif key == "stats":
            current.show_stats()
        elif key == "switch":
            current = choose_pet(pets)
        elif key == "exit":
            break

def main():
    pets = [
        Dog("Rex"),
        Cat("Mia"),
        Parrot("Polly"),
    ]
    menu(pets)

if __name__ == "__main__":
    main()