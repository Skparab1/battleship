# Battleship

# print all the lines
def printarena():
    global c1,c2,c3,c4,c5,c6,c7,c8,c9,c10, l1,l2,l3,l4,l5,l6,l7,l8,l9,l10
    print('\n'*50)
    print('          Your board               Computer\'s board   \n')
    print('    A B C D E F G H I J            A B C D E F G H I J   ')
    print('    _____________________         ______________________ ')
    print('1  |'+l1+'|         |'+c1+'|  1')
    print('2  |'+l2+'|         |'+c2+'|  2')
    print('3  |'+l3+'|         |'+c3+'|  3')
    print('4  |'+l4+'|         |'+c4+'|  4')
    print('5  |'+l5+'|         |'+c5+'|  5')
    print('6  |'+l6+'|         |'+c6+'|  6')
    print('7  |'+l7+'|         |'+c7+'|  7')
    print('8  |'+l8+'|         |'+c8+'|  8')
    print('9  |'+l9+'|         |'+c9+'|  9')
    print('10 |'+l10+'|         |'+c10+'|  10')
    print('   |____________________|         |____________________|\n\n')

def removeship1():
    global l1,l2,l3,l4,l5,l6,l7,l8,l9,l10
    l1,l2,l3,l4,l5,l6,l7,l8,l9,l10 = l1.replace('^',' '),l2.replace('^',' '),l3.replace('^',' '),l4.replace('^',' '),l5.replace('^',' '),l6.replace('^',' '),l7.replace('^',' '),l8.replace('^',' '),l9.replace('^',' '),l10.replace('^',' ')

def adds1(line):
    global ship1pos
    pos = ship1pos*2
    linepart1 = line[:pos]
    linepart2 = line[pos+1:]
    line = linepart1 + '^' + linepart2
    return line

# initialise line variables
l1,l2,l3,l4,l5,l6,l7,l8,l9,l10 = ' '*20,' '*20,' '*20,' '*10 + '^' + ' '*9,' '*10 + '^' + ' '*9,' '*10 + '^' + ' '*9,' '*20,' '*20,' '*20,' '*20
c1,c2,c3,c4,c5,c6,c7,c8,c9,c10 = ' '*20,' '*20,' '*20,' '*20,' '*20,' '*20,' '*20,' '*20,' '*20,' '*20
choice = 'start'
ship1pos = 5
height = 3

while choice != 'done':
    printarena()
    print('position your ship')
    print('press WASD keys followed by enter to move your ship')
    #print('press t to turn your ship') Sorry, turning does not work yet
    print('type done and enter when you are done')
    print(height)
    choice = input('')
    choice = choice.lower()
    if choice == 'w':
        height = (height - 1 if height > 0 else height)
        ln = height
        removeship1()
        l1,l2,l3,l4,l5,l6,l7,l8 = (adds1(l1) if ln == 0 else l1), (adds1(l2) if (ln == 1 or ln == 0) else l2), (adds1(l3) if (ln == 2 or ln == 1 or ln == 0) else l3), (adds1(l4) if (ln == 3 or ln == 2 or ln == 1) else l4), (adds1(l5) if (ln == 4 or ln == 3 or ln == 2) else l5), (adds1(l6) if (ln == 5 or ln == 4 or ln == 3) else l6), (adds1(l7) if (ln == 6 or ln == 5 or ln == 4) else l7), (adds1(l8) if (ln == 7 or ln == 6 or ln == 5) else l8)
        if ln == 8 or ln == 7 or ln == 6:
            l9 = adds1(l9)
        if ln == 9 or ln == 8 or ln == 7:
            l10 = adds1(l10)
        #l9,l10 = (adds1(l9) if (ln == 8 if ln == 7 if ln == 6) else l9), (adds1(l10) if (ln == 9 or ln == 8 or ln == 7) else l10) 
    if choice == 's':
        height = (height + 1 if height < 10 else height)
        ln = height
        removeship1()
        l1,l2,l3,l4,l5,l6,l7,l8 = (adds1(l1) if ln == 0 else l1), (adds1(l2) if (ln == 1 or ln == 0) else l2), (adds1(l3) if (ln == 2 or ln == 1 or ln == 0) else l3), (adds1(l4) if (ln == 3 or ln == 2 or ln == 1) else l4), (adds1(l5) if (ln == 4 or ln == 3 or ln == 2) else l5), (adds1(l6) if (ln == 5 or ln == 4 or ln == 3) else l6), (adds1(l7) if (ln == 6 or ln == 5 or ln == 4) else l7), (adds1(l8) if (ln == 7 or ln == 6 or ln == 5) else l8)
        if ln == 8 or ln == 7 or ln == 6:
            l9 = adds1(l9)
        if ln == 9 or ln == 8 or ln == 7:
            l10 = adds1(l10)
    if choice == 'a':
        ship1pos = (ship1pos - 1 if ship1pos > 0 else ship1pos)
        ln = height
        removeship1()
        l1,l2,l3,l4,l5,l6,l7,l8 = (adds1(l1) if ln == 0 else l1), (adds1(l2) if (ln == 1 or ln == 0) else l2), (adds1(l3) if (ln == 2 or ln == 1 or ln == 0) else l3), (adds1(l4) if (ln == 3 or ln == 2 or ln == 1) else l4), (adds1(l5) if (ln == 4 or ln == 3 or ln == 2) else l5), (adds1(l6) if (ln == 5 or ln == 4 or ln == 3) else l6), (adds1(l7) if (ln == 6 or ln == 5 or ln == 4) else l7), (adds1(l8) if (ln == 7 or ln == 6 or ln == 5) else l8)
        if ln == 8 or ln == 7 or ln == 6:
            l9 = adds1(l9)
        if ln == 9 or ln == 8 or ln == 7:
            l10 = adds1(l10)
    if choice == 'd':
        ship1pos = (ship1pos + 1 if ship1pos < 10 else ship1pos)
        ln = height
        removeship1()
        l1,l2,l3,l4,l5,l6,l7,l8 = (adds1(l1) if ln == 0 else l1), (adds1(l2) if (ln == 1 or ln == 0) else l2), (adds1(l3) if (ln == 2 or ln == 1 or ln == 0) else l3), (adds1(l4) if (ln == 3 or ln == 2 or ln == 1) else l4), (adds1(l5) if (ln == 4 or ln == 3 or ln == 2) else l5), (adds1(l6) if (ln == 5 or ln == 4 or ln == 3) else l6), (adds1(l7) if (ln == 6 or ln == 5 or ln == 4) else l7), (adds1(l8) if (ln == 7 or ln == 6 or ln == 5) else l8)
        if ln == 8 or ln == 7 or ln == 6:
            l9 = adds1(l9)
        if ln == 9 or ln == 8 or ln == 7:
            l10 = adds1(l10)