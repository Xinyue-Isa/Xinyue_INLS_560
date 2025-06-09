menu_option = ''

while menu_option != 'q':
    print(f'''
Pet Corgi Care Menu:
a: Feeding routine
b: Length of exercise
c: Bathing frequency
d: Determining Corgi Mood
q: quit
''')
    menu_option = input("Enter a letter for more information about Corgi: ")
    if menu_option == 'a':
        print("Corgi needs to be fed twice a day, once in the morning and once in the evening.")
    elif menu_option == 'b':
        print("Corgi needs to be out and about twice a day, with 30 to 40 minutes at a time being optimal.")
    elif menu_option == 'c':
        frequent_bath = input('Do you think corgi need frequent baths because they hang out in the grass every day? enter (y or n): ').lower()
        if frequent_bath == 'y':
            print("That's the wrong idea! Frequent bathing can cause corgi's skin to lose its ability to protect itself and get skin diseases.")
        else:
            print("You are right! Corgi could be bathed at most once every half a month.")
    elif menu_option == 'd':
        print("Corky wags its tail when it's happy and tucks it down when it's scared.")