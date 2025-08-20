a=str(input("Give a string:"))
for j in range(1,11):
    for i in range(j):
        print(a, end="")
    print()
for j in range(11,0,-1):
    for i in range(j):
        print(a, end="")
    print()