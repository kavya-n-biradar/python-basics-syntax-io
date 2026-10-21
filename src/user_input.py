"""Interactive user profile: greets the user and works out the year
they will turn 100."""

from datetime import date


def ask_name():
    """Ask for a name until the user types something.

    Returns:
        str: The name entered, without surrounding spaces.
    """
    while True:
        name = input("What is your name? ").strip()
        if name:
            return name
        print("Name cannot be empty. Please try again.")


def ask_age():
    """Ask for an age until the user enters a sensible whole number.

    Returns:
        int: The age entered (between 0 and 120).
    """
    while True:
        text = input("How old are you? ").strip()
        try:
            age = int(text)  # input() returns a string, so convert it
        except ValueError:
            print("Please enter your age as a whole number, e.g. 21.")
            continue
        if 0 <= age <= 120:
            return age
        print("Please enter an age between 0 and 120.")


def ask_language():
    """Ask for a favorite programming language until one is entered.

    Returns:
        str: The language entered, without surrounding spaces.
    """
    while True:
        language = input("What is your favorite programming language? ")
        language = language.strip()
        if language:
            return language
        print("Please enter a language, e.g. Python.")


def year_of_100(age):
    """Work out the year in which a person turns 100.

    Args:
        age (int): The person's current age.

    Returns:
        int: The calendar year they turn (or turned) 100.
    """
    current_year = date.today().year
    return current_year + (100 - age)


def main():
    """Collect the user's details and print a personalized message."""
    name = ask_name()
    age = ask_age()
    language = ask_language()
    year = year_of_100(age)

    print()
    print(f"Hello, {name}! Nice to meet you.")
    print(f"{language} is a great choice. Keep coding!")
    if year >= date.today().year:
        print(f"You will turn 100 in the year {year}.")
    else:
        print(f"You turned 100 in the year {year}.")


if __name__ == "__main__":
    main()