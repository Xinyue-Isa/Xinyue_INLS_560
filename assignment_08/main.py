def get_user_choice():
    choices = {
        'a': '60s-music.csv',
        'b': 'athletes.csv',
        'c': 'fruits.csv'
    }

    while True:
        user_input = input('''
What file would you like to search?:
    a) 60s-music file
    b) athletes file
    c) fruits file
    x) to exit
''').lower()

        if user_input == 'x':
            return None
        elif user_input in choices:
            return choices[user_input]
        else:
            print("Invalid option. Please select a, b, c, or x.")

def search_file(file_name, search_term):
    search_term = search_term.lower()

    with open(file_name, 'r') as file:
        content = file.read().lower()

    if search_term in content:
        print(f'\nYour search term "{search_term}" exists in the {file_name} file!')
        see_entries = input('Would you like to see the entries? (y or n): ').lower()

        if see_entries == 'y':
            print(f'\nHere are all of the entries with the term "{search_term}":')
            with open(file_name, 'r') as file:
                for line in file:
                    if search_term in line.lower():
                        print(line.strip())
        elif see_entries == 'n':
            print('Okay, returning to main menu.')
            return
        else:
            print('Invalid option. Please enter y or n.')
    else:
        print(f'\n"{search_term}" does not exist in {file_name}')

def main():
    while True:
        file_name = get_user_choice()
        if file_name is None:
            print("Exiting from this program. Goodbye!")
            break

        search_term = input(f'Enter the search term for {file_name} file: ').lower()
        search_file(file_name, search_term)

if __name__ == '__main__':
    main()
