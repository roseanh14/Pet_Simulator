from animals.pet import Pet
from animals.dog import Dog
from animals.cat import Cat
from animals.parrot import Parrot
from database.database_manager import DatabaseManager


pets = [Dog("REX"), Cat("MIA"), Parrot("MAI")]


def interact_with_pets(pets):
    for x in pets:
        x.make_sound()
        x.random_event()
        if isinstance(x, Parrot):
            x.repeat_word("Polly wants a cracker!")


def main():
    # interact_with_pets(pets)

    db = DatabaseManager()
    rex_id = db.create_pet("REX", "Dog", hunger=60, energy=50, happiness=40)
    db.log_activity(rex_id, "FEED", dh=-10)
    db.log_activity(rex_id, "PLAY", de=-5, dhap=+10)
    state = db.get_current_state(rex_id)
    print("REX:", state)

    db.close()

if __name__ == "__main__":
    main()
