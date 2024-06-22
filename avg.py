def calculate_average():
    values = []  # Create an empty list to store the values
    num_values = int(input("Enter the number of values you want to average: "))

    # Input the values
    for i in range(num_values):
        value = float(input(f"Enter value {i + 1}: "))
        values.append(value)

    # Calculate the average
    total_sum = sum(values)
    average = total_sum / len(values)

    return average

result = calculate_average()
print(f"The average is: {result}")
