def get_year() -> int:
    while True:
        year = input("\nEnter a year to check if it's a leap year: ")
        if not year.isdigit():
            print("\nPlease enter a valid year.")
        elif not int(year) > 0:
            print("\nPlease enter a year greater than 0.")
        else:
            return int(year)


def is_it_leap(year: int) -> bool:
    if year % 400 == 0:
        return True

    elif year % 4 == 0 and year % 100 != 0:
        return True

    else:
        return False


def check_again():
    while True:
        response = input("\nWould you like to check again with a different year? (y/n) ")
        if response not in ["y", "n"]:
            print("\nPlease enter a valid response.")
        elif response == "y":
            main()
        elif response == "n":
            exit()


def main():
    year = get_year()
    leapy = is_it_leap(year)
    if leapy:
        print(f"\nThe year {year} is a leap year.")
    else:
        print(f"\nThe year {year} is not a leap year.")
    check_again()


if __name__ == '__main__':
    main()
