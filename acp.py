a=int(input("Enter the number of rows"))
for i in range(a,0,-1):
    sp='  ' *(a-i)
    st='* ' *i
    print(sp+st)