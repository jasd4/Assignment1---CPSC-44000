# Title for program: Software Engineering: Assignment 1
# File Name: Assignment 1.py
# Programmers: Mercy Jayaraj and Jasmine Davis
# Email Address: mercyjayaraj@lewisu.edu and jasminedavis@lewisu.edu
# Course: Software Engineering -CPSC-44000-LT1
# Date: February 14, 2025
# Program Description:

def find_near_misses(n, k):
    # Variable to track the smallest relative miss found
    smallest_relative_miss = float('inf')
    best_x, best_y, best_z = None, None, None
    best_miss = None

    # Loop through possible values of x and y (10 <= x, y <= k)
    for x in range(10, k + 1):
        for y in range(10, k + 1):
            # Compute xn + yn for the current x and y
            sum_of_the_powers = x ** n + y ** n

            # Find z so that z^n < sum_of_powers < (z+1)^n
            z = int(sum_of_the_powers ** (1 / n))  # Initial guess for z
            while z ** n < sum_of_the_powers:
                z += 1
            while (z + 1) ** n > sum_of_the_powers:
                z -= 1

            # Calculate the miss value integer
            miss_lower = sum_of_the_powers - z ** n
            miss_upper = (z + 1) ** n - sum_of_the_powers
            relative_miss_lower = miss_lower / sum_of_the_powers
            relative_miss_upper = miss_upper / sum_of_the_powers

            # Determine the smallest relative miss percentage
            if relative_miss_lower < smallest_relative_miss:
                smallest_relative_miss = relative_miss_lower
                best_x, best_y, best_z = x, y, z
                best_miss = miss_lower
                print(f"New Smallest Miss Found:")
                print(f"x = {x}, y = {y}, z = {z}")
                print(f"Miss = {miss_lower}, Relative Miss = {relative_miss_lower * 100:.5f}%")

            if relative_miss_upper < smallest_relative_miss:
                smallest_relative_miss = relative_miss_upper
                best_x, best_y, best_z = x, y, z + 1
                best_miss = miss_upper
                print(f"New Smallest Miss Found:")
                print(f"x = {x}, y = {y}, z = {z + 1}")
                print(f"Miss = {miss_upper}, Relative Miss = {relative_miss_upper * 100:.5f}%")

    print(f"\nThe smallest relative miss found:")
    print(f"x = {best_x}, y = {best_y}, z = {best_z}")
    print(f"Miss = {best_miss}, Relative Miss = {smallest_relative_miss * 100:.5f}%")


def main():
    # Ask user for input value
    print("Welcome to Fermat's Last Theorem Near Miss Finder!")
    n = int(input("Enter the power (n): "))
    while n < 3 or n >= 12:  # Check if the input is valid
        print("Error: n must be an integer between 3 and 11 inclusive.")
        n = int(input("Enter the power (n): "))

    k = int(input("Enter the upper limit for x and y (k): "))
    while k < 10:  # Check if the input is valid
        print("Error: k must be at least 10.")
        k = int(input("Enter the upper limit for x and y (k): "))

    # Call the function to find near misses
    find_near_misses(n, k)


if __name__ == "__main__":
    main()