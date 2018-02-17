def greet_users(names):
	"""Print a simple greeting to each user in the list."""
	for name in names: 
		msg = "Hello, {}!".format(name.title())
		print(msg)
		
usernames = ['HannAH', 'DiggeR', 'OtAcOn']
greet_users(usernames)
