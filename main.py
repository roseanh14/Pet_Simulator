from animals.pet import Pet
from animals.dog import Dog
from animals.cat import Cat
from animals.parrot import Parrot
import inquirer
from database.database_manager_usage import create_tables, create_pet, load_pet_by_name, log_activity


def show_status(pet: Pet):
    print(f"\n=== {pet.name} ===")
    print(f"Hunger: {pet.hunger} | Energy: {pet.energy} | Happiness: {pet.happiness}\n")


def choose_pet(pets):
    if len(pets) == 1:
        return pets[0]
    answer = inquirer.prompt(
        [
            inquirer.List(
                "pet",
                message="Pick a pet",
                choices=[p.name for p in pets] + ["Back", "Exit"],
            )
        ]
    )
    if not answer or "pet" not in answer or answer["pet"] == "Exit":
        return None
    if answer["pet"] == "Back":
        return "BACK"
    chosen = answer["pet"]
    for p in pets:
        if p.name == chosen:
            return p


def menu(pets):
    current = None
    while current is None or current == "BACK":
        current = choose_pet(pets)
        if current is None:
            return
        if current == "BACK":
            continue


    actions = [
        ("Feed the pet", "feed"),
        ("Play with the pet", "play"),
        ("Let the pet sleep", "sleep"),
        ("Advance to the next day (random events)", "next_day"),
        ("Show current pet status", "status"),
        ("Show pet statistics", "stats"),
        ("Switch pet", "switch"),
        ("Back", "back"),
        ("Exit", "exit"),
    ]

    while True:
        answer = inquirer.prompt(
            [
                inquirer.List(
                    "action",
                    message=f"What do you want to do with {current.name}?",
                    choices=[label for (label, _) in actions],
                )
            ]
        )
        if not answer or "action" not in answer:
            print("Cancelled.")
            return

        key = dict(actions)[answer["action"]]

        if key == "feed":
            before = (current.hunger, current.energy, current.happiness)
            current.feed()
            after = (current.hunger, current.energy, current.happiness)
            log_activity(
                create_pet(current.name, current.__class__.__name__.lower(), before[0], before[1], before[2]),
                "feed",
                dh=after[0] - before[0],
                de=after[1] - before[1],
                dhap=after[2] - before[2],
            )
            show_status(current)
        elif key == "play":
            before = (current.hunger, current.energy, current.happiness)
            current.play()
            after = (current.hunger, current.energy, current.happiness)
            log_activity(
                create_pet(current.name, current.__class__.__name__.lower(), before[0], before[1], before[2]),
                "play",
                dh=after[0] - before[0],
                de=after[1] - before[1],
                dhap=after[2] - before[2],
            )
            show_status(current)
        elif key == "sleep":
            before = (current.hunger, current.energy, current.happiness)
            current.sleep()
            after = (current.hunger, current.energy, current.happiness)
            log_activity(
                create_pet(current.name, current.__class__.__name__.lower(), before[0], before[1], before[2]),
                "sleep",
                dh=after[0] - before[0],
                de=after[1] - before[1],
                dhap=after[2] - before[2],
            )
            show_status(current)
        elif key == "next_day":
            before = (current.hunger, current.energy, current.happiness)
            current.next_day_events()
            after = (current.hunger, current.energy, current.happiness)
            log_activity(
                create_pet(current.name, current.__class__.__name__.lower(), before[0], before[1], before[2]),
                "next_day",
                dh=after[0] - before[0],
                de=after[1] - before[1],
                dhap=after[2] - before[2],
            )
            show_status(current)
        elif key == "status":
            show_status(current)
        elif key == "stats":
            current.show_stats()
        elif key == "switch":
            chosen = choose_pet(pets)
            if chosen is None:
                return
            if chosen != "BACK":
                current = chosen
        elif key == "back":
            return
        elif key == "exit":
            return


def construct_pet_from_record(rec):
    species = rec["species"].lower()
    name = rec["name"]
    hunger = rec["hunger"]
    energy = rec["energy"]
    happiness = rec["happiness"]
    if species == "dog":
        return Dog(name, hunger, energy, happiness)
    if species == "cat":
        return Cat(name, hunger, energy, happiness)
    if species == "parrot":
        return Parrot(name, hunger, energy, happiness)
    return Pet(name, hunger, energy, happiness)


def create_or_load_pet():
    choices = ["Create new pet", "Load pet from database", "Back", "Exit"]
    answer = inquirer.prompt([inquirer.List("choice", message="Choose an option", choices=choices)])
    if not answer or "choice" not in answer:
        return None
    choice = answer["choice"]
    if choice == "Exit":
        return None
    if choice == "Back":
        return "BACK"
    if choice == "Create new pet":
        species = inquirer.prompt([inquirer.List("species", message="Choose species", choices=["dog", "cat", "parrot", "Back", "Exit"])])
        if not species or species["species"] in ("Back", "Exit"):
            return "BACK"
        name_ans = inquirer.prompt([inquirer.Text("name", message="Pet name")])
        if not name_ans or not name_ans.get("name"):
            return "BACK"
        name = name_ans["name"]
        pid = create_pet(name, species["species"])
        rec = load_pet_by_name(name)
        pet = construct_pet_from_record(rec)
        return pet
    if choice == "Load pet from database":
        name_ans = inquirer.prompt([inquirer.Text("name", message="Existing pet name")])
        if not name_ans or not name_ans.get("name"):
            return "BACK"
        rec = load_pet_by_name(name_ans["name"])
        if not rec:
            print("Pet not found.")
            return "BACK"
        return construct_pet_from_record(rec)


def main():
    create_tables() 
    pets = []
    while True:
        pet = create_or_load_pet() 
        if pet is None:
            break
        if pet == "BACK":
            continue
        pets.append(pet)
        more = inquirer.prompt([inquirer.List("more", message="Add another pet?", choices=["Yes", "No", "Back", "Exit"])])
        if not more or more["more"] in ("No", "Exit"):
            break
        if more["more"] == "Back":
            pets.pop()
            continue
    if not pets:
        return
    menu(pets)


if __name__ == "__main__":
    main()