a=str(input("Give a string:"))
n=int(input("Enter the number of rows:"))
for j in range(n):
    for i in range(j+1):
        print(a, end="")
    print()