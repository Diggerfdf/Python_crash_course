requested_topping_0 = 'mushrooms'

if requested_topping_0 != 'anchovies':
    print("Hold the anchovies!")
    
requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + '.')
    print("\nFinished making your Pizza!")

else: 
    print("Are you sure you want a plain pizza?")
    
available_toppings = ['mushrooms', 'olives', 'green peppers', 
                        'peperoni', 'pineapple', 'extra cheese']

chosen_toppings = ['mushrooms', 'french fries', 'extra cheese']

for chosen_topping in chosen_toppings:
    if chosen_topping in available_toppings:
        print("Adding " + chosen_topping + ".")
    else: 
        print("Sorry, we don't have " + chosen_topping + ".")

print("\nFinished making your pizza!")
