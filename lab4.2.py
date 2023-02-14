x,y = map(str,input().split())

while not (x.isdigit() and y.isdigit()):

   x,y = map(str,input().split())

print(int(x)+int(y))

