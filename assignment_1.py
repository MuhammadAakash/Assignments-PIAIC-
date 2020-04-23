a = float(input("Enter 1st number :"))
b =  float(input("Enter 2nd Number:"))
op = input("Enter operator for calculation : ")
if op == "+":
    print(" You choose Addition :")
    sum = a + b
    print(f"Result is {sum}")
elif op == "-":
    print(" You choose Subtraction :")
    sum = a - b
    print(f"Result is {sum}")
elif op == "*":
    print(" You choose Multiplication :")
    sum = a * b
    print(f"Result is {sum}")
elif op == "/":
    print(" You choose Devision :")
    sum = a/b
    print(f"Result is {sum}")