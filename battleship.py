# Battleship

from math import trunc
import random, time
from random import randint,randrange

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

def removeship2():
    global l1,l2,l3,l4,l5,l6,l7,l8,l9,l10
    l1,l2,l3,l4,l5,l6,l7,l8,l9,l10 = l1.replace('O',' '),l2.replace('O',' '),l3.replace('O',' '),l4.replace('O',' '),l5.replace('O',' '),l6.replace('O',' '),l7.replace('O',' '),l8.replace('O',' '),l9.replace('O',' '),l10.replace('O',' ')

def adds2(line):
    global ship2pos
    pos = ship2pos*2
    linepart1 = line[:pos]
    linepart2 = line[pos+1:]
    line = linepart1 + 'O' + linepart2
    return line

def removeship3():
    global l1,l2,l3,l4,l5,l6,l7,l8,l9,l10
    l1,l2,l3,l4,l5,l6,l7,l8,l9,l10 = l1.replace('+',' '),l2.replace('+',' '),l3.replace('+',' '),l4.replace('+',' '),l5.replace('+',' '),l6.replace('+',' '),l7.replace('+',' '),l8.replace('+',' '),l9.replace('+',' '),l10.replace('+',' ')

def adds3(line):
    global ship3pos
    pos = ship3pos*2
    linepart1 = line[:pos]
    linepart2 = line[pos+1:]
    line = linepart1 + '+' + linepart2
    return line

def addhit(line,pos):
    pos = (pos-1)*2
    linepart1 = line[:pos]
    linepart2 = line[pos+1:]
    line = linepart1 + 'X' + linepart2
    return line

def addmiss(line,pos):
    pos = (pos-1)*2
    linepart1 = line[:pos]
    linepart2 = line[pos+1:]
    line = linepart1 + '-' + linepart2
    return line

# initialise line variables
l1,l2,l3,l4,l5,l6,l7,l8,l9,l10 = ' '*20,' '*20,' '*20,' '*10 + '^' + ' '*9,' '*10 + '^' + ' '*9,' '*10 + '^' + ' '*9,' '*20,' '*20,' '*20,' '*20
c1,c2,c3,c4,c5,c6,c7,c8,c9,c10 = ' '*20,' '*20,' '*20,' '*20,' '*20,' '*20,' '*20,' '*20,' '*20,' '*20
choice = 'start'
ship1pos = 5
height = 3

while choice != '':
    printarena()
    print('position your first ship')
    print('press WASD keys followed by enter to move your ship')
    #print('press t to turn your ship') Sorry, turning does not work yet
    print('press enter when you are done')
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
        ship1pos = (ship1pos + 1 if ship1pos < 9 else ship1pos)
        ln = height
        removeship1()
        l1,l2,l3,l4,l5,l6,l7,l8 = (adds1(l1) if ln == 0 else l1), (adds1(l2) if (ln == 1 or ln == 0) else l2), (adds1(l3) if (ln == 2 or ln == 1 or ln == 0) else l3), (adds1(l4) if (ln == 3 or ln == 2 or ln == 1) else l4), (adds1(l5) if (ln == 4 or ln == 3 or ln == 2) else l5), (adds1(l6) if (ln == 5 or ln == 4 or ln == 3) else l6), (adds1(l7) if (ln == 6 or ln == 5 or ln == 4) else l7), (adds1(l8) if (ln == 7 or ln == 6 or ln == 5) else l8)
        if ln == 8 or ln == 7 or ln == 6:
            l9 = adds1(l9)
        if ln == 9 or ln == 8 or ln == 7:
            l10 = adds1(l10)

ship2pos = (5 if ship1pos != 5 else 3)
height2 = 3
choice = 'reset'

while choice != '':
    ln = height2
    l1,l2,l3,l4,l5,l6,l7,l8 = (adds2(l1) if ln == 0 else l1), (adds2(l2) if (ln == 1 or ln == 0) else l2), (adds2(l3) if (ln == 2 or ln == 1 or ln == 0) else l3), (adds2(l4) if (ln == 3 or ln == 2 or ln == 1) else l4), (adds2(l5) if (ln == 4 or ln == 3 or ln == 2) else l5), (adds2(l6) if (ln == 5 or ln == 4 or ln == 3) else l6), (adds2(l7) if (ln == 6 or ln == 5 or ln == 4) else l7), (adds2(l8) if (ln == 7 or ln == 6 or ln == 5) else l8)
    printarena()
    print('position your second ship')
    print('press WASD keys followed by enter to move your ship')
    #print('press t to turn your ship') Sorry, turning does not work yet
    print('press enter when you are done')
    print(height2)
    choice = input('')
    choice = choice.lower()

    if choice == 'w':
        height2 = (height2 - 1 if height2 > 0 else height2)
        ln = height2
        removeship2()
        l1,l2,l3,l4,l5,l6,l7,l8 = (adds2(l1) if ln == 0 else l1), (adds2(l2) if (ln == 1 or ln == 0) else l2), (adds2(l3) if (ln == 2 or ln == 1 or ln == 0) else l3), (adds2(l4) if (ln == 3 or ln == 2 or ln == 1) else l4), (adds2(l5) if (ln == 4 or ln == 3 or ln == 2) else l5), (adds2(l6) if (ln == 5 or ln == 4 or ln == 3) else l6), (adds2(l7) if (ln == 6 or ln == 5 or ln == 4) else l7), (adds2(l8) if (ln == 7 or ln == 6 or ln == 5) else l8)
        if ln == 8 or ln == 7 or ln == 6:
            l9 = adds2(l9)
        if ln == 9 or ln == 8 or ln == 7:
            l10 = adds2(l10)

    if choice == 's':
        height2 = (height2 + 1 if height2 < 10 else height2)
        ln = height2
        removeship2()
        l1,l2,l3,l4,l5,l6,l7,l8 = (adds2(l1) if ln == 0 else l1), (adds2(l2) if (ln == 1 or ln == 0) else l2), (adds2(l3) if (ln == 2 or ln == 1 or ln == 0) else l3), (adds2(l4) if (ln == 3 or ln == 2 or ln == 1) else l4), (adds2(l5) if (ln == 4 or ln == 3 or ln == 2) else l5), (adds2(l6) if (ln == 5 or ln == 4 or ln == 3) else l6), (adds2(l7) if (ln == 6 or ln == 5 or ln == 4) else l7), (adds2(l8) if (ln == 7 or ln == 6 or ln == 5) else l8)
        if ln == 8 or ln == 7 or ln == 6:
            l9 = adds2(l9)
        if ln == 9 or ln == 8 or ln == 7:
            l10 = adds2(l10)

    if choice == 'a':
        ship2pos = (ship2pos - 1 if ship2pos > 0 else ship2pos)
        ln = height2
        removeship2()
        l1,l2,l3,l4,l5,l6,l7,l8 = (adds2(l1) if ln == 0 else l1), (adds2(l2) if (ln == 1 or ln == 0) else l2), (adds2(l3) if (ln == 2 or ln == 1 or ln == 0) else l3), (adds2(l4) if (ln == 3 or ln == 2 or ln == 1) else l4), (adds2(l5) if (ln == 4 or ln == 3 or ln == 2) else l5), (adds2(l6) if (ln == 5 or ln == 4 or ln == 3) else l6), (adds2(l7) if (ln == 6 or ln == 5 or ln == 4) else l7), (adds2(l8) if (ln == 7 or ln == 6 or ln == 5) else l8)
        if ln == 8 or ln == 7 or ln == 6:
            l9 = adds2(l9)
        if ln == 9 or ln == 8 or ln == 7:
            l10 = adds2(l10)

    if choice == 'd':
        ship2pos = (ship2pos + 1 if ship2pos < 9 else ship2pos)
        ln = height2
        removeship2()
        l1,l2,l3,l4,l5,l6,l7,l8 = (adds2(l1) if ln == 0 else l1), (adds2(l2) if (ln == 1 or ln == 0) else l2), (adds2(l3) if (ln == 2 or ln == 1 or ln == 0) else l3), (adds2(l4) if (ln == 3 or ln == 2 or ln == 1) else l4), (adds2(l5) if (ln == 4 or ln == 3 or ln == 2) else l5), (adds2(l6) if (ln == 5 or ln == 4 or ln == 3) else l6), (adds2(l7) if (ln == 6 or ln == 5 or ln == 4) else l7), (adds2(l8) if (ln == 7 or ln == 6 or ln == 5) else l8)
        if ln == 8 or ln == 7 or ln == 6:
            l9 = adds2(l9)
        if ln == 9 or ln == 8 or ln == 7:
            l10 = adds2(l10)

ship3pos = 5 if (ship1pos != 5 and ship2pos != 5) else (3 if (ship1pos != 3 and ship2pos != 3) else 7)
height3 = 3
choice = 'reset'

while choice != '':
    ln = height3
    l1,l2,l3,l4,l5,l6,l7,l8 = (adds3(l1) if ln == 0 else l1), (adds3(l2) if (ln == 1 or ln == 0) else l2), (adds3(l3) if (ln == 2 or ln == 1 or ln == 0) else l3), (adds3(l4) if (ln == 3 or ln == 2 or ln == 1) else l4), (adds3(l5) if (ln == 4 or ln == 3 or ln == 2) else l5), (adds3(l6) if (ln == 5 or ln == 4 or ln == 3) else l6), (adds3(l7) if (ln == 6 or ln == 5 or ln == 4) else l7), (adds3(l8) if (ln == 7 or ln == 6 or ln == 5) else l8)
    printarena()
    print('position your third ship')
    print('press WASD keys followed by enter to move your ship')
    #print('press t to turn your ship') Sorry, turning does not work yet
    print('press enter when you are done')
    print(height2)
    choice = input('')
    choice = choice.lower()

    if choice == 'w':
        height3 = (height3 - 1 if height3 > 0 else height3)
        ln = height3
        removeship3()
        l1,l2,l3,l4,l5,l6,l7,l8 = (adds3(l1) if ln == 0 else l1), (adds3(l2) if (ln == 1 or ln == 0) else l2), (adds3(l3) if (ln == 2 or ln == 1 or ln == 0) else l3), (adds3(l4) if (ln == 3 or ln == 2 or ln == 1) else l4), (adds3(l5) if (ln == 4 or ln == 3 or ln == 2) else l5), (adds3(l6) if (ln == 5 or ln == 4 or ln == 3) else l6), (adds3(l7) if (ln == 6 or ln == 5 or ln == 4) else l7), (adds3(l8) if (ln == 7 or ln == 6 or ln == 5) else l8)
        if ln == 8 or ln == 7 or ln == 6:
            l9 = adds3(l9)
        if ln == 9 or ln == 8 or ln == 7:
            l10 = adds3(l10)

    if choice == 's':
        height3 = (height3 + 1 if height3 < 10 else height3)
        ln = height3
        removeship3()
        l1,l2,l3,l4,l5,l6,l7,l8 = (adds3(l1) if ln == 0 else l1), (adds3(l2) if (ln == 1 or ln == 0) else l2), (adds3(l3) if (ln == 2 or ln == 1 or ln == 0) else l3), (adds3(l4) if (ln == 3 or ln == 2 or ln == 1) else l4), (adds3(l5) if (ln == 4 or ln == 3 or ln == 2) else l5), (adds3(l6) if (ln == 5 or ln == 4 or ln == 3) else l6), (adds3(l7) if (ln == 6 or ln == 5 or ln == 4) else l7), (adds3(l8) if (ln == 7 or ln == 6 or ln == 5) else l8)
        if ln == 8 or ln == 7 or ln == 6:
            l9 = adds3(l9)
        if ln == 9 or ln == 8 or ln == 7:
            l10 = adds3(l10)

    if choice == 'a':
        ship3pos = (ship3pos - 1 if ship3pos > 0 else ship3pos)
        ln = height3
        removeship3()
        l1,l2,l3,l4,l5,l6,l7,l8 = (adds3(l1) if ln == 0 else l1), (adds3(l2) if (ln == 1 or ln == 0) else l2), (adds3(l3) if (ln == 2 or ln == 1 or ln == 0) else l3), (adds3(l4) if (ln == 3 or ln == 2 or ln == 1) else l4), (adds3(l5) if (ln == 4 or ln == 3 or ln == 2) else l5), (adds3(l6) if (ln == 5 or ln == 4 or ln == 3) else l6), (adds3(l7) if (ln == 6 or ln == 5 or ln == 4) else l7), (adds3(l8) if (ln == 7 or ln == 6 or ln == 5) else l8)
        if ln == 8 or ln == 7 or ln == 6:
            l9 = adds3(l9)
        if ln == 9 or ln == 8 or ln == 7:
            l10 = adds3(l10)

    if choice == 'd':
        ship3pos = (ship3pos + 1 if ship3pos < 9 else ship3pos)
        ln = height3
        removeship3()
        l1,l2,l3,l4,l5,l6,l7,l8 = (adds3(l1) if ln == 0 else l1), (adds3(l2) if (ln == 1 or ln == 0) else l2), (adds3(l3) if (ln == 2 or ln == 1 or ln == 0) else l3), (adds3(l4) if (ln == 3 or ln == 2 or ln == 1) else l4), (adds3(l5) if (ln == 4 or ln == 3 or ln == 2) else l5), (adds3(l6) if (ln == 5 or ln == 4 or ln == 3) else l6), (adds3(l7) if (ln == 6 or ln == 5 or ln == 4) else l7), (adds3(l8) if (ln == 7 or ln == 6 or ln == 5) else l8)
        if ln == 8 or ln == 7 or ln == 6:
            l9 = adds3(l9)
        if ln == 9 or ln == 8 or ln == 7:
            l10 = adds3(l10)

# finding out your coordinates
yourcoords, ship1pos, ship2pos, ship3pos, height, height2, height3 = '', ship1pos + 1, ship2pos + 1, ship3pos + 1, height + 1, height2 + 1, height3 + 1

ls1 = 'a' if ship1pos == 1 else ('b' if ship1pos == 2 else ('c' if ship1pos == 3 else ('d' if ship1pos == 4 else ('e' if ship1pos == 5 else ('f' if ship1pos == 6 else ('g' if ship1pos == 7 else ('h' if ship1pos == 8 else ('i' if ship1pos == 9 else 'j'))))))))
yourcoords = yourcoords + ' ' + ls1 + str(height) + ' ' + ls1 + str(height+1) + ' ' + ls1 + str(height+2)

ls2 = 'a' if ship2pos == 1 else ('b' if ship2pos == 2 else ('c' if ship2pos == 3 else ('d' if ship2pos == 4 else ('e' if ship2pos == 5 else ('f' if ship2pos == 6 else ('g' if ship2pos == 7 else ('h' if ship2pos == 8 else ('i' if ship2pos == 9 else 'j'))))))))
yourcoords = yourcoords + ' ' + ls2 + str(height2) + ' ' + ls2 + str(height2+1) + ' ' + ls2 + str(height2+2)

ls3 = 'a' if ship3pos == 1 else ('b' if ship3pos == 2 else ('c' if ship3pos == 3 else ('d' if ship3pos == 4 else ('e' if ship3pos == 5 else ('f' if ship3pos == 6 else ('g' if ship3pos == 7 else ('h' if ship3pos == 8 else ('i' if ship3pos == 9 else 'j'))))))))
yourcoords = yourcoords + ' ' + ls3 + str(height3) + ' ' + ls3 + str(height3+1) + ' ' + ls3 + str(height3+2)

print(yourcoords)


printarena()

print('\n\nBattleship')
input('press enter to begin')

# computer picking random coordinates for ships
coordinates = ''
letterstr = 'abcdefghij'
letter = letterstr[randint(0,9)]
num = (randint(3,9))
num2 = str(num-1)
num3 = str(num-2)
ship1coords = '        ' + letter+str(num)+letter+num2+letter+num3
coordinates = coordinates + ship1coords

letterstr = letterstr.replace(letter,'')
letter = letterstr[randint(0,8)]
num = (randint(3,9))
num2 = str(num-1)
num3 = str(num-2)
ship2coords = '        ' + letter+str(num)+letter+num2+letter+num3
coordinates = coordinates + ship2coords

letterstr = letterstr.replace(letter,'')
letter = letterstr[randint(0,7)]
num = (randint(3,9))
num2 = str(num-1)
num3 = str(num-2)
ship3coords = '        ' + letter+str(num)+letter+num2+letter+num3
coordinates = coordinates + ship3coords

print(coordinates)

won = False
toprint = ''
guessedcoords = ''
hitships = 0
stringofcoords = 'a1 a2 a3 a4 a5 a6 a7 a8 a9 a10 b1 b2 b3 b4 b5 b6 b7 b8 b9 b10 c1 c2 c3 c4 c5 c6 c7 c8 c9 c10 d1 d2 d3 d4 d5 d6 d7 d8 d9 d10 e1 e2 e3 e4 e5 e6 e7 e8 e9 e10 f1 f2 f3 f4 f5 f6 f7 f8 f9 f10 g1 g2 g3 g4 g5 g6 g7 g8 g9 g10 h1 h2 h3 h4 h5 h6 h7 h8 h9 h10 i1 i2 i3 i4 i5 i6 i7 i8 i9 i10 j1 j2 j3 j4 j5 j6 j7 j8 j9 j10'
hits, misses, sinks = 0,0,0
grato = False
chs, lasthit, lastcoord = 0, False, ''
compplayed, chits = '', 0

while won != True:
    try:

        if grato == True:
            # computer play

            print(' The computer is playing'), time.sleep(1.5)

            # picking random coordinate 
            if lasthit == False: 
                letterstr = 'abcdefghij'
                letter = letterstr[randint(0,9)]
                num = (randint(3,9))
                randcoord = letter+str(num)
                while randcoord in compplayed:
                    letter = letterstr[randint(0,9)]
                    num = (randint(3,9))
                    randcoord = letter+str(num)
            
            else:
                l = lastcoord[-1]
                h = lastcoord[0]
                l = int(l)
                l += 1
                l = str(l)
                randcoord = h+l
                while randcoord in compplayed:
                    l = int(l) + randint(-1,1)
                    randcoord = h+str(l)

            if randcoord in yourcoords:
                lasthit = True
                lastcoord = randcoord
                toprint = 'computer has hit one of your ships'
                coordinate = str(randcoord)
                chs += 1
                chits += 1

                l = int(coordinate[-1])
                h = coordinate[0]

                hh = 1 if h == 'a' else (2 if h == 'b' else (3 if h == 'c' else (4 if h == 'd' else (5 if h == 'e' else (6 if h == 'f' else (7 if h == 'g' else (8 if h == 'h' else (9 if h == 'i' else (0)))))))))
            
                ln = l
            
                l1,l2,l3,l4,l5,l6,l7,l8,l9,l10 = (addhit(l1,hh) if ln == 1 else l1), (addhit(l2,hh) if ln == 2 else l2), (addhit(l3,hh) if ln == 3 else l3), (addhit(l4,hh) if ln == 4 else l4), (addhit(l5,hh) if ln == 5 else l5), (addhit(l6,hh) if ln == 6 else l6), (addhit(l7,hh) if ln == 7 else l7), (addhit(l8,hh) if ln == 8 else l8), (addhit(l9,hh) if ln == 9 else l9), (addhit(l10,hh) if ln == 0 else l10)

            else:
                toprint = 'computer has missed'
                coordinate = str(randcoord)

                l = int(coordinate[-1])
                h = coordinate[0]

                hh = 1 if h == 'a' else (2 if h == 'b' else (3 if h == 'c' else (4 if h == 'd' else (5 if h == 'e' else (6 if h == 'f' else (7 if h == 'g' else (8 if h == 'h' else (9 if h == 'i' else (0)))))))))
            
                ln = l
            
                l1,l2,l3,l4,l5,l6,l7,l8,l9,l10 = (addmiss(l1,hh) if ln == 1 else l1), (addmiss(l2,hh) if ln == 2 else l2), (addmiss(l3,hh) if ln == 3 else l3), (addmiss(l4,hh) if ln == 4 else l4), (addmiss(l5,hh) if ln == 5 else l5), (addmiss(l6,hh) if ln == 6 else l6), (addmiss(l7,hh) if ln == 7 else l7), (addmiss(l8,hh) if ln == 8 else l8), (addmiss(l9,hh) if ln == 9 else l9), (addmiss(l10,hh) if ln == 0 else l10)

            if chs == 3:
                chs = 0
                toprint = 'The computer has hit and sank a ship'
                lasthit = False

            randcoord = randcoord.replace(' ','')
            compplayed = randcoord + ' ' + compplayed

        grato = True

        printarena()
        print('- = miss     X = hit')
        print('\nHits: ',hits,'   misses: ', misses,'   sinks: ', sinks,'')
        print(toprint)
        toprint = ''

        coordinate = input('\ntype the coordinate of the point you want to fire. for example, a1 or b7. \n> ')
        coordinate = coordinate.replace(' ','')

        if hits >= 9:
            won = True
            print('You have hit all the computer\'s ships and won the game.')

        if chits >= 9:
            won = True
            print('The computer has hit all of your ships. you have lost')

        if (coordinate in coordinates) and (coordinate != '') and (coordinate != ' '):
            coordinate = str(coordinate)
            toprint = 'You hit a ship'
            hitships += 1
            hits += 1

            guessedcoords = guessedcoords + ' ' + coordinate
            l = int(coordinate[-1])
            h = coordinate[0]

            hh = 1 if h == 'a' else (2 if h == 'b' else (3 if h == 'c' else (4 if h == 'd' else (5 if h == 'e' else (6 if h == 'f' else (7 if h == 'g' else (8 if h == 'h' else (9 if h == 'i' else (0)))))))))
            
            ln = l
            
            c1,c2,c3,c4,c5,c6,c7,c8,c9,c10 = (addhit(c1,hh) if ln == 1 else c1), (addhit(c2,hh) if ln == 2 else c2), (addhit(c3,hh) if ln == 3 else c3), (addhit(c4,hh) if ln == 4 else c4), (addhit(c5,hh) if ln == 5 else c5), (addhit(c6,hh) if ln == 6 else c6), (addhit(c7,hh) if ln == 7 else c7), (addhit(c8,hh) if ln == 8 else c8), (addhit(c9,hh) if ln == 9 else c9), (addhit(c10,hh) if ln == 0 else c10)

            if hitships == 3:
                sinks += 1
                hitships = 0
                toprint = 'You have hit and sank a ship'
    
        elif (coordinate != '') and (coordinate != ' ') and (coordinate in stringofcoords) and coordinate not in guessedcoords:
            toprint = 'You missed'
            coordinate = str(coordinate)
            misses += 1
            guessedcoords = guessedcoords + ' ' + coordinate

            l = int(coordinate[-1])
            h = coordinate[0]

            hh = 1 if h == 'a' else (2 if h == 'b' else (3 if h == 'c' else (4 if h == 'd' else (5 if h == 'e' else (6 if h == 'f' else (7 if h == 'g' else (8 if h == 'h' else (9 if h == 'i' else (0)))))))))
            
            ln = l
            
            c1,c2,c3,c4,c5,c6,c7,c8,c9,c10 = (addmiss(c1,hh) if ln == 1 else c1), (addmiss(c2,hh) if ln == 2 else c2), (addmiss(c3,hh) if ln == 3 else c3), (addmiss(c4,hh) if ln == 4 else c4), (addmiss(c5,hh) if ln == 5 else c5), (addmiss(c6,hh) if ln == 6 else c6), (addmiss(c7,hh) if ln == 7 else c7), (addmiss(c8,hh) if ln == 8 else c8), (addmiss(c9,hh) if ln == 9 else c9), (addmiss(c10,hh) if ln == 0 else c10)

            #print('The computer is playing', end = ''), time.sleep(0.1), print('.', end = ''), time.sleep(0.1),print('.', end = ''), time.sleep(0.1), print('.', end = ''), time.sleep(0.1), print('.', end = ''),time.sleep(0.1), print('.', end = ''), time.sleep(0.1), print('.', end = ''), time.sleep(0.5)

        elif coordinate in guessedcoords and (coordinate != '') and (coordinate != ' '):
            toprint = 'You have already guessed that coordinate. try again'
            grato = False

        else:
            toprint = 'Invalid coordinate. try again'
            grato = False

        printarena()
        print('\nHits: ',hits,'   misses: ', misses,'   sinks: ', sinks,'\n')
        print(toprint)
    except:
        pass