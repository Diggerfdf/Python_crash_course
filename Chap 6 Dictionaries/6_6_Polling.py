favorite_languages = {
    'jen': 'python', 
    'sarah': 'c', 
    'edward': 'ruby',
    'phil': 'python',
    }
    
coders = ['fabiano','phil', 'otávio', 'sandra', 'jen', 'edward']

for coder in coders:
    if coder in favorite_languages.keys():
        print("Thank you for taking the poll, " + coder.title() + "!")
    else:
        print(coder.title() + ", what's your favorite programming language?")
