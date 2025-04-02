def calc():
    nums = (input("expression:"))
    x,y,z = nums.split(" ")
    if y == "+":
        print(float(x) + float(z))
    if y == "-":
        print(float(x) - float(z))
    if y == "*":
        print(float(x) * float(z))
    if y == "/":
        if z == "0":
            print("not defined")
        else:
            print(float(x) / float(z))
calc()