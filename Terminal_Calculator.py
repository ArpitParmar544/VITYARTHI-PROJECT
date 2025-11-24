import math

def add(x,y):
    return x+y

def subtract(x,y):
    return x-y

def multiply(x,y):
    return x*y

def divide(x,y):
    if y==0:
        return "ERROR!!!!! Division by zero."
    return x/y
    
def natural_log(x):
    if x <= 0:
        raise ValueError("ERROR!!!!!! Logarithm is only defined for positive numbers.")
    return math.log(x)

def main():
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Diviaion")
    print("5. Log") 
    print("Enter 'Quit' to quit")

    while True:
        choice = input("Enter choice(1/2/3/4/5/q): ") 

        if choice.lower()=='q':
            print("Thank you for using the calculator,We Hope you had an Nice Experience.")
            break

        if choice in ['1','2','3','4','5']:
            if choice=='5':
                try:
                    num1 = float(input("Enter number to find the natural log (ln): "))
                    result = natural_log(num1)
                    print(f"ln({num1}) = {result}")
                    
                except ValueError as e:
                    print(e)
                    
                print("-" * 20)
                continue
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
        
        else:
            print("This choice is not avaliable. Please enter a valid choice")

        print("-" * 30)

if __name__ == "__main__":
    main()