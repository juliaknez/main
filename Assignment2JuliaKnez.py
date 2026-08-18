import random

#I Julia Knez, 001249434, certify that this work is my own effort and that I have not allowed anyone else to copy from it.

amount = random.randint(0,20) + round( random.randint(0,100)/100, 2 )

print (amount)

payment = float(input("Customer payment: "))
#assume payment is greater than amount

change = payment - amount

if change == 0:
    print ("No change owed.") #If payment exactly equals amount
else:
    #initiate coin variables
    d = 0
    q = 0
    i = 0
    n = 0
    #calculating dollars owed in change
    d = int(change // 1)
    change = change - d 
    if change == 0:
        print ("You got " + str(d) + " dollars back in change.")
    else:
        #calculating number of quarters owed in change
        q = int (change/0.25)
        change = change - (q*0.25)
        #calculating the number of dimes owed in change
        i = int (change/0.10)
        change = change - (i*0.10)
        #calculating the number of nickels owed in change
        n = int (change/0.05)
        change = change - (n*0.05)
        n = n + round(change*2, 1)*10
        print ("You got " + str(d) + " dollars, " +str(q) + " quarters, " +str(i) + " dimes, and " + str(int(n)) + " nickels back in change.")
        
#end of program 
