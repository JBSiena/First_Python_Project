#COlOR TEXT
a = '\033[4;32m'
b = '\033[0m'
c = '\033[4;32m'
d = '\033[1;3;37;40m'
e = '\033[5;31m'
f = '\033[1;4m'
g = "\033[5;36m"

import time

#example 2 for Loop
def loopsamp():
		while True:
			try:
				num1 =int(input("Enter a number of arrows: "+b))
				for i in range(1,6+1):
					print(('\033[1;33m*'*i + ' '*(7-i+1))*num1)
				for i in range(7,0,-1):
					print(('\033[1;33m*'*i + ' '*(7-i+1))*num1)	
				else:
					print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
					input("Enter to Continue.....")
					break
			except ValueError:
				print("Try Again!")
				loopsamp()
				break
		exit


#count down
def leave():
	print(f+"Please Wait a Second..."+b)
	time.sleep(2)

#discussion selection
def pick():
	print("[1] Python's Discussion")
	print("[2] Command Prompt's Discussion")
	while True:
		try:
			p = int(input("\nPick a Discussion: "))
			if p == 1:
				suggest()
				break
			elif p == 2:
				c1()
				break
			else:
				print("\nTry Again Select from 1-2\n")
				print(f+"Please Wait a Second\n"+b)
				time.sleep(2)
				pick()
				break
		except ValueError:
			print(e+"\nTry Again Select from 1-2\n"+b)
			print(f+"Please Wait a Second\n"+b)
			time.sleep(2)
			pick()
			break
	exit

#Main Menu
def menu():
	print("[1] Printing in Python")
	print("[2] Variable Definition")
	print("[3] Operators in Python")
	print("[4] Conditional in Python")
	print("[5] Loop in Python")
	print("[6] Functions in Python")
	print("[7] Arrays in Python")
	print("[8] Dictionary in Python")
	print("[9] Go Back to Selection of Topics")
	print("[0] Exit")
	while True:
		try:
			option = int(input("\nEnter the Number of Chosen Topic: "))
			print()
			if option == 1:
				o1()
				break
			elif option == 2:
				o2()
				break
			elif option == 3:
				o3()
				break
			elif option == 4:
				o4()
				break
			elif option == 5:
				o5()
				break
			elif option == 6:
				o6()
				break
			elif option == 7:
				o7()
				break
			elif option == 8:
				o8()
				break
			elif option == 9:
				print(f+"Please Wait a Second"+b)
				time.sleep(2)
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print("Welcome Back",a+n.title()+b+"!Here are the Selection of Topics.")
				pick()
				break
			elif option == 0:
				print(f+"Exiting Program Please Wait..."+b)
				time.sleep(2)
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print(d+"Thank you for using this Program!\nThis is Siena,John Benjie's Menu Signing Off"+b)
				break
			else:
				print(e+"Invalid Number Choose 1-9\n"+b)
				menu()
				break
		except ValueError:
			print(e+"\nPlease Enter a Number from 1-9\n"+b)
			menu()
			break
	exit

#Suggested Topics
def suggest():
	print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
	print(d+"Welcome to Python's Topic\n"+b)
	while True:
		try:
			print(c+"Suggested Topics:"+b)
			print("[1] Printing in Python")
			print("[2] Operators in Python")
			print("[3] Loop in Python")
			print("[4] Main Menu")
			print("[5] Go Back to Selection")
			print("[6] Exit")
			nn = int(input("\nEnter The Number: "))
			print()
			if nn == 1:
				o1()
				break
			elif nn == 2:
				o3()
				break
			elif nn == 3:
				o5()
				break
			elif nn == 4:
				leave()
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print("Hello!"+a+n.title()+b,"Here is the Menu for Fundamentals of Python")
				menu()
				break
			elif nn == 5:
				leave()
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print("Welcome",a+n.title()+b,"! Here are the Selection of Topics.\n")
				pick()
				break
			elif nn == 6:
				leave()
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print(d+"Thank you for using this Program!\nThis is Siena,John Benjie's Menu Signing Off"+b)
				break
			else:
				print(e+"Invalid Number Try Again Choose 1-6\n"+b)
				print("Please Wait a Second")
				time.sleep(3)
				suggest()
				break
		except ValueError:
			print(e+"\nTry Again Please Enter a Number from 1-6\n"+b)
			print("Please Wait a Second\n")
			time.sleep(3)
			suggest()
			break
	exit

def suggest1():
	print(d+"Welcome to Python's Suggested Topics\n"+b)
	while True:
		try:
			print(c+"Suggested Topics:"+b)
			print("[1] Printing in Python")
			print("[2] Operators in Python")
			print("[3] Loop in Python")
			print("[4] Main Menu")
			print("[5] Go Back to Selection")
			print("[6] Exit")
			nn = int(input("\nEnter The Number: "))
			print()
			if nn == 1:
				o1()
				break
			elif nn == 2:
				o3()
				break
			elif nn == 3:
				o5()
				break
			elif nn == 4:
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print("Hello!"+a+n.title()+b,"Here is the Menu for Fundamentals of Python")
				menu()
				break
			elif nn == 5:
				leave()
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print("Welcome",a+n.title()+b,"! Here are the Selection of Topics.\n")
				pick()
				break
			elif nn == 6:
				leave()
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print(d+"Thank you for using this Program!\nThis is Siena,John Benjie's Menu Signing Off"+b)
				break
			else:
				print(e+"Invalid Number Choose 1-6\n"+b)
				suggest1()
				break
		except ValueError:
			print(e+"\nPlease Enter a Number from 1-6\n"+b)
			suggest1()
			break
	exit

def suggest2():
	print(d+"Welcome to Python's Suggested Topics\n"+b)
	while True:
		try:
			print(c+"Suggested Topics:"+b)
			print("[1] Variable Definition")
			print("[2] Conditional in Python")
			print("[3] Loop in Python")
			print("[4] Main Menu")
			print("[5] Go Back to Selection")
			print("[6] Exit")
			nn = int(input("\nEnter The Number: "))
			print()
			if nn == 1:
				o2()
				break
			elif nn == 2:
				o4()
				break
			elif nn == 3:
				o5()
				break
			elif nn == 4:
				leave()
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print("Hello!"+a+n.title()+b,"Here is the Menu for Fundamentals of Python")
				menu()
				break
			elif nn == 5:
				leave()
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print("Welcome",a+n.title()+b,"! Here are the Selection of Topics.\n")
				pick()
				break
			elif nn == 6:
				leave()
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print(d+"Thank you for using this Program!\nThis is Siena,John Benjie's Menu Signing Off"+b)
				break
			else:
				print(e+"Invalid Number Choose 1-6\n"+b)
				suggest2()
				break
		except ValueError:
			print(e+"\nPlease Enter a Number from 1-6\n"+b)
			suggest2()
			break
	exit

def suggest3():
	print(d+"Welcome to Python's Suggested Topics\n"+b)
	while True:
		try:
			print(c+"Suggested Topics:"+b)
			print("[1] Operators in Python")
			print("[2] Functions in Python")
			print("[3] Arrays Python")
			print("[4] Main Menu")
			print("[5] Go Back to Selection")
			print("[6] Exit")
			nn = int(input("\nEnter The Number: "))
			print()
			if nn == 1:
				o3()
				break
			elif nn == 2:
				o6()
				break
			elif nn == 3:
				o7()
				break
			elif nn == 4:
				leave()
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print("Hello!"+a+n.title()+b,"Here is the Menu for Fundamentals of Python")
				menu()
				break
			elif nn == 5:
				leave()
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print("Welcome",a+n.title()+b,"! Here are the Selection of Topics.\n")
				pick()
				break
			elif nn == 6:
				leave()
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print(d+"Thank you for using this Program!\nThis is Siena,John Benjie's Menu Signing Off"+b)
				break
			else:
				print(e+"Invalid Number Choose 1-6\n"+b)
				suggest3()
				break
		except ValueError:
			print(e+"\nPlease Enter a Number from 1-6\n"+b)
			suggest3()
			break
	exit
	
def suggest4():
	print(d+"Welcome to Python's Suggested Topics\n"+b)
	while True:
		try:
			print(c+"Suggested Topics:"+b)
			print("[1] Conditional in Python")
			print("[2] Functions in Python")
			print("[3] Operators in Python")
			print("[4] Main Menu")
			print("[5] Go Back to Selection")
			print("[6] Exit")
			nn = int(input("\nEnter The Number: "))
			print()
			if nn == 1:
				o4()
				break
			elif nn == 2:
				o6()
				break
			elif nn == 3:
				o3()
				break
			elif nn == 4:
				leave()
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print("Hello!"+a+n.title()+b,"Here is the Menu for Fundamentals of Python")
				menu()
				break
			elif nn == 5:
				leave()
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print("Welcome",a+n.title()+b,"! Here are the Selection of Topics.\n")
				pick()
				break
			elif nn == 6:
				leave()
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print(d+"Thank you for using this Program!\nThis is Siena,John Benjie's Menu Signing Off"+b)
				break
			else:
				print(e+"Invalid Number Choose 1-6\n"+b)
				suggest4()
				break
		except ValueError:
			print(e+"\nPlease Enter a Number from 1-6\n"+b)
			suggest4()
			break
	exit
	
def suggest5():
	print(d+"Welcome to Python's Suggested Topics\n"+b)
	while True:
		try:
			print(c+"Suggested Topics:"+b)
			print("[1] Loop in Python")
			print("[2] Arrays in Python")
			print("[3] Printing in Python")
			print("[4] Main Menu")
			print("[5] Go Back to Selection")
			print("[6] Exit")
			nn = int(input("\nEnter The Number: "))
			print()
			if nn == 1:
				o5()
				break
			elif nn == 2:
				o7()
				break
			elif nn == 3:
				o1()
				break
			elif nn == 4:
				leave()
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print("Hello!"+a+n.title()+b,"Here is the Menu for Fundamentals of Python")
				menu()
				break
			elif nn == 5:
				leave()
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print("Welcome",a+n.title()+b,"! Here are the Selection of Topics.\n")
				pick()
				break
			elif nn == 6:
				leave()
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print(d+"Thank you for using this Program!\nThis is Siena,John Benjie's Menu Signing Off"+b)
				break
			else:
				print(e+"Invalid Number Choose 1-6\n"+b)
				suggest5()
				break
		except ValueError:
			print(e+"\nPlease Enter a Number from 1-6\n"+b)
			suggest5()
			break
	exit
	
def suggest6():
	print(d+"\nWelcome to Python's Topic\n"+b)
	while True:
		try:
			print(c+"Suggested Topics:"+b)
			print("[1] Functions in Python")
			print("[2] Dictionary in Python")
			print("[3] Operators in Python")
			print("[4] Main Menu")
			print("[5] Go Back to Selection")
			print("[6] Exit")
			nn = int(input("\nEnter The Number: "))
			print()
			if nn == 1:
				o6()
				break
			elif nn == 2:
				o8()
				break
			elif nn == 3:
				o3()
				break
			elif nn == 4:
				leave()
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print("Hello!"+a+n.title()+b,"Here is the Menu for Fundamentals of Python")
				menu()
				break
			elif nn == 5:
				leave()
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print("Welcome",a+n.title()+b,"! Here are the Selection of Topics.\n")
				pick()
				break
			elif nn == 6:
				leave()
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print(d+"Thank you for using this Program!\nThis is Siena,John Benjie's Menu Signing Off"+b)
				break
			else:
				print(e+"Invalid Number Choose 1-6\n"+b)
				suggest6()
				break
		except ValueError:
			print(e+"\nPlease Enter a Number from 1-6\n"+b)
			suggest6()
			break
	exit

def suggest7():
	print(d+"\nWelcome to Python's Topic\n"+b)
	while True:
		try:
			print(c+"Suggested Topics:"+b)
			print("[1] Arrays in Python")
			print("[2] Dictionary in Python")
			print("[3] Functions in Python")
			print("[4] Main Menu")
			print("[5] Go Back to Selection")
			print("[6] Exit")
			nn = int(input("\nEnter The Number: "))
			print()
			if nn == 1:
				o7()
				break
			elif nn == 2:
				o8()
				break
			elif nn == 3:
				o6()
				break
			elif nn == 4:
				leave()
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print("Hello!"+a+n.title()+b,"Here is the Menu for Fundamentals of Python")
				menu()
				break
			elif nn == 5:
				leave()
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print("Welcome",a+n.title()+b,"! Here are the Selection of Topics.\n")
				pick()
				break
			elif nn == 6:
				leave()
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print(d+"Thank you for using this Program!\nThis is Siena,John Benjie's Menu Signing Off"+b)
				break
			else:
				print(e+"Invalid Number Choose 1-6\n"+b)
				suggest7()
				break
		except ValueError:
			print(e+"\nPlease Enter a Number from 1-6\n"+b)
			suggest7()
			break
	exit

def suggest8():
	print(d+"\nWelcome to Python's Topic\n"+b)
	while True:
		try:
			print(c+"Suggested Topics:"+b)
			print("[1] Dictionary in Python")
			print("[2] Conditional in Python")
			print("[3] Variables Definiton")
			print("[4] Main Menu")
			print("[5] Go Back to Selection")
			print("[6] Exit")
			nn = int(input("\nEnter The Number: "))
			print()
			if nn == 1:
				o8()
				break
			elif nn == 2:
				o4()
				break
			elif nn == 3:
				o2()
				break
			elif nn == 4:
				leave()
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print("Hello!"+a+n.title()+b,"Here is the Menu for Fundamentals of Python")
				menu()
				break
			elif nn == 5:
				leave()
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print("Welcome",a+n.title()+b,"! Here are the Selection of Topics.\n")
				pick()
				break
			elif nn == 6:
				leave()
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print(d+"Thank you for using this Program!\nThis is Siena,John Benjie's Menu Signing Off"+b)
				break
			else:
				print(e+"Invalid Number Choose 1-6\n"+b)
				suggest8()
				break
		except ValueError:
			print(e+"\nPlease Enter a Number from 1-6\n"+b)
			suggest8()
			break
	exit




#Printing
def o1():
	print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
	print(d+"The print() function prints the specified message to the screen,or other standard output device.The message can be a string,or any other object,the object will be converted into a string before written to the screen."+b)
	print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
	key = input("\nPress Enter to Continue>>>")
	print()#
	while True:
		try:
			print(c+"Options:"+b)
			print("[1] Example")
			print("[2] More Example")
			print("[3] Next")
			print("[4] Main Menu")
			print("[5] Suggested Topics")
			print("[6] Exit")
			option = int(input("\nPlease Select a Number: "))
			print()
			if option == 1:
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print(d+"Example:\nprint('Hello','how are you?')\n\nOutput:\nHello, how are you?"+b)
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				key = input("\nPress Enter to Continue>>")
				print()#
			elif option == 2:
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print(d+"Example:\na = 5\nprint('a =', a, sep='00000', end='')\nprint('a =', a, sep='0', end='')\n\nOutput:\na =000005\na =05"+b)
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				key = input("\nPress Enter to Continue>>")
				print()#
			elif option == 3:
				o2()
				break
			elif option == 4:
				print(f+"Please Wait a Second\n"+b)
				time.sleep(2)
				print("Welcome Back!"+a+n.title()+b,"Here are the Menu for Fundamentals of Python.")
				menu()
				break
			elif option == 5:
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				suggest1()
				break
			elif option == 6:
				print(f+"Exiting Program Please Wait..."+b)
				time.sleep(2)
				print(d+"Thank you for using this Program!\nThis is Siena,John Benjie's Menu Signing Off"+b)
				break
			else:
				print(option,e+"is not in the list Choose 1-6\n"+b)
				continue
		except ValueError:
			print(e+"\nPlease Enter a Number from 1-6\n"+b)
			continue
	exit
	
#Variables
def o2():
	print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
	print(d+"A Python variable is a symbolic name that is a reference or pointer to an object.Once an object is assigned to a variable,you can refer to the object by that name.But the data itself is still contained within the object."+b)
	print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
	key = input("\nPress Enter to Continue>>>")
	print()#
	while True:
		try:
			print(c+"Options:"+b)
			print("[1] Example")
			print("[2] More Examples")
			print("[3] Next")
			print("[4] Previous")
			print("[5] Main Menu")
			print("[6] Suggested Topics")
			print("[7] Exit")
			option = int(input("\nPlease Select a Number: "))
			print()#
			if option == 1:
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print(d+"Example 1:\nvariable_name = 'John Benjie Siena'\nprint(variable_name)\n\nOutput:\nJohn Benjie Siena\n"+b)
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				key = input("\nPress Enter to Continue>>")
				print()#
			elif option == 2:
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print(d+"Example 2:\na = 'John Benjie Siena'\nprint('Hi,',a,'Welcome to my Program')\n\nOutput:\nHi,John Benjie Siena Welcome to my Program\n"+b)
				print(d+"Example 3:\na = 'MyName'\nb = 1+2\nprint(a,b)\n\nOutput:\nMyName 3\n"+b)
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				key = input("\nPress Enter to Continue>>")
				print()#
			elif option == 3:
					o3()
					break
			elif option == 4:
					o1()
					break
			elif option == 5:
				print(f+"Please Wait a Second"+b)
				time.sleep(2)
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print("Welcome Back!"+a+n.title()+b,"Here are the Menu for Fundamentals of Python.")
				menu()
				break
			elif option == 6:
				suggest2()
				break
			elif option == 7:
				print(f+"Exiting Program Please Wait..."+b)
				time.sleep(2)
				print(d+"Thank you for using this Program!\nThis is Siena,John Benjie's Menu Signing Off"+b)
				break
			else:
				print(option,e+"is not in the list Choose 1-7\n"+b)
				continue
		except ValueError:
			print(e+"\nPlease Enter a Number from 1-7\n"+b)
			continue
			
	exit
	
#Operators
def o3():
	print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
	print(d+"Python divides the operators in the following groups:\n\n•Arithmetic operators\n•Comparison operators\n•Assignment operators\n•Logical operators\n•Identity operators\n•Membership operators\n•Bitwise operators")
	print("\nPython Arithmetic Operators\n\nArithmetic operators are used with numeric values to perform common mathematical operations:\n")
	print("Sign\t  Name\t\tExample")
	print("+	Addition	x + y	\n-	Subtraction	x - y	\n*	Multiplication	x * y	\n/	Division	x / y	\n%	Modulus	\tx % y	\n**	Exponentiation	x ** y	\n//	Floor division	x // y")
	print("\nPython Comparison Operators\n\nComparison operators are used to compare two values:\n")
	print("Operator\tName\t\t\tExample")
	print("==	        Equal\t\t\tx == y	\n!=            Not equal	\t\tx != y	\n>\t\t\b\b\b\bGreater than	\tx > y	\n<	     Less than	\t\tx < y	\n>=	Greater than or equal to	x >= y	\n<=	Less than or equal to	\tx <= y")
	print("\nPython Assignment Operators\n\nAssignment operators are used to assign values to variables:\n")
	print("Operator	Example	\tSame As")
	print("=	\tx = 5	\tx = 5	\n+=	\tx += 3	\tx = x + 3	\n-=	\tx -= 3	\tx = x - 3	\n*=	\tx *= 3	\tx = x * 3	\n/=	\tx /= 3	\tx = x / 3	\n%=	\tx %= 3	\tx = x % 3	\n//=	\tx //= 3	\tx = x // 3	\n**=	\tx **= 3	\tx = x ** 3	\n&=	\tx &= 3	\tx = x & 3	\n|=	\tx |= 3	\tx = x | 3	\n^=	\tx ^= 3	\tx = x ^ 3	\n>>=	\tx >>= 3	\tx = x >> 3	\n<<=	\tx <<= 3	\tx = x << 3")
	print("\nPython Logical Operators\n\nLogical operators are used to combine conditional statements:\n")
	print("Operator	Description	\t\t\t\tExample")
	print("and 	Returns True if both statements are true   \t\tx < 5 and  x < 10")
	print("or	Returns True if one of the statements is true	\tx < 5 or x < 4")
	print("not	Reverse the result,returns False if the result is true	not(x < 5 and x < 10)")
	print("\nPython Identity Operators\n\nIdentity operators are used to compare the objects,not if they are equal,but if they are actually the same object, with the same memory location:\n")
	print('Operator	\t\tDescription	\t\t\tExample')
	print("is 	\tReturns True if both variables are the same object	x is y	\nis not	\tReturns True if both variables are not the same object	x is not y")
	print("\nPython Membership Operators\n\nMembership operators are used to test if a sequence is presented in an object:\n")
	print("Operator     	\t\tDescription	\t\t\t\t\t\t\tExample")
	print("in      	Returns True if a sequence with the specified value is present in the object\t	x in y	\nnot in	        Returns True if a sequence with the specified value is not present in the object	x not in y")
	print("\nPython Bitwise Operators\n\nBitwise operators are used to compare (binary) numbers:\n")
	print("Operator	\t\b\bName	\t\tDescription")
	print("& 	      AND	\b\b\b\b\b\t\t\tSets each bit to 1 if both bits are 1\n|	      OR	\b\b\b\b\b\t\t\tSets each bit to 1 if one of two bits is 1\n^	      XOR	\b\b\b\b\b\t\t\tSets each bit to 1 if only one of two bits is 1\n~	      NOT	\b\b\b\b\b\b\t\t\tInverts all the bits\n<<	      Zero fill left shift	\b\b\b\b\b\tShift left by pushing zeros in from the right and let the leftmost bits fall off\n>>	      Signed right shift	\b\b\b\b\b\tShift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off"+b)
	print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
	key = input("\nPress Enter to Continue>>>")
	print()#
	while True:
		try:
			print(c+"Options:"+b)
			print("[1] Example")
			print("[2] More Examples")
			print("[3] Next")
			print("[4] Previous")
			print("[5] Main Menu")
			print("[6] Suggested Topics")
			print("[7] Exit")
			option = int(input("\nPlease Select a Number: "))
			print()#
			if option == 1:
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print(d+"Example Arithmetic:\na = 7\nb = 2\n\n# addition\nprint ('Sum: ', a + b)  \nSum: 9\n\n# subtraction\nprint ('Subtraction:', a - b)\nSubtraction: 5\n\n# multiplication\nprint ('Multiplication:', a * b)\nMultiplication: 14\n\n# division\nprint ('Division: ', a / b)\nDivision: 3.5\n\n# floor division\nprint ('Floor Division: ', a // b)Floor Division: 3\n\n# modulo\nprint ('Modulo: ', a % b)\nModulo: 1\n\n# a to the power b\nprint ('Power:', a ** b)\nPower: 49\n"+b)
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				key = input("\nPress Enter to Continue>>")
				print()#
			elif option == 2:
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print(d+"Example Assignment:\n# assign 10 to a\na = 10\n\n# assign 5 to b\nb = 5 \n\n# assign the sum of a and b to a\na += b      # a = a + b\n\nprint(a)\n\n# Output: 15"+b)
				print(d+"\nExample Comparison:\na = 5\n\nb = 2\n\n# equal to operator\nprint('a == b =', a == b)\n\n# not equal to operator\nprint('a != b =', a != b)\n\n# greater than operator\nprint('a > b =', a > b)\n\n# less than operator\nprint('a < b =', a < b)\n\n# greater than or equal to operator\nprint('a >= b =', a >= b)\n\n# less than or equal to operator\nprint('a <= b =', a <= b)\n\n#Output:\na == b = False\na != b = True\na > b = True\na < b = False\na >= b = True\na <= b = False"+b)
				print(d+"\nExample Logical:\na = 5\nb = 6\n\nprint((a > 2) and (b >= 6))\n#Output:\nTrue"+b)
				print(d+"\n# logical AND\nprint(True and True)     # True\nprint(True and False)    # False\n\n# logical OR\nprint(True or False)     # True\n\n# logical NOT\nprint(not True)          # False"+b)
				print(d+"\nExample Indentity:\nx1 = 5\ny1 = 5\nx2 = 'Hello'\ny2 = 'Hello'\nx3 = [1,2,3]\ny3 = [1,2,3]\n\nprint(x1 is not y1)  # prints False\n\nprint(x2 is y2)  # prints True\n\nprint(x3 is y3)  # prints False"+b)
				print(d+"\nExample Membership:\nx = 'Hello world'\ny = {1:'a', 2:'b'}\n\n# check if 'H' is present in x string\nprint('H' in x)  # prints True\n\n# check if 'hello' is present in x string\nprint('hello' not in x)  # prints True\n\n# check if '1' key is present in y\nprint(1 in y)  # prints True\n\n# check if 'a' key is present in y\nprint('a' in y)  # prints False"+b)
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				key = input("\nPress Enter to Continue>>")
				print()#
			elif option == 3:
				o4()
				break
			elif option == 4:
				o2()
				break
			elif option == 5:
				print(f+"Please Wait a Second"+b)
				time.sleep(2)
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print("Welcome Back!"+a+n.title()+b,"Here are the Menu for Fundamentals of Python.")
				menu()
				break
			elif option == 6:
				suggest3()
				break
			elif option == 7:
				print(f+"Exiting Program Please Wait..."+b)
				time.sleep(2)
				print(d+"Thank you for using this Program!\nThis is Siena,John Benjie's Menu Signing Off"+b)
				break
			else:
				print(option,e+"is not in the list Choose 1-7\n"+b)
				continue
		except ValueError:
			print(e+"\nPlease Enter a Number from 1-7\n"+b)
			continue		
	exit
	
#Conditional
def o4():
	print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
	print(d+"Python Conditions and If statements\n\nPython supports the usual logical conditions from mathematics:\n\nEquals: a == b\nNot Equals: a != b\nLess than: a < b\nLess than or equal to: a <= b\nGreater than: a > b\nGreater than or equal to: a >= b\nThese conditions can be used in several ways,most commonly in 'if statements' and loops.\n\nAn 'if statement' is written by using the if keyword.\n\nIndentation\n\nPython relies on indentation (whitespace at the beginning of a line) to define scope in the code.Other programming languages often use curly-brackets for this purpose.\n\nElif\n\nThe elif keyword is pythons way of saying 'if the previous conditions were not true, then try this condition'.\n\nElse\n\nThe else keyword catches anything which isn't caught by the preceding conditions.\n\nShort Hand If\n\nIf you have only one statement to execute, you can put it on the same line as the if statement.\n\nShort Hand If ... Else\n\nIf you have only one statement to execute, one for if,and one for else, you can put it all on the same line.\n\nAnd\n\nThe and keyword is a logical operator,and is used to combine conditional statements.\n\nOr\n\nThe or keyword is a logical operator,and is used to combine conditional statements.\n\nNested If\n\nYou can have if statements inside if statements,this is called nested if statements.\n\nThe pass Statement\n\nif statements cannot be empty,but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error."+b)
	print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
	key = input("\nPress Enter to Continue>>")
	print()#
	while True:
		try:
			print(c+"Options:"+b)
			print("[1] Example")
			print("[2] More Examples")
			print("[3] Next")
			print("[4] Previous")
			print("[5] Main Menu")
			print("[6] Suggested Topics")
			print("[7] Exit")
			option = int(input("\nPlease Select a Number: "))
			print()#
			if option == 1:
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print(d+"Example If statements:\na = 33\nb = 200\nif b > a:\n  print('b is greater than a')\n\nExample Indentation:\na = 33\nb = 200\nif b > a:\nprint('b is greater than a') # you will get an error\n\nExample Elif:\na = 33\nb = 33\nif b > a:\n  print('b\nis greater than a')\nelif a == b:\n  print('a and b are equal')\n\nExample Else:\na = 200\nb = 33\nif b > a:\n  print('b is\ngreater than a')\nelif a == b:\n  print('a and b are equal')\nelse:\n  print('a is greater than b')\n"+b)
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				key = input("\nPress Enter to Continue>>")
				print()#
			elif option == 2:
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print(d+"Example Short Hand If ... Else:\nif a > b: print('a is greater than b')\n\na = 2\nb = 330\nprint('A') if a > b else print('B')\n\nExample And:\na = 200\nb = 33\nc = 500\nif a > b and c > a:\n  print('Both conditions are True')\n\nExample Or:\na = 200\nb = 33\nc = 500\nif a > b or a > c:\n  print('At least one of the conditions is True')\n\nExample Nested If:\nx = 41\n\nif x > 10:\n  print('Above ten,')\n  if x > 20:\n    print('and also above 20!')\n  else:\n    print('but not above 20.')\n\nExample Pass:\na = 33\nb = 200\n\nif b > a:\n  pass"+b)
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				key = input("\nPress Enter to Continue>>")
				print()#
			elif option == 3:
				o5()
				break
			elif option == 4:
				o3()
				break
			elif option == 5:
				print(f+"Please Wait a Second"+b)
				time.sleep(2)
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print("Welcome Back!"+a+n.title()+b,"Here are the Menu for Fundamentals of Python.")
				menu()
				break
			elif option == 6:
				suggest4()
				break
			elif option == 7:
				print(f+"Exiting Program Please Wait..."+b)
				time.sleep(2)
				print(d+"Thank you for using this Program!\nThis is Siena,John Benjie's Menu Signing Off"+b)
				break
			else:
				print(option,e+"is not in the list Choose 1-7\n"+b)
				continue
		except ValueError:
			print(e+"\nPlease Enter a Number from 1-7\n"+b)
			continue
	exit
	
#Loop
def o5():
	print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
	print(d+"Python For Loops\nA for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).\n\nThis is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.\n\nWith the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.\nThe for loop does not require an indexing variable to set beforehand.\nLooping Through a String\nEven strings are iterable objects, they contain a sequence of characters.\nThe range() Function\nTo loop through a set of code a specified number of times, we can use the range() function,\nThe range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number."+b)
	print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
	key = input("\nPress Enter to Continue>>")
	print()#
	while True:
		try:
			print(c+"Options:"+b)
			print("[1] Example")
			print("[2] More Examples")
			print("[3] Next")
			print("[4] Previous")
			print("[5] Main Menu")
			print("[6] Suggested Topics")
			print("[7] Exit")
			option = int(input("\nPlease Select a Number: "))
			print()#
			if option == 1:
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print(d+"Example For Loop:\n#Print each fruit in a fruit list:\nfruits = ['apple', 'banana', 'cherry']\nfor x in fruits:\n  print(x)\n\nExample range() function:\n#Using the range() function:\nfor x in range(6):\n  print(x)\n#Note that range(6) is not the values of 0 to 6, but the values 0 to 5.\nExample range():\n#Using the start parameter:\nfor x in range(2, 6):\n  print(x)\n\nThe range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):\nExample:\n#Increment the sequence with 3 (default is 1):\nfor x in range(2, 30, 3):\n  print(x)"+b)
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				key = input("\nPress Enter to Continue>>")
				print()#
			elif option == 2:
				print(d+"Example Looping Through a String:\n#Loop through the letters in the word 'banana':\nLoop through the letters in the word 'banana':\nfor x in 'banana':\n  print(x)\n\nExample The break Statement:\n#Exit the loop when x is 'banana':\nfruits = ['apple', 'banana', 'cherry']\nfor x in fruits:\n  print(x)\n  if x == 'banana':\n    break\n\nExample continue Statement:\n#Do not print banana.\nfruits = ['apple', 'banana', 'cherry']\nfor x in fruits:\n  if x == 'banana':\n    continue\n  print(x)\n\nExample Else in for Loop:\nPrint all numbers from 0 to 5, and print a message when the loop has ended:\nfor x in range(6):\n  print(x)\nelse:\n  print('Finally finished!')\n\nNote: The else block will NOT be executed if the loop is stopped by a break statement.\n\nExample\nBreak the loop when x is 3, and see what happens with the else block:\n\nfor x in range(6):\n  if x == 3: break\n  print(x)\nelse:\n  print('Finally finished!')"+b)
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				key = input(b+"\nPress Enter to Continue>>")
				samp1 = input("\033[1;32mWould you like to try my Example? y/n >>")
				if samp1.lower() == 'y':
					loopsamp()
				elif samp1.lower() == 'n':
					print("You Denied to Try Examples")
					input("Enter to Continue.....")
			elif option == 3:
				o6()
				break
			elif option == 4:
				o4()
				break
			elif option == 5:
				print(f+"Please Wait a Second")
				time.sleep(2)
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print("Welcome Back!"+a+n.title()+b,"Here are the Menu for Fundamentals of Python.")
				menu()
				break
			elif option == 6:
				suggest5()
				break
			elif option == 7:
				print(f+"Exiting Program Please Wait..."+b)
				time.sleep(2)
				print(d+"Thank you for using this Program!\nThis is Siena,John Benjie's Menu Signing Off"+b)
				break
			else:
				print(option,e+"is not in the list Choose 1-7\n"+b)
		except ValueError:
			print(e+"\nPlease Enter a Number from 1-7\n"+b)
			continue
	exit
	
#Functions
def o6():
	print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
	print(d+"A function is a block of code which only runs when it is called.\n\nYou can pass data, known as parameters, into a function.\n\nA function can return data as a result."+b)
	print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
	key = input("\nPress Enter to Continue>>")
	print()#
	while True:
		try:
			print(c+"Options:"+b)
			print("[1] Example")
			print("[2] More Examples")
			print("[3] Next")
			print("[4] Previous")
			print("[5] Main Menu")
			print("[6] Suggested Topics")
			print("[7] Exit")
			option = int(input("\nPlease Select a Number: "))
			print()#
			if option == 1:
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print(d+"Creating a Function\nIn Python a function is defined using the def keyword:\n\nExample\ndef my_function():\n  print('Hello from a function')\n\nCalling a Function\nTo call a function, use the function name followed by parenthesis:\n\nExample\ndef my_function():\n  print('Hello from function')\n\nmy_function()"+b)
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				key = input("\nPress Enter to Continue>>")
			elif option == 2:
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print(d+"Arguments\nInformation can be passed into functions as arguments.\n\nArguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.\n\nThe following example has a function with one argument (fname). When the function is called, we pass along a first name, which is used inside the function to print the full name:\n\nExample\ndef my_function(fname):\n  print(fname + ' Refsnes')\n\nmy_function('Emil')\nmy_function('Tobias')\nmy_function('Linus')"+b)
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				key = input("\nPress Enter to Continue>>")
				print()#
			elif option == 3:
				o7()
				break
			elif option == 4:
				o5()
				break
			elif option == 5:
				print(f+"Please Wait a Second")
				time.sleep(2)
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print("Welcome Back!"+a+n.title()+b,"Here are the Menu for Fundamentals of Python.")
				menu()
				break
			elif option == 6:
				suggest6()
				break
			elif option == 7:
				print(f+"Exiting Program Please Wait..."+b)
				time.sleep(2)
				print(d+"Thank you for using this Program!\nThis is Siena,John Benjie's Menu Signing Off"+b)
				break
			else:
				print(option,e+"is not in the list Choose 1-7\n"+b)
				continue
		except ValueError:
			print(e+"\nPlease Enter a Number from 1-7\n"+b)
			continue
	exit
	
#Arrays
def o7():
	print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
	print(d+"What is an Array?\nAn array is a special variable, which can hold more than one value at a time.\n\nIf you have a list of items (a list of car names, for example), storing the cars in single variables could look like this:\n\ncar1 = 'Ford'\ncar2 = 'Volvo'\ncar3 = 'BMW'\nHowever, what if you want to loop through the cars and find a specific one? And what if you had not 3 cars, but 300?\n\nThe solution is an array!\n\nAn array can hold many values under a single name, and you can access the values by referring to an index number."+b)
	print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
	key = input("\nPress Enter to Continue>>")
	print()#
	while True:
		try:
			print(c+"Options:"+b)
			print("[1] Example")
			print("[2] More Examples")
			print("[3] Next")
			print("[4] Previous")
			print("[5] Main Menu")
			print("[6] Suggested Topics")
			print("[7] Exit")
			option = int(input("\nPlease Select a Number: "))
			print()#
			if option == 1:
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print(d+"Example Create an array containing car names:\n\ncars = ['Ford', 'Volvo', 'BMW']\n\nAccess the Elements of an Array\nYou refer to an array element by referring to the index number.\n\nExample\nGet the value of the first array item:\n\nx = cars[0]"+b)
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				key = input("\nPress Enter to Continue>>")
				print()#
			elif option == 2:
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print(d+"Looping Array Elements\nYou can use the for in loop to loop through all the elements of an array.\n\nExample\nPrint each item in the cars array:\n\nfor x in cars:\n  print(x)\n\nAdding Array Elements\nYou can use the append() method to add an element to an array.\n\nExample\nAdd one more element to the cars array:\n\ncars.append('Honda')\n\nRemoving Array Elements\nYou can use the pop() method to remove an element from the array.\n\nExample\nDelete the second element of the cars array:\n\ncars.pop(1)\nYou can also use the remove() method to remove an element from the array.\n\nExample\nDelete the element that has the value 'Volvo':\n\ncars.remove('Volvo')"+b)
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				key = input("\nPress Enter to Continue>>")
				print()#
			elif option == 3:
				o8()
				break
			elif option == 4:
				o6()
				break
			elif option == 5:
				print(f+"Please Wait a Second")
				time.sleep(2)
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print("Welcome Back!"+a+n.title()+b,"Here are the Menu for Fundamentals of Python.")
				menu()
				break
			elif option == 6:
				suggest7()
				break
			elif option == 7:
				print(f+"Exiting Program Please Wait..."+b)
				time.sleep(2)
				print(d+"Thank you for using this Program!\nThis is Siena,John Benjie's Menu Signing Off"+b)
				break
			else:
				print(option,e+"is not in the list Choose 1-7\n"+b)
				continue
		except ValueError:
			print(e+"\nPlease Enter a Number from 1-7\n"+b)
			continue
	exit
	
#Dictionary
def o8():
	print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
	print(d+"Dictionary\nDictionaries are used to store data values in key:value pairs.\n\nA dictionary is a collection which is ordered*, changeable and do not allow duplicates.\n\nAs of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.\n\nDictionaries are written with curly brackets, and have keys and values:"+b)
	print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
	key = input("\nPress Enter to Continue>>")
	print()#
	while True:
		try:
			print(c+"Options:"+b)
			print("[1] Example")
			print("[2] More Example")
			print("[3] Previous")
			print("[4] Main Menu")
			print("[5] Suggested Topics")
			print("[6] Exit")
			option = int(input("\nPlease Select a Number: "))
			print()#
			if option == 1:
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print(d+"Example\nCreate and print a dictionary:\n\nthisdict = {\n   'brand':'Ford',\n   'model': 'Mustang',\n   'year': 1964\n}\nprint(thisdict)\n\nDictionary Items\nDictionary items are ordered, changeable, and does not allow duplicates.\n\nDictionary items are presented in key:value pairs, and can be referred to by using the key name.\n\nExample\nPrint the 'brand' value of the dictionary:\n\nthisdict = {\n  'brand': 'Ford',\n  'model': 'Mustang',\n  'year': 1964\n}\nprint(thisdict['brand'])\n\nDictionary Length\nTo determine how many items a dictionary has, use the len() function:\nExample\nPrint the number of items in the dictionary:\n\nprint(len(thisdict))\n\nThe dict() Constructor\nIt is also possible to use the dict() constructor to make a dictionary.\n\nExample\nUsing the dict() method to make a dictionary:\n\nthisdict = dict(name = 'John', age = 36, country = 'Norway')\nprint(thisdict)"+b)
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				key = input("\nPress Enter to Continue>>")
				print()#
			elif option == 2:
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print(d+"Dictionary Items - Data Types\nThe values in dictionary items can be of any data type:\n\nExample\nString, int, boolean, and list data types:\n\nthisdict = {\n  'brand': 'Ford',\n  'electric': False,\n  'year': 1964,\n  'colors': ['red', 'white', 'blue']\n}\n\ntype()\nFrom Python's perspective, dictionaries are defined as objects with the data type 'dict':\n\n<class 'dict'>\nExample\nPrint the data type of a dictionary:\nthisdict = {\n  'brand': 'Ford',\n  'model': 'Mustang',\n  'year': 1964\n}\nprint(type(thisdict))"+b)
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				key = input("\nPress Enter to Continue>>")
				print()#
			elif option == 3:
				o7()
				break
			elif option == 4:
				print(f+"Please Wait a Second")
				time.sleep(2)
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print("Welcome Back!"+a+n.title()+b,"Here are the Menu for Fundamentals of Python.")
				menu()
				break
			elif option == 5:
				suggest8()
				break
			elif option == 6:
				print(f+"Exiting Program Please Wait..."+b)
				time.sleep(2)
				print(d+"Thank you for using this Program!\nThis is Siena,John Benjie's Menu Signing Off"+b)
				break
			else:
				print(option,e+"is not in the list Choose 1-6\n"+b)
				continue
		except ValueError:
			print(e+"\nPlease Enter a Number from 1-6\n"+b)
			continue
	exit
	
#CMD 
def c1():
	print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
	print(d+"Welcome to Command Prompt's Topic."+b)
	print()#
	while True:
		try:
			print(c+"Options:"+b)
			print("[1] Discussions")
			print("[2] Example")
			print("[3] Go Back to Selection")
			print("[4] Exit")
			option = int(input("\nPlease Select a Number: "))
			if option == 1:
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print(d+"What is a command prompt?\nA command prompt is the input field in a text-based user interface screen for an operating system (OS) or program. The prompt is designed to elicit an action. The command prompt consists of a brief text string followed by a blinking cursor, which is where the user types command prompt commands.")
				print("\nCommand-line interfaces (CLI) and prompts were the standard interface for computers from the early days of computing into the 1980s. Microsoft MS-DOS systems and other early consumer-based computers used CLIs. Current Windows systems offer the CLI for administrative tasks. The CLI is still an essential part of the Linux OS.")
				print("\nThe command prompt is an executable CLI program, cmd.exe. At the command prompt, the user types a statement including a base batch file or a command name and any arguments to specify running conditions, logging and so on for the program. In Windows systems, such as Windows 10 and many previous versions of Windows, the command interpreter and executioner are referred to as the Windows Command Processor.")
				print("Command prompt interfaces can be powerful and succinct. Some tools that aren't available through the graphical user interface (GUI) can be accessed through the command prompt. It also offers superior automation through scripting, but mastering the commands can be challenging.")
				print("\nHow to use the command prompt")
				print("\nMany Windows users regularly use the GUI. However, it is helpful to know how to execute system functions in the command prompt window. For example, basic functions such changing a directory or performing an examination of the system disk are easy to execute at the command level.")
				print("\nThere are various ways to open command prompt. A common one in Windows is to use the command prompt shortcut located in the Start menu or on the Apps screen.")
				print("\nThe basic command level might look like this:")
				print("\nC:\Windows\system32\>cmd.exe and <enter>")
				print("\nThis results in the following:")
				print("\nC:\>")
				print("\nThe OS is now ready for a command. Each command launches a batch file that initiates a specific function. The change directory function looks like this:")
				print("\nC:\>dir and <enter>")
				print("\nThis presents a list of available directories linked to the root directory -- for example, the C drive -- in the system. To change to a different directory, the following is performed, using the example of changing to a directory called applications:")
				print("\nC:\>cd applications\ and <enter>")
				print("\nThis changes the directory to:")
				print("\nC:\applications\>")
				print("\nNow the system needs a command to execute something in the applications directory. To check on the status of the elements associated with a specific directory, the user enters the following at the command prompt:")
				print("\nC:\applications\>chkdsk and <enter>")
				print("\nThe OS executes the chkdsk utility for the applications directory and presents a summary of the components in that directory, such as the number of files and subdirectories, and number of bytes in use and the number available."+b)
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				key = input("\nPress Enter to Continue>>")
				print()#
			elif option == 2:
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print(d+"The syntax of the wording entered on the command-line is important. The system will not execute a function if a letter or number is in the wrong sequence.\n\nExamples of commands\nCommonly used commands include the following:\n\n•Cls to clear the command prompt screen;\n•Copy to create a copy of something such as a file;\n•Del to delete a file;\n•Format to formats a disk according to specific requirements;\n•Ipconfig to list the network data such as IP address and subnet mask;\n•Ping to send a packet to an IP address and display the information returned from the other device;\n•Sfc to detect and fix corrupt system files; and\n•Shutdown to execute a system shutdown or restart."+b)
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				key = input("\nPress Enter to Continue>>")
				print()#
			elif option == 3:
				print(f+"\nPlease Wait a Second"+b)
				time.sleep(2)
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print("Welcome Back",a+n.title()+b,"! Here are the Selection of Topics.")
				pick()
				break
			elif option == 4:
				print(f+"Exiting Program Please Wait..."+b)
				time.sleep(2)
				print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
				print(d+"Thank you for using this Program!\nThis is Siena,John Benjie's Menu Signing Off"+b)
				break
			else:
				print(option,e+"is not in the list Choose 1-4\n"+b)
				continue
		except ValueError:
			print(e+"\nPlease Enter a Number from 1-4\n"+b)
			continue
	exit


#User's Name
n = input(d+"Enter Your Name:"+b)
print("Welcome to my Program "+a+n.title()+b+",Here are the Selection of Topics.")
print("————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————")
pick()
