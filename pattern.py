x = int(input("Enter the height of the triangle you want: "))
print("Right Triangle Pattern: ")
for i in range (1, x + 1):
    for j in range (i):
        print('*',end="" )
    print()