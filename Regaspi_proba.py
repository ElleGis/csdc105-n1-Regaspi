# Author          : Ma. Giselle N. Regaspi
# Course and Year : BS IT-2
# Filename        : Regaspi_proba.py
# Description     : A program that prints a triangle shape composed of specific ASCII character.
# Honor Code      : I have not given nor received any unathorized help in
#                   completing this exercise. I am also well aware of the 
#                   policies stipulated in the AdNU student handbook.


T = int(input()) # number of test cases
count = 1        
i = 0
j = 0
s=0

while(i < T): # it continously iterate until the program stop
    k = int(input()) # input the height of the triangle 
    c = str(input()) # ASCII character
    
    print ("CASES", count, ": ")
    count = count + 1 # count the number of iteration
  
    temp = k # k was assigned to a temporary variable 
    i += 1   # increment by 1
  
    for j in range  (0, k): # An outer loop that iterate the number of rows
        for s in range(0, temp - j + 1): # inner loop, handles the number of columns. it depends on the outer loop
           print(end=" ")
        for s in range (0, 2 * j + 1):  # add new line after each row. 
            print (c,  end=" ") # display the pattern
        print()
        temp -= 1 # decrement 
    