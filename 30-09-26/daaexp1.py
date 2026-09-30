n = int(input("Enter number of strings: "))

a = []

for i in range(n):
    a.append(input("Enter string: "))

for x in a:
    if x == x[::-1]:
        print("First Palindromic String:", x)
        break
else:
    print("No Palindromic String Found")
