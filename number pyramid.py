# Get input value from user
num_rows = int(input("Enter the number of rows for the pyramid: "))

# Use nested loops to print the pyramid
for i in range(1, num_rows+1):
    # Print spaces before numbers
    for j in range(num_rows - i):
        print(" ", end="")
    # Print numbers
    for k in range(i):
        print(k+1, end=" ")
    # Print numbers in reverse order
    for l in range(i-1, 0, -1):
        print(l, end=" ")
    # Move to next line
    print()
