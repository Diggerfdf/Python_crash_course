def make_shirt(message='I love Python', size='Large'):
    """Sumarize the shirt that's going to be made."""
    print("\nI'm going to make a {} size T-Shirt.".format(size.capitalize()))
    print('It will say: {}'.format(message.title()))

make_shirt()  
make_shirt('I love Python!')
make_shirt('Shirt Happens!')
make_shirt(message='Readability counts.', size='medium')
