prompt = "\nPlease choose a pizza topping: "
prompt += "\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    
    if topping != 'quit':
        print("     I'll add {} to your pizza.".format(topping))
    else:
        break
