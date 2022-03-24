# First exercise!!!!!!!!!!!!!!!
#from random import choice
#n1 = str(input('First student: '))
#n2 = str(input('Second Student: '))
#n3 = str(input('Third Student: '))
#n4 = str(input('Fourth Student: '))
#list = [n1, n2, n3, n4]
#chosen = choice(list)
#print('The chosen student is', chosen)

import random
n1 = str(input('First student: '))
n2 = str(input('Second Student: '))
n3 = str(input('Third Student: '))
n4 = str(input('Fourth Student: '))
list = [n1, n2, n3, n4]
random.shuffle(list)
print('The presentation order is', list)
