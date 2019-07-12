num1 = int(input("enter first number: "))
num2 = int(input("enter second nuber: "))
print ("enter which operation you will like to perform?")
ch = input("enter any of these char for specific operation +,-,*,/: ")
results = 0
if ch == '+':
    result = num1 + num2
elif ch == '-':
    result = num1 - num2
elif ch =='*':
    result = num1 * num2
elif ch == '/':
    result = num1 / num2
else:
    print("input character is not accepted!")
print(num1, ch , num2, ":", result)