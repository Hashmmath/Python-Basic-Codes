email = input("Enter your Gmail address: ")
if email.endswith("@gmail.com"):
    username = email[:email.index("@")]
    domain = "gmail.com"
    print("Your username is:", username)
    print("Your domain is:", domain)
else:
    print("Invalid Gmail address.")
