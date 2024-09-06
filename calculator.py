operator = input("enter the an operator(+ - * / ): ")
num1 = float(input("enter the 1st number : "))
num2 = float(input("enter the 2nd number : "))

if operator == "+":
  result = num1 + num2
  print(round (result,3))
elif operator == "-":
  result = num1 - num2
  print(round (result,3))
elif operator == "*":
  result = num1 * num2
  print(round (result,3))
elif operator == "/":
   if num2 == 0:
     print("error");
   else:
      result = num1 / num2
      print(round (result,3))
else:
  print (f"{operator} is not valid operator")
