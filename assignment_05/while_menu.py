menu_option = ''

while menu_option != 'q':
    print('Pet Corgi Care Menu:', 
          'a: Feeding routine', 
          'b: Length of exercise', 
          'c: Bathing frequency',
          'd: Determining Corgi Mood'
          'q: quit', 
          sep="\n")
    menu_option = input("Enter a letter for more information about Corgi: ")
    if menu_option == 'a':
        print("Corgi needs to be fed twice a day, once in the morning and once in the evening.")
    elif menu_option == 'b':
        print("Corgi needs to be out and about twice a day, with 30 to 40 minutes at a time being optimal.")
    elif menu_option == 'c':
        print("Corgi should be bathed at most once every half a month, not too often, which can lead to skin diseases.")
    elif menu_option == 'd':
        print("Corky wags its tail when it's happy and tucks it down when it's scared.")

