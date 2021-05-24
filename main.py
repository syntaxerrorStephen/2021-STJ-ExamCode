'''
Comp-Sci Example Q's

Donate Here:
paypal.me/

 -Change some variables if copying,
 -Uncomment to make code run,
 -Don't run code in this Repl
'''

# Q16 
from time import sleep
##############################
# Q16 (a)
# Student name: 
	
# Q16 (a) Section i (Comments)
# Thi program is a simple ordering system

# Q16 (a) Section ii (Input Statement)
userName = input("Please enter your username: ")

print("Welcome to the new online ordering system. \n")

sleep(1)

#  Q16 (a) Section iv START (Code Modification Using For Loop)
lst = []
num = int(input('How many items are in the customers order? : '))

sleep (1)

for n in range(num):
    numbers = float(input(("Enter the price of item {} : €".format(n+1))))
    lst.append(numbers)
    
sleep(1)

totalCost = (sum(lst))

print("You entered", num, "items and the total due is €", totalCost)
# Q16 (a) Section iv END 

# Q16 (a) Section v START (Basic Operators)
bal = float(input("What is the customers current account balance : €"))

if totalCost > bal:
	print("Customer does not have enough credit")
	
else:
	finalBal = (bal - totalCost)
	
	sleep(1)
	
	print("Your remaining balance is : €", finalBal)
	

# Q16 (a) Section v END 

sleep(1)

# Q16 (a) Section iii (Calling Variable From Input)
print("The member of staff who processed your order is", userName)
