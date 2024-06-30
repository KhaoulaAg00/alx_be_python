# pattern_drawing.py

# Prompt the user for the pattern size
size = int(input("Enter the size of the pattern: "))

# Use a while loop to iterate through each row
row = 0
while row < size:
    # Use a for loop to print asterisks side by side
    for _ in range(size):
        print("*", end="")
    print()  # Print a newline character to move to the next row
    row += 1
