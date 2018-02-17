def make_car(manufacturer, model, **options):
    """Build a dictionary that contains information about a car."""
    car_dict = {'manufacturer': manufacturer.title(),
                'model': model.title(),
                }
    for option, value in options.items():
        car_dict[option] = value
    return car_dict

user_car = make_car('Fiat', 'Palio', 
                    color = 'Dark green',
                    portas = 2,
                    motor = 1.0)
                    
print(user_car)
