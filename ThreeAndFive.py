#Author: Susan Liu
#Class: CS325
#Assignment: 1
#Date: 9/28/2021


#ask for input
num = input("Please input in a number\n")

print("You have chose number ",num)
num = int(num)

if num >= 8:
    #seperate number into 3x and 5y
    y = num//5
    #print("Y: ",y)
    
    total=num-(y*5)
    #print(total)
    
    x=total//3
    #print("X: ",x)
    
    t=num-((5*y)+(3*x))
    #print("MAYBE 8? ", t)
    
    while t!=0:
      y=y-1
      totall=num-(y*5)
      x=totall//3
      #print(x)
      t=num-((5*y)+(3*x))
      #print("T: ",t)
    
    #calculate how many 3 and 5 there are
    #print("3X: ",x)
    #print("5Y: ",y)
    tuple=(x,y)
    print(tuple)

else:
    print("Your number is not greater or equal to 8")
