import math
import random as rd
user_number = int(input('Enter a number of your choice between [0 and 9]: '))
system_number = rd.randint(0,10)
if system_number == user_number:
	print('CrorePati')
else:
	print('RoadPati')