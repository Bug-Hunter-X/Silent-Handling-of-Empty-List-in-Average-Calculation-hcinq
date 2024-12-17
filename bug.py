def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    average = total / len(numbers)
    return average

my_list = []
average = calculate_average(my_list)
print(f"The average is: {average}") #This will return 0, which might be unexpected if no error is raised

my_list = [10, 20, 30, 40, 50]
average = calculate_average(my_list)
print(f"The average is: {average}") #This will return 30.0