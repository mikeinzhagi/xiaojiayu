while True:
    s = input("Please input your password")
    if len(s) <= 8:
        if s.isdigit() or s.isalpha():
            print("Password set successful")
            break
        else:
            print("Please enter a number or letter")
    else:
        print("too long")