from user import Admin

fabiano = Admin('fabiano', 'ferreira', 'f_ferreira', 'diggerfdf@gmail.com', 'são paulo')
fabiano.describe_user()

fabiano_privileges = [
    'Can reset passwords',
    'Can moderate discussions',
    'Can suspend accounts',
    ]

fabiano.privileges.privileges = fabiano_privileges

print("\nThe admin " + fabiano.username + " has these privileges: ")
fabiano.privileges.show_privileges()
