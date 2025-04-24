def get_user_numbers():
    """
    Collect numbers from the user and return them as a list.
    """
    user_numbers = []
    while True:
        user_input = input("Enter a number (or press Enter to finish): ")
        if user_input == "":
            break
        try:
            num = int(user_input)
            user_numbers.append(num)
        except ValueError:
            print("Please enter a valid number.")
    return user_numbers


def count_nums(num_lst):
    """
    Count occurrences of each number in the list.
    """
    num_dict = {}
    for num in num_lst:
        num_dict[num] = num_dict.get(num, 0) + 1
    return num_dict


def print_counts(num_dict):
    """
    Print how many times each number appeared.
    """
    for num, count in num_dict.items():
        print(f"{num} appears {count} times.")


def main():
    """
    Main function to execute the program.
    """
    user_numbers = get_user_numbers()
    num_dict = count_nums(user_numbers)
    print_counts(num_dict)


if __name__ == "__main__":
    main()