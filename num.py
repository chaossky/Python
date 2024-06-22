import random

def generate_unique_random_numbers(n, start, end):
    if n > (end - start + 1):
        return None  # Not enough unique numbers available

    numbers = list(range(start, end + 1))
    random.shuffle(numbers)
    return numbers[:n]

def main():
    num_count = 10
    start_range = 1
    end_range = 10

    random_numbers = generate_unique_random_numbers(num_count, start_range, end_range)
    if random_numbers is not None:
        for num in random_numbers:
            print(num)
    else:
        print("Not enough unique numbers available in the given range.")

if __name__ == "__main__":
    main()