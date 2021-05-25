'''
Comp-Sci Example Q's

Donate Here:
paypal.me/

 -Change some variables if copying,
 -Uncomment to make code run,
 -Don't run code in this Repl
'''

'''

#---IMPORTANT---
#Dont include this in code
#Here until "#END OF PART A" are for section A
#Copy code in between the apostrophe to run
#---------------

# Q16 
import os
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

# Q16 (a) Section vii (Error Handling and Exit Program)
if num < 0:
	print("Invalid Option")
	exit()

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

# Q16 (a) Section vi START (If Statement)
if totalCost > bal:
	diff = (bal - totalCost)
	print("Customer does not have enough credit, they still owe : €", diff)
	
else:
	finalBal = (bal - totalCost)
	
	sleep(1)
	
	print("Your remaining balance is : €", finalBal)
	
# Q16 (a) Section vi END
# Q16 (a) Section v END 

sleep(1)

# Q16 (a) Section iii (Calling Variable From Input)
print("The member of staff who processed your order is", userName)

#END OF PART A
'''



'''
# Q16 (b)
# Students name: 
import os
from time import sleep

# Q16 (b)	Section i (Creating List & Case Sensitivity)
Standard_Postal_List = ['Netherlands', 'netherlands', 'Denmark', 'denmark', 'Poland', 'poland', 'Portugal', 'portugal', 'Finland', 'finland', 'Romania', 'romania', 'France', 'france', 'Germany', 'germany', 'Greece', 'greece', 'Spain', 'spain', 'Hungary', 'hungary', 'Sweden', 'sweden', 'Ireland', 'ireland']

# Q16 (b) Section ii START (Setting Parameters For Postal List)
countryIn = input("Enter what country are you sending too : ")

sleep(1)

if countryIn in Standard_Postal_List:
	print("Its on the list.")
else:
	addCountry = input("That country is not on the approved delivery list, would you like to add it to the list? y/n : ")
# Q16 (b) Section ii END

sleep(1)

# Q16 (b) Section iii START (Append To Approved Country List)
if addCountry == 'y':
	print(countryIn, 'will be added to the list.')
	Standard_Postal_List.append(countryIn)
	# Q16 (b) Section iv (Print List When New Country Added In Alphabetical Order)
	alphaList = sorted(Standard_Postal_List)
	sleep(1)
	print("The countries on the list are", alphaList)
elif addCountry == 'n':
	print(countryIn, 'will not be added to the list')
else:
	print("Error: Invalid Syntax. The options are case sensitive:")
	exit()
# Q16 (b) Section iii END
'''
