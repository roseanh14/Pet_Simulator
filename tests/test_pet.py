from animals import Pet,Dog,Cat ,Parrot

def test_class_realationships():
    #animals should inherit from Pet
    assert issubclass (Dog, Pet)
    assert issubclass (Cat, Pet)
    assert issubclass (Parrot, Pet)

def test_can_construct_instances():
    #create instances and they keep their names
    rex=Dog("Rex")
    mia=Cat("Mia")
    polly=Parrot("Polly")

    assert rex.name == "Rex"
    assert mia.name == "Mia"
    assert polly.name == "Polly"

def test_call_methods_no_exeptions():
    #calling core methods should not raise exceptions
    pet=Pet("Any")
    pet.feed()
    pet.play()
    pet.sleep()
    pet.random_event()
    pet.show_stats()

def test_stats_has_expected_keys():
    #the stats dic should contain the expected counters 
    p=Pet("Any")
    expected={"fed","played","slept","illness","fatigue"}
    assert expected.issubset(set(p.stats.keys()))
