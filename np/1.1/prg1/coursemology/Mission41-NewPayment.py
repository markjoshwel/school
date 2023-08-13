def cal_new_payment(age, amount):
    if age >= 60:
        print(f"Original amount to pay is ${amount:.2f}")
        new_amount = amount * 0.95
        return new_amount

    else:
        print("You are not entitled for a discount.")
        return amount


# age = int(input("Please enter your age : "))
# amount = float(input("Please enter the amount you have to pay : "))
# new_amount = cal_new_payment(age, amount)
# print(new_amount)
