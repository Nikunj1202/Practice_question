# Create a multiplication table for any number.
a = int(input("enter number you want to write table:/ "))
b = 1 
while b <= 10:
    c =  a * b 
    print(f"{a} * {b} = {c}")
    b += 1
