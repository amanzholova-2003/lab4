x = input()
y = input()
while not(x.isdigit() and y.isdigit()):
    x = input()
    y = input()
print(int(x) + int(y))


