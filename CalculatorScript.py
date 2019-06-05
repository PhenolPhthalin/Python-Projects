import os
import time

os.system('cls')

def add(x, y):
	return x + y

def subtract(x, y):
	return x - y

def multiply(x, y):
	return x * y

def divide(x, y):
	return x / y

print ("Choose your Mode...")
print ("1. Addition")
print ("2. Subtraction")
print ("3. Multiply")
print ("4. Divide")
choice = input("Bitte waehlen Sie...(1/2/3/4):  ")

num1 = int(input("Type the first Number... "))
num2 = int(input("Type the second Number... "))

if choice == '1':
        print("Das Ergebnis ist: ",num1,"+",num2,"=", add(num1,num2))
        time.sleep(time.localtime(time.time())[1])
        os.system(exit)
elif choice == '2':
        print("Das Ergebnis ist: ",num1,"-",num2,"=", subtract(num1,num2))
        time.sleep(time.localtime(time.time())[1])
        os.system(exit)
elif choice == '3':
        print("Das Ergebnis ist: ",num1,"*",num2,"=", multiply(num1,num2))
        time.sleep(time.localtime(time.time())[1])
        os.system(exit)
elif choice == '4':
        print("Das Ergebnis ist: ",num1,"/",num2,"=", divide(x,y))
        time.sleep(time.localtime(time.time())[1])
        os.system(exit)	
else:
        print("Fehler, kehre zurück zum Hauptmenü...")
        time.sleep(10)
        os.system(exit)
	
