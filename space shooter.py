# space shooter
import time, random
from random import randint

# printing all lines
def printlines():
    global balls,pos,line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18
    print(line18[1:100]),print(line17[1:100]),print(line16[1:100]),print(line15[1:100]),print(line14[1:100]),print(line13[1:100]),print(line12[1:100]),print(line11[1:100]),print(line10[1:100]),print(line9[1:100]),print(line8[1:100]),print(line7[1:100]),print(line6[1:100]),print(line5[1:100]),print(line4[1:100]),print(line3[1:100]),print(line2[1:100]),print(line1[1:100])
    print(' '*pos,' ||')
    print(' '*pos,' ||')
    print(' '*pos,'<||>')
    print(' '*pos,'<__>')

# removing ball from all lines
def removeballs():
    global balls,pos,line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18
    line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = line1.replace('-',' '),line2.replace('-',' '),line3.replace('-',' '),line4.replace('-',' '),line5.replace('-',' '),line6.replace('-',' '),line7.replace('-',' '),line8.replace('-',' '),line9.replace('-',' '),line10.replace('-',' '),line11.replace('-',' '),line12.replace('-',' '),line13.replace('-',' '),line14.replace('-',' '),line15.replace('-',' '),line16.replace('-',' '),line17.replace('-',' '),line18.replace('-',' ')
    line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = line1.replace('o',' '),line2.replace('o',' '),line3.replace('o',' '),line4.replace('o',' '),line5.replace('o',' '),line6.replace('o',' '),line7.replace('o',' '),line8.replace('o',' '),line9.replace('o',' '),line10.replace('o',' '),line11.replace('o',' '),line12.replace('o',' '),line13.replace('o',' '),line14.replace('o',' '),line15.replace('o',' '),line16.replace('o',' '),line17.replace('o',' '),line18.replace('o',' ')

# removing balls from line
def rb(line):
    line = line.replace('-oo-','    ')
    return line

# scans line for ball (NOT IN USE NOW)
def scanforball(line):
    scanner,num = '',0
    while scanner != '-oo-':
        scanner = line[num]
    if '-oo-' in line:
        num = 999
    return num

# removes arrow from all lines
def removearrow():
    global balls,pos,line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18
    line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = line1.replace('^',' '),line2.replace('^',' '),line3.replace('^',' '),line4.replace('^',' '),line5.replace('^',' '),line6.replace('^',' '),line7.replace('^',' '),line8.replace('^',' '),line9.replace('^',' '),line10.replace('^',' '),line11.replace('^',' '),line12.replace('^',' '),line13.replace('^',' '),line14.replace('^',' '),line15.replace('^',' '),line16.replace('^',' '),line17.replace('^',' '),line18.replace('^',' ')

# removes arrow from one line
def ra(line):
    line = line.replace('^',' ')
    return line

# adds ball to line
def addball(ballpos,line):
    linepart1 = line[:ballpos-1]
    linepart2 = line[ballpos+1:]
    line = linepart1 + '-oo- ' + linepart2
    return line

# adds arrow to line
def addarrow(arrowpos,line):
    linepart1 = line[:arrowpos-1]
    linepart2 = line[arrowpos+1:]
    line = linepart1 + '^ ' + linepart2
    return line

# moves balls in line down (if any). (new algorithm is in use, old one is commented out)
def movelinesdown():
    global balls,ballpos,line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18
    #linenum = 1 if ('o' in line1 ) else (2 if ('o' in line2 ) else (3 if ('o' in line3 ) else (4 if ('o' in line4 ) else (5 if ('o' in line5 ) else (6 if ('o' in line6 ) else (7 if ('o' in line7 ) else (8 if ('o' in line8 ) else (9 if ('o' in line9 ) else (10 if ('o' in line10 ) else (11 if ('o' in line11 ) else (12 if ('o' in line12 ) else (13 if ('o' in line13 ) else (14 if ('o' in line14 ) else (15 if ('o' in line15 ) else (16 if ('o' in line16 ) else (17 if ('o' in line17 ) else 18))))))))))))))))
    #removeballs()
    #line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = (addball(ballpos,line1) if linenum == 2 else line1),(addball(ballpos,line2) if linenum == 3 else line2),(addball(ballpos,line3) if linenum == 4 else line3),(addball(ballpos,line4) if linenum == 5 else line4),(addball(ballpos,line5) if linenum == 6 else line5),(addball(ballpos,line6) if linenum == 7 else line6),(addball(ballpos,line7) if linenum == 8 else line7),(addball(ballpos,line8) if linenum == 9 else line8),(addball(ballpos,line9) if linenum == 10 else line9),(addball(ballpos,line10) if linenum == 11 else line10),(addball(ballpos,line11) if linenum == 12 else line11),(addball(ballpos,line12) if linenum == 13 else line12),(addball(ballpos,line13) if linenum == 14 else line13),(addball(ballpos,line14) if linenum == 15 else line14),(addball(ballpos,line15) if linenum == 16 else line15),(addball(ballpos,line16) if linenum == 17 else line16),(addball(ballpos,line17) if linenum == 18 else line17),(addball(ballpos,line18) if linenum == False else line18)
    b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18 = True if '-oo-' in line1 else False,True if '-oo-' in line2 else False,True if '-oo-' in line3 else False,True if '-oo-' in line4 else False,True if '-oo-' in line5 else False,True if '-oo-' in line6 else False,True if '-oo-' in line7 else False,True if '-oo-' in line8 else False,True if '-oo-' in line9 else False,True if '-oo-' in line10 else False,True if '-oo-' in line11 else False,True if '-oo-' in line12 else False,True if '-oo-' in line13 else False,True if '-oo-' in line14 else False,True if '-oo-' in line15 else False,True if '-oo-' in line16 else False,True if '-oo-' in line17 else False,True if '-oo-' in line18 else False
    line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = (addball(ballpos,line1) if b2 == True else line1),(addball(ballpos,line2) if b3 == True else (rb(line2) if b2 == True else line2)),(addball(ballpos,line3) if b4 == True else (rb(line3) if b3 == True else line3)),(addball(ballpos,line4) if b5 == True else (rb(line4) if b5 == True else line4)),(addball(ballpos,line5) if b6 == True else (rb(line5) if b5 == True else line5)),(addball(ballpos,line6) if b7 == True else (rb(line6) if b6 == True else line6)),(addball(ballpos,line7) if b8 == True else (rb(line7) if b7 == True else line7)),(addball(ballpos,line8) if b9 == True else (rb(line8) if b8 == True else line8)),(addball(ballpos,line9) if b10 == True else (rb(line9) if b9 == True else line9)),(addball(ballpos,line10) if b11 == True else (rb(line10) if b10 == True else line10)),(addball(ballpos,line11) if b12 == True else (rb(line11) if b11 == True else line11)),(addball(ballpos,line12) if b13 == True else (rb(line12) if b12 == True else line12)),(addball(ballpos,line13) if b14 == True else (rb(line13) if b13 == True else line13)),(addball(ballpos,line14) if b15 == True else (rb(line14) if b14 == True else line14)),(addball(ballpos,line15) if b16 == True else (rb(line15) if b15 == True else line15)),(addball(ballpos,line16) if b17 == True else (rb(line16) if b16 == True else line16)),(addball(ballpos,line17) if b18 == True else (rb(line17) if b17 == True else line17)),(rb(line18) if b18 == True else line18)

# moves arrows in line up (if any). (new algorithm is in use, old one is commented out)
def moveup():
    global balls,arrowpos,line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18
    #linenum = 1 if ('^' in line1 ) else (2 if ('^' in line2 ) else (3 if ('^' in line3 ) else (4 if ('^' in line4 ) else (5 if ('^' in line5 ) else (6 if ('^' in line6 ) else (7 if ('^' in line7 ) else (8 if ('^' in line8 ) else (9 if ('^' in line9 ) else (10 if ('^' in line10 ) else (11 if ('^' in line11 ) else (12 if ('^' in line12 ) else (13 if ('^' in line13 ) else (14 if ('^' in line14 ) else (15 if ('^' in line15 ) else (16 if ('^' in line16 ) else (17 if ('^' in line17 ) else 18))))))))))))))))
    #removearrow()
    #line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = (addarrow(arrowpos,line2) if linenum == 1 else line2),(addarrow(arrowpos,line3) if linenum == 2 else line3),(addarrow(arrowpos,line4) if linenum == 3 else line4),(addarrow(arrowpos,line5) if linenum == 4 else line5),(addarrow(arrowpos,line6) if linenum == 5 else line6),(addarrow(arrowpos,line7) if linenum == 6 else line7),(addarrow(arrowpos,line8) if linenum == 7 else line8),(addarrow(arrowpos,line9) if linenum == 8 else line9),(addarrow(arrowpos,line10) if linenum == 9 else line10),(addarrow(arrowpos,line11) if linenum == 10 else line11),(addarrow(arrowpos,line12) if linenum == 11 else line12),(addarrow(arrowpos,line13) if linenum == 12 else line13),(addarrow(arrowpos,line14) if linenum == 13 else line14),(addarrow(arrowpos,line15) if linenum == 14 else line15),(addarrow(arrowpos,line16) if linenum == 15 else line16),(addarrow(arrowpos,line17) if linenum == 16 else line17),(addarrow(arrowpos,line18) if linenum == 17 else line18)
    b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13,b14,b15,b16,b17,b18 = True if '^' in line1 else False,True if '^' in line2 else False,True if '^' in line3 else False,True if '^' in line4 else False,True if '^' in line5 else False,True if '^' in line6 else False,True if '^' in line7 else False,True if '^' in line8 else False,True if '^' in line9 else False,True if '^' in line10 else False,True if '^' in line11 else False,True if '^' in line12 else False,True if '^' in line13 else False,True if '^' in line14 else False,True if '^' in line15 else False,True if '^' in line16 else False,True if '^' in line17 else False,True if '^' in line18 else False
    line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = (ra(line1) if b1 == True else line1),(addarrow(arrowpos,line2) if b1 == True else (ra(line2) if b2 == True else line2)),(addarrow(arrowpos,line3) if b2 == True else (ra(line3) if b3 == True else line3)),(addarrow(arrowpos,line4) if b3 == True else (ra(line4) if b4 == True else line4)),(addarrow(arrowpos,line5) if b4 == True else (ra(line5) if b5 == True else line5)),(addarrow(arrowpos,line6) if b5 == True else (ra(line6) if b6 == True else line6)),(addarrow(arrowpos,line7) if b6 == True else (ra(line7) if b7 == True else line7)),(addarrow(arrowpos,line8) if b7 == True else (ra(line8) if b8 == True else line8)),(addarrow(arrowpos,line9) if b8 == True else (ra(line9) if b9 == True else line9)),(addarrow(arrowpos,line10) if b9 == True else (ra(line10) if b10 == True else line10)),(addarrow(arrowpos,line11) if b10 == True else (ra(line11) if b11 == True else line11)),(addarrow(arrowpos,line12) if b11 == True else (ra(line12) if b12 == True else line12)),(addarrow(arrowpos,line13) if b12 == True else (ra(line13) if b13 == True else line13)),(addarrow(arrowpos,line14) if b13 == True else (ra(line14) if b14 == True else line14)),(addarrow(arrowpos,line15) if b14 == True else (ra(line15) if b15 == True else line15)),(addarrow(arrowpos,line16) if b15 == True else (ra(line16) if b16 == True else line16)),(addarrow(arrowpos,line17) if b16 == True else (ra(line17) if b17 == True else line17)),(addarrow(arrowpos,line18) if b17 == True else line18)

# initilaise variables
line1,line2,line3,line4,line5,line6,line7,line8,line9,line10,line11,line12,line13,line14,line15,line16,line17,line18 = ' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,' '*100,((' '*50)+'-oo-'+(' '*49)),' '*100,' '*100,' '*100,' '*100
pos = 50
ballpos = randint(45,55)
arrowpos = 50
balls = 25
movedirection = 'right'
alt = 0
score = 10

# intro
print('\n'*50)
print('Space Shooter Game')
print('How to play:')
print('1. Press control c to fire a ball')
print('2. You have 25 balls. you lose a ball when you fire it and gain 2 balls when you hit a spaceship')
print('3. You lose when an asteroid hits you (or when you run out of balls because then you can\'t fire at the asteroid')
input('press enter to begin')


while True:
    try:
        time.sleep(0.07)

        # move shooter left and right
        if movedirection == 'right':
            pos += 1
            if pos == 55:
                movedirection = 'left'
        if movedirection == 'left':
            pos -= 1
            if pos == 45:
                movedirection = 'right'

        # define line below and line below below
        linenum = 1 if ('-oo-' in line1 ) else (2 if ('-oo-' in line2 ) else (3 if ('-oo-' in line3 ) else (4 if ('-oo-' in line4 ) else (5 if ('-oo-' in line5 ) else (6 if ('-oo-' in line6 ) else (7 if ('-oo-' in line7 ) else (8 if ('-oo-' in line8 ) else (9 if ('-oo-' in line9 ) else (10 if ('-oo-' in line10 ) else (11 if ('-oo-' in line11 ) else (12 if ('-oo-' in line12 ) else (13 if ('-oo-' in line13 ) else (14 if ('-oo-' in line14 ) else (15 if ('-oo-' in line15 ) else (16 if ('-oo-' in line16 ) else (17 if ('-oo-' in line17 ) else 18))))))))))))))))
        printlines()
        lb = line1 if ('-oo-' in line1 ) else (line1 if ('-oo-' in line2 ) else (line2 if ('-oo-' in line3 ) else (line3 if ('-oo-' in line4 ) else (line4 if ('-oo-' in line5 ) else (line5 if ('-oo-' in line6 ) else (line6 if ('-oo-' in line7 ) else (line7 if ('-oo-' in line8 ) else (line8 if ('-oo-' in line9 ) else (line9 if ('-oo-' in line10 ) else (line10 if ('-oo-' in line11 ) else (line11 if ('-oo-' in line12 ) else (line12 if ('-oo-' in line13 ) else (line13 if ('-oo-' in line14 ) else (line14 if ('-oo-' in line15 ) else (line15 if ('-oo-' in line16 ) else (line16 if ('-oo-' in line17 ) else (line17 if ('-oo-' in line18 ) else line18)))))))))))))))))
        lbb = line1 if ('-oo-' in line1 ) else (line1 if ('-oo-' in line2 ) else (line1 if ('-oo-' in line3 ) else (line2 if ('-oo-' in line4 ) else (line3 if ('-oo-' in line5 ) else (line4 if ('-oo-' in line6 ) else (line5 if ('-oo-' in line7 ) else (line6 if ('-oo-' in line8 ) else (line7 if ('-oo-' in line9 ) else (line8 if ('-oo-' in line10 ) else (line9 if ('-oo-' in line11 ) else (line10 if ('-oo-' in line12 ) else (line11 if ('-oo-' in line13 ) else (line12 if ('-oo-' in line14 ) else (line13 if ('-oo-' in line15 ) else (line14 if ('-oo-' in line16 ) else (line15 if ('-oo-' in line17 ) else (line16 if ('-oo-' in line18 ) else line18)))))))))))))))))
        #print(lb)
        #input(lbb)

        # checks for arrow in line below and line below below
        if ('^' == lb[ballpos] or '^' == lb[ballpos+1] or '^' == lb[ballpos+2] or '^' == lb[ballpos+3]) or ('^' == lbb[ballpos] or '^' == lbb[ballpos+1] or '^' == lbb[ballpos+2] or '^' == lbb[ballpos+3]):
            removeballs()
            removeballs()
            removearrow()
            ballpos = randint(48,53)
            line18 = addball(ballpos,line18)
            balls += 2
            score += 10

        # move lines ever oither shooter movement
        if alt == 1:
            movelinesdown()
            moveup()
            alt = -1
        
        # moves ball a bit randomly, not in use right now
        if ballpos >= 53:
            ballpos -= 1
        elif ballpos <= 48:
            ballpos += 1
        elif randint(1,4) == 1:
            blank = '' #ballpos = ballpos + (randint(-1,1))

        # print score and arrows left
        print('Score: ',score)
        print('You have ',balls, ' Arrows: ','^'*balls)

        #print(pos)
        #moveup()

        # if you have been hit, break
        if '-oo-' in line1:
            print('you have been hit')
            break

        # tells it to move objects every other 0.1 sec
        alt += 1

    except: # when user presses control c

        if balls > 0: # fire a ball if the user is not out of balls
            arrowpos = pos + 5
            line1 = addarrow(arrowpos,line1)
            balls -= 1
            score -= 1

print('you have lost')
print('Your score was: ',score)