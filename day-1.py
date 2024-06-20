# Challenge 1
name = input("What is your name? ")
print("Hello " + name)
try:
  userAge = int(input("How old are you? "))
except:
  print("Please input a number")
  userAge = int(input("How old are you? "))

print("You are ", userAge, " years old")

# Challenge 2
try:
  num1 = int(input("Enter the first number: "))
except:
  print("Please input a number")
  num1 = int(input("Enter the second number: "))

try:
  num2 = int(input("Enter the first number: "))
except:
  print("Please input a number")
  num2 = int(input("Enter the first number: "))

operator = str(input("Choose an operator [p]lus or [m]inus: "))
while (operator != "p" and operator != "m"):
  print("Please choose a valid operator")
  operator = str(input("Choose an operator: "))

if (operator == "p"):
  print(num1, "+", num2,  "=" , num1 + num2)
elif (operator == "m"):
  print(num1, "-", num2,  "=" , num1 - num2)
else:
  print("Something failed")


# Challenge 3
from random import randint
num = randint(1,10)
guess = int(input("Guess a number between 1 and 10: "))

while (guess != num):
  if (guess > num):
    print("The number is lower")
  else: 
    print("The number is higher")
  guess = int(input("Guess a number between 1 and 10: "))

print("You guessed the number!")
