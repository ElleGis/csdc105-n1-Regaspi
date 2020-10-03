# Author          : Ma. Giselle N. Regaspi
# Course and Year : BS IT - 2
# Filename        : geometry.py
# Description     : Define a function that computes for the perimeter and 
#					area of a triangle and a function that checks if the 
#					side lengths of a triangle is valid or not.
# Honor Code      : I have not given nor received any unathorized help in
#                   completing this exercise. I am also well aware of the 
#                   policies stipulated in the AdNU student handbook.

import math

#A function compute for the perimeter of a triangle
def perimeter (*side_lengths):  
  P = (a + b + c)/2
  return P

#A function that computes for the area of a triangle	
def triangle_heronsarea (a, b, c):
  s = perimeter()
  A = math.sqrt(s*(s-a)*(s-b)*(s-c))
  return A

#A function that check if the side lenths of a triangle is valid
def check_If_Valid(a, b, c):    
	if (a + b > c) and (a + c > b) and (b + c > a): # if the sum of two sides are highest than the other one it returns true else false
		return True
	else:
		return False
	
	
	