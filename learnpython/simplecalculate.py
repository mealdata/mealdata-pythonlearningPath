num1= int(input("Inter firts number: "))
num2= int(input("Inter second number: "))
operator = input("Please your operator: ")
if operator == "+":
    print("Based on your op ", operator, ", the value is ", num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print(f'The multiplication is, {num1*num2}')
elif operator== "/":
    print("The devision is ", num1/num2)