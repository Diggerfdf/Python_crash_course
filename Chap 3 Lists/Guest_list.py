guest_list = ['Mary ShELLEy', 'Mark Twain', 'Érico Veríssimo', 
                'Karajan', 'BeEThoven', 'Joseph Campbell']
                
host = "Fabiano Dias Ferreira"
                
print(guest_list)

print()

print('Cara: ' + guest_list[0].title() + '. Você está sendo convidada a um jantar com '
                + host + '.\n\tPor favor confirme sua presença.')
                
print()
                
print('Caro: ' + guest_list[1].title() + '. Você está sendo convidado a um jantar com '
                + host + '.\n\tPor favor confirme sua presença.')
 
print()
                
print('Caro: ' + guest_list[2].title() + '. Você está sendo convidado a um jantar com '
                + host + '.\n\tPor favor confirme sua presença.')
                
print()
                
print('Caro: ' + guest_list[3].title() + '. Você está sendo convidado a um jantar com '
                + host + '.\n\tPor favor confirme sua presença.')
                
print()
                
print('Caro: ' + guest_list[4].title() + '. Você está sendo convidado a um jantar com '
                + host + '.\n\tPor favor confirme sua presença.')
                
print()

print('Caro: ' + guest_list[5].title() + '. Você está sendo convidado a um jantar com '
                + host + '.\n\tPor favor confirme sua presença.')
                
print('\n\n')
                
print('Infelizmente o senhor ' + guest_list[2] + ' nao poderá comparecer')

print('\n\n')
                
new_list = guest_list.pop(2)

guest_list.insert(2, 'Juvelino Pasqualino')

#guest_list = guest_list.insert(2, 'Juvelino Pasqualino')

print (guest_list)


guest_list.append('Otávio Marques de Assis')
guest_list.insert(0, 'Sandra Regina Marques')
guest_list.insert(3, 'Fabiano Dias Ferreira')


# 3-7 Shrinking Guest List

print(guest_list)

print('Sorry, I can only invite two people for dinner.')

a = guest_list.pop(1)

print(a + ' Desculpe-me você não poderá comparecer')
print(guest_list)

b = guest_list.pop(1)

print(b + ' Desculpe-me você não poderá comparecer')
print(guest_list)

c = guest_list.pop(2)

print(c + ' Desculpe-me você não poderá comparecer')
print(guest_list)

d = guest_list.pop(2)

print(d + ' Desculpe-me você não poderá comparecer')
print(guest_list)

print(guest_list[0] + ' Parabéns, você ainda está convidada')

print()

print(guest_list[1] + ' Parabéns, você ainda está convidado')

print(guest_list)

del guest_list[-1]
del guest_list[-1]
del guest_list[-1]
del guest_list[-1]
del guest_list[-1]

print(guest_list)
























































