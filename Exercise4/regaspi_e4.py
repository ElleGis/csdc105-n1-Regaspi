# Author          : Ma. Giselle N. Regaspi
# Course and Year : BS IT - 2
# Filename        : regaspi_e4.py
# Description     : This program must read three (3) numbers, comma separated. 
#                   Your program must then check if these numbers are valid 
#                   side lengths of a triangle. If so, your program must compute 
#                   the triangle’s perimeter and area using the functions defined 
#                   in the `geometry` module and display these results. Otherwise, 
#                   your program must issue an error.
# Honor Code      : I have not given nor received any unathorized help in
#                   completing this exercise. I am also well aware of the 
#                   policies stipulated in the AdNU student handbook.

import geometry
import math 
	
print("Enter the side lengths of a triangle: ", end=" ") #Prompt the user to enter the side lengths of a triangle
a,b,c = map(float, input().split(",")) #declare the varibles as float and read it  and separate it by a comma using the funtion split()
side_lengths = a,b,c #assigned the values to a temporary variable side_lengths

if geometry.check_If_Valid(a, b, c): #returns the perimeter and area of a triangle if the side lengths is valid
	print("Perimeter: ", round(geometry.perimeter(*side_lengths),2)) #display the perimeter by calling the function created in the module and round it off to two decimals 
	print("Area: ", round(geometry.triangle_heronsarea(a, b, c),2)) #display the area of triangle by calling the function created in the module and round it off to two decimals
else:
	print("Invalid input") # if the sum of the two side is less than the other sides it display "Invalid input" 
	
	