#coding=utf-8
'''
Created on 2015年11月11日

@author: quqiao
'''
number = 23
running = True

while running:
    guess = int(raw_input("Enter an integer:"))
    
    if guess == number:
        print"Congratulation,you guessed it."
        running = False #this causes the while loop to stop
    elif guess < number:
        print"No,it is a little higher than that"
    else:
        print"No,it is a little lower than that"
else:
    print"The while loop is over."
    #Do anything else you want to do here
print "Done"
        