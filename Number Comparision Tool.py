num1=float(input("Enter a number:"))
num2=float(input("Enter a number:"))
if num1>num2:
    print(f"{num1} is greator than {num2}")
elif num1==num2:
     print(f"Both numbers are equal{num1}")    
else:
      print(f"{num1} is less than {num2}")  
if num1==0 or num2==0:
     print("Atleast one number is Zero")
else:
     print("Both numbers are non-zero")     
         