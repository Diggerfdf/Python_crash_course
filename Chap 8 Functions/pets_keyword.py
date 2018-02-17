def describe_pet(pet_name, animal_type):
    """Display information about a pet."""
    print("\nI have a " + animal_type + ".")
    print("My " + animal_type + "'s name is " + pet_name.title() + ".")
    
# A dog named Willie.
describe_pet('MelindA', "cat")
describe_pet('harry', 'dog')
describe_pet('Flipper', 'dolphin')
