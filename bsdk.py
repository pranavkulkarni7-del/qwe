import sys

# Check if exactly 2 arguments are provided
if len(sys.argv) != 3:
    print("Usage: python app.py <num1> <num2>")
    sys.exit(1)

# Read command-line arguments
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

# Perform operations
print("Addition:", num1 + num2)
print("Multiplication:", num1 * num2)
