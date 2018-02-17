
'''
# Set a flag to indicate that polling is active.
choice = True
responses = {}

while choice: 
    # Prompt for the person's name and response.
    name = input("\nWhat is your name? ")
    place = input("If you could visit one place in the world, where it would it be? ")
    
    # Store the response in the dictionary:
    responses[name] = place
    
    # Find out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        choice = False
    
# Polling is complete. Show the results. 
print("\n --- Poll Results ---")
for name, place in responses.items():
    print("{} would like to visit {}.".format(name.title(), response.title()))'''


name_prompt = "\nWhat's your name? "
place_prompt = "If you could visit one place in the World, where would it be? "
continue_prompt = "\nWould you like to let someone else respond? (yes/no) "

# Responses will be stored in the form {name: place}.
responses = {}

while True: 
#     Ask the user where they'd like to go.
    name = input(name_prompt)
    place = input(place_prompt)
    
#     Store the response.
    responses[name] = place
    
#     Ask if there's anyone else responding.
    repeat = input(continue_prompt)
    if repeat != 'yes':
        break
# Show results of the survey.
print("\n-----Results-----")
for name, place in responses.items():
    print("{} would like to visit {}.".format(name.title(), place.title()))
