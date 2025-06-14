number1=float(input("Enter a number :"))
number2=float(input("Enter a number :"))
addition=number1+number2
subtraction=number1-number2
division=number1/number2 if number2!=0 else "cannot divide by 0"
modulus=number1%number2
exponential=number1**number2
multiplication=number1*number2
floordivision=number1//number2

print("---Calculator Result---")
print(f"Addition:{addition}")
print(f"Subtraction:{subtraction}")
print(f"Multiplication:{multiplication}")
print(f"Division:{division}")
print(f"Modulus:{modulus}")
print(f"Exponential:{exponential}")
print(f"Floordivision:{floordivision}")


