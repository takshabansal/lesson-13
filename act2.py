r=int(input("Please enter the total number of rows:"))
n=1
print("\nFLOYD'S TRIANGLE")
for i in range(1,r+1):
    for j in range(1, i+1):
        print(n, end = ' ')
        n=n+1
    print()
