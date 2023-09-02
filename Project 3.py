def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y

print("Operations:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    op = input("Enter the index of operation: ")

    if op in ('1','2','3','4'):

        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))

        if op == '1':
            print(f"",num1," + ",num2," = ",add(num1,num2))

        elif op == '2':
            print(f"",num1," - ",num2," = ",subtract(num1,num2))

        elif op == '3':
            print(f"",num1," x ",num2," = ",multiply(num1,num2))

        elif op == '4':
            print(f"",num1," / ",num2," = ",divide(num1,num2))

        break
    
    else:
        print("Invalid input")


