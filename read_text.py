import csv

def sum_price_column(file_path):
    total_sum = 0
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                # Extract the value from the 'price' column and convert it to float
                price = float(row['Unit Price'])
                # Add the price to the total sum
                total_sum += price
            except ValueError:
                # Handle the case where the 'price' column does not contain a valid float
                print(f"Invalid price value encountered: {row['price']}")
    print(f"The total sum of the 'price' column is: {total_sum}")

# Replace 'Sales.csv' with your file path if needed
sum_price_column('Sales.csv')
