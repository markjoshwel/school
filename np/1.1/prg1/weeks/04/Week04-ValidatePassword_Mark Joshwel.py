password = input("Enter password: ")

if len(password) < 8:
    print("Password must be at least 8 characters long.")

elif not any([c.isupper() for c in password]):
    print("Password must contain at least one uppercase letter.")

elif not any([c.isdigit() for c in password]):
    print("Password must contain at least one digit.")

else:
    print("Password is valid.")
