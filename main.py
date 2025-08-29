from animals.pet import Pet
from animals.dog import Dog
from animals.cat import Cat
from animals.parrot import Parrot

def menu(pet: Pet):
    while True:
        print(f"\n=== {pet.name} ===  (H:{pet.hunger} E:{pet.energy} Happy:{pet.happiness})")
        print("1) Feed")
        print("2) Play")
        print("3) Sleep")
        print("4) Random event")
        print("5) Show stats")
        print("0) Exit")
        choice = input("Choose: ").strip()

        if choice == "1":
            pet.feed()
        elif choice == "2":
            pet.play()
        elif choice == "3":
            pet.sleep()
        elif choice == "4":
            pet.random_event()
        elif choice == "5":
            pet.show_stats()
        elif choice == "0":
            break
        else:
            print("Unknown option.")

def main():
    Pet = Dog("Rex")
    menu(Pet)

if __name__ == "__main__":
    main()
