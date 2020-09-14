# Author          : Ma. Giselle N. Regaspi
# Course and Year : BS IT-2
# Filename        : Regaspi_probb.py
# Description     : a program that reads an integer $n$ and prints the sequence 
#					$F_n$ of Fibonacci numbers as a comma-separated 
#					list on a single line.
# Honor Code      : I have not given nor received any unathorized help in
#                   completing this exercise. I am also well aware of the 
#                   policies stipulated in the AdNU student handbook.


T = int(input()) #test cases
count = 1
i = 1 # index

while (i < T): # stop when the iteration reach the test cases
    n = int(input())
    
    print("CASES", count,":", end=" ") # display the iteration
    count += 1 # counts the number of iteration 
    
    i += 1 # increment by 1
    
    f0 = 0 #fisrt term
    f1 = 1 # second term
    
    if n == 1:  # automatically prints 0 if the value of n is 1
        print(f0)
    elif n >= 2: # perform when the number is greater than 2
        print("{},{}".format(f0,f1),end="")
        for i in range(2, n):
            fn = f0 + f1  #the next term would be the sum of first and second term
            print(",{}".format(fn),end="")
            f0 = f1  # f0 takes the value of f1
            f1 = fn  # while the f1 takes the value of fn
        