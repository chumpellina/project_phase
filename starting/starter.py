import random
import sys
import os

print ("ciao bella")
print ("5**3 = ", 5**3)
my_dictionary = { 'egy' : 'flóra', 'kettő' : 'menyus', 'három' : 'lófasz'}
print (my_dictionary.values())

age = 200

if age < 20 :
    print ("hello")
else :
    print ("bello")

random_num = random.randrange (0, 50)
while (random_num != 10):
    print (random_num)
    random_num = random.randrange(0,50)

name = sys.stdin.readline ()

print ('Hello, ', name)



