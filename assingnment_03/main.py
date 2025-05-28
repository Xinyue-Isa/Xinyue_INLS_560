# This program determines whether a student qualifies for a 
# good college student discount of a badminton club

MIN_TOTAL_CREDITS = 12  # The minimum total credits that the student 
                        # earned in college
MIN_GPA = 3.0        # The minimum overall GPA in college

# Get the student's total credits in college
credits = int(input('Enter your total credits: '))

# Get the student's overall GPA.
gpa = float(input('Enter your overall GPA: '))

# Determine whether the student qualifies.
if credits >= MIN_TOTAL_CREDITS and gpa >= MIN_GPA:
    print('You qualify for this good student discount.')
else:
    print(f'''Sorry, you do not qualify for this good student discount. 
          You need a minimum of {MIN_TOTAL_CREDITS} total credits and at least 
          a {MIN_GPA} GPA. ''')