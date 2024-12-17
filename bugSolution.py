def calculate_average(numbers):
    if not numbers:
        raise ValueError("Cannot calculate the average of an empty list.")
    total = sum(numbers)
    average = total / len(numbers)
    return average

try:
    my_list = []
    average = calculate_average(my_list)
    print(f"The average is: {average}")
except ValueError as e:
    print(f"Error: {e}")

my_list = [10, 20, 30, 40, 50]
average = calculate_average(my_list)
print(f"The average is: {average}") 