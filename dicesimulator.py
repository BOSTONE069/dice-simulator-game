import random
print("This is a dice simulator")
x = "y"
while x == "y":
     number = random.randint(1,6)
     if number == 1:
         print("---------")
         print("|       |")
         print("|   o   |")
         print("|       |")
         print("---------")
     if number == 2:
         print("---------")
         print("|       |")
         print("|o     o|")
         print("|       |")
         print("---------")
     if number == 3:
         print("---------")
         print("|   o   |")
         print("|   o   |")
         print("|   o   |")
         print("---------")
     if number == 4:
         print("---------")
         print("|o     o|")
         print("|       |")
         print("|o     o|")
         print("---------")
     if number == 5:
         print("---------")
         print("|o     o|")
         print("|   o   |")
         print("|o     o|")
         print("---------")
     if number == 6:
         print("---------")
         print("|o     o|")
         print("|o     o|")
         print("|o     o|")
         print("---------")
     x = input("Press y in order to roll again")
