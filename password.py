import itertools

# Define the range of digits
digits = '0123456789'

# Open the file in write mode
with open("10_digit_combinations.txt", "w") as f:
    # Generate all combinations of 10 digits
    for combination in itertools.product(digits, repeat=10):
        # Write each combination to the file
        f.write(''.join(combination) + '\n')
