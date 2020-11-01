# Copy this code into your own repl. Click the navigation bar in the top left corner and go to My Repl. 

# Click the New Repl on the left, create the repl, and paste the code. Or put into another IDE 

 

# Everyone in SUSD has a gapps gmail. How did they create these for tens of thousands of students? Code. Let’s Try 

# Create 3 variables: First letter of first name, last name, and last two digits of student ID. Assign them your info. 

# Then create the variable email, which concatanates the previous variables into the susd gapps email. Then print the email. 

firstI = "M" 

lastN = "Salaway" 

lastTwo = 42 

email = firstI + lastN + str(lastTwo) + "@susdgapps.org" 

print(email) 

 

# Say we want to take a user's input. We do this with the input() function. 

""" 
input()                              # Allows for user input 
input("Enter your name: ")           # Prints a prompt for the user 
name = input("Enter your name: ")    # Stores the user input in a variable 
""" 

""" 
# Lets make a basic addition calcuator with user input. Try it! Here are some steps... 
# Create 2 variables num1 and num2, asking for user input 
num1 = float(input("Enter first number: ")) 
num2 = float(input("Enter second number: ")) 
result = num1 + num2 
print(result) 
""" 

# There are 5 basic operators: + - * / %. Test them out in the basic calculator 

# % or Modulus determines the remainder of a division operation. Instead of returning the result of the division, the mod operation returns the whole number remainder 

""" 
print(10 % 1) 
print(10 % 2) 
print(10 % 3) 
print(10 % 4) 
print(1234 % 10) # Mod by 10 and returns the last didgit 
print(1234 % 100) # Each multiple of ten, another last didgit returns 
""" 

 

# Now that we know Mod, let’s make the SUSD email. But better 

# The district is most likely given the whole student ID, not just the last two. How do they get the last two digits? 

studentID = 234322 

lastTwo = studentID % 100 

 

# The same can be done with the students’ first initial. We can use string index 

# Imagine we number each letter, starting at 0. "Cat" C = 0, a = 1, t = 2. We can access the letter by referencing the index of the string. 

firstName = "Abraham" 

firstInitial = firstName[0] 

 

# Now all we need is the last name and email 

lastName = "Lincoln" 

susdEmail = firstInitial + lastName + str(lastTwo) + "@susdgapps.org" 

print(susdEmail) 

 

# As we get into classes and objects, we will be able to see how a program can create everyone’s SUSD email without hard casting (manually entering) each variable for name and id 

 

# Lets go over if statements, so we can build a better calculator. https://www.w3schools.com/python/python_conditions.asp 

# Its easier than you think. We make decisions like this every day. If it is raining, then take a raincoat. 

 

num1 = float(input("Enter First Number: ")) 

op = input("Enter operator: ") 

num2 = float(input("Enter Second Number: ")) 

 

if op == "+": 

   print(num1 + num2) 

elif op == "-": 

   print(num1-num2) 

elif op == "/": 

   print(num1/num2) 

elif op == "*": 

   print(num1*num2) 

elif op == "%": 

   print(num1%num2) 

else: 

   print("Invalid Operator") 
