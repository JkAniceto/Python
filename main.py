
import math

#PROBLEM 1 CHECKING IF PALINDROME OR NOT
userinput = int(input("Enter a number: "))
#Convert to string
numstr = str(userinput)

# Check if the number is a palindrome by comparing the string with its reverse
if numstr == numstr[::-1]:
    print(userinput, "is a palindrome number.")
else:
    print(userinput, "is not a palindrome number.")



#PROBLEM 2 CHECKING IF PRIME NUMBER
userinput = int(input("Enter a number: "))

if userinput > 1:

    for i in range(2, int(math.sqrt(userinput)) + 1):
        if (userinput % i) == 0:
            print(userinput, "is not a prime number")
            break
    else:
        print(userinput, "is a prime number")
else:
    print(userinput, "is not a prime number")


#PROBLEM 3
userinput = input("Enter a number: ")

input_list = list(userinput)

sum = 0
for digit in input_list:
    sum += int(digit)

print("The Sum Of A Number:", sum)




#Problem4
num = int(input("Input number: "))
factors_sum = 1

for i in range(2, int(math.sqrt(num)) + 1):
    if num % i == 0:
        factors_sum += i
        if i != num // i:
            factors_sum += num // i

if factors_sum == num:
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")





rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))
symbol = input("Enter a symbol: ")

for x in range(rows):
    for y in range(columns):
        if x == 0 or x == rows - 1 or y == 0 or y == columns - 1:
            print(symbol, end="")
        else:
            print(" ", end="")
    print()

