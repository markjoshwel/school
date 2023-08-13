L = float(input("What is your desired loan amount? "))
A = float(input("What is your annual income? "))
C = float(input("What is the total value of your current loans? "))
S = float(input("What is the total of your savings? "))
Y = int(input("How many years do you want to pay back this loan? "))

I = (L + C) / (S + A * Y)
print(f"Your interest rate is {I * 100:.1f}%")
