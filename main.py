# ---------------------------- Libraries ------------------------------- #
from random import randint


# ---------------------------- Constants ------------------------------- #
logo = """
 __  __ _ _ _             ____       _     _       
|  \/  (_) | | ___ _ __  |  _ \ __ _| |__ (_)_ __  
| |\/| | | | |/ _ \ '__| | |_) / _` | '_ \| | '_ \ 
| |  | | | | |  __/ |    |  _ < (_| | |_) | | | | |
|_|  |_|_|_|_|\___|_|    |_| \_\__,_|_.__/|_|_| |_|
"""

# ---------------------------- Functions ------------------------------- #
def validate_user_input(prompt: str) -> int:
    """
    Validate the user input.
    :param str prompt: The prompt message to display to the user.
    :return: The validated integer input from the user.
    """

    while True:
        user_input = input(prompt)

        try:
            value = int(user_input)

            if value <= 0:
                raise ValueError("Invalid Input: Please enter a positive number.")
            break

        except ValueError:
            print("Invalid Input: Please enter a positiv number.")

    return value


def miller_rabin(n, k=1000):
    """
    Miller-Rabin primality test.
    :param n: Number to test.
    :param k: Number of iterations.
    :return: True if n is prime, False otherwise.
    """
    # Variables
    d = n - 1
    s = 0

    # Body
    while d % 2 == 0:
        d //= 2
        s += 1

    for _ in range(k):
        a = randint(2, n - 1)
        x = pow(a, d, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(s - 1):
            x = pow(x, 2, n)

            if x == n - 1:
                break
        else:
            return False

    return True


def main():
    """
    Main function of the program.
    :return: None
    """

    # Header
    print()
    print(logo)
    print()

    # Variables
    number = validate_user_input("Please enter the number you want to test: ")
    iterations = validate_user_input("Please enter the number of iterations: ")

    # Body
    print()
    if miller_rabin(number, iterations):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")


# ------------------------------ Main ---------------------------------- #

if __name__ == "__main__":
    main()
