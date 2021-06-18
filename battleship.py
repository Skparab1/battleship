# Battleship

# print all the lines
def printarena():
    global c1,c2,c3,c4,c5,c6,c7,c8,c9,c10, l1,l2,l3,l4,l5,l6,l7,l8,l9,l10
    print('      Your board      |       |  Computer\'s board   |')
    print('______________________         _______________________')
    print('|'+l1+'|         |'+c1+'|')
    print('|'+l2+'|         |'+c2+'|')
    print('|'+l3+'|         |'+c3+'|')
    print('|'+l4+'|         |'+c4+'|')
    print('|'+l5+'|         |'+c5+'|')
    print('|'+l6+'|         |'+c6+'|')
    print('|'+l7+'|         |'+c7+'|')
    print('|'+l8+'|         |'+c8+'|')
    print('|'+l9+'|         |'+c9+'|')
    print('|'+l10+'|         |'+c10+'|')
    print('|____________________|         |____________________|')

# initialise line variables
l1,l2,l3,l4,l5,l6,l7,l8,l9,l10 = ' '*20,' '*20,' '*20,' '*20,' '*20,' '*20,' '*20,' '*20,' '*20,' '*20
c1,c2,c3,c4,c5,c6,c7,c8,c9,c10 = ' '*20,' '*20,' '*20,' '*20,' '*20,' '*20,' '*20,' '*20,' '*20,' '*20
choice = 'start'

while choice != 'done':
    print('position your ships')
    printarena()
    choice = input('press')
