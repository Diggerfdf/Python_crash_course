def make_shirt(size, message):
    """Sumarize the shirt that's going to be made."""
    print("\nI'm going to make a {} size T-Shirt.".format(size.capitalize()))
    print('It will say: {}'.format(message.title()))
    
make_shirt('large', 'I love Python!')
make_shirt(message='Readability counts.', size='medium')
