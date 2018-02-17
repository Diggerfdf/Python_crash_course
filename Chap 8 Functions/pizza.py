def make_pizza(*toppings):
    """Sumarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza('Peperoni')
make_pizza('mushrooms', 'green pepers', 'extra cheese')


def make_pizza_2(size, *toppings):
    """Sumarize the Pizza we are about to make."""

    print("\nMaking a " + str(size) +
          "-inch pizza with the following toppings:")
    for topping in toppings:
        print("- " + topping)


make_pizza_2(16, 'peperoni')
make_pizza_2(12, 'mushrooms', 'green peppers', 'extra cheese')
