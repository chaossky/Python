import re

def sum_numbers_in_file(file_path):
    total_sum = 0
    with open(file_path, 'r') as file:
        for line in file:
            # Extract numbers from the line using regex
            numbers = re.findall(r'-?\d+\.?\d*', line)
            # Convert extracted numbers to float and add to the total sum
            total_sum += sum(map(float, numbers))
    print(f"The total sum of all numbers in the file is: {total_sum}")

# Replace 'numbers.txt' with your file path
sum_numbers_in_file('numbers.txt')