def madlib(adj1, snack_types, verb, celebrity, noun, emotion, movie_genre):
    ''' Madlib using a function'''
    story = (f'''        
    A Night at the Movies: 
    Last night, I went to the cinema to see a {adj1} film. 
    As I entered the theater, the smell of {snack_types} hit me instantly. 
    While I was {verb} to my seat, I nearly bumped into {celebrity} carrying a giant {noun}!
    The lights dimmed, and I felt a rush of {emotion} as the trailers started. 
    The movie was a(n) {movie_genre} masterpiece, and by the end, the whole audience 
    was on their feet clapping.
    ''')
    return story
print(madlib("comedic", "popcorn", "walking", "Taylor Swift", "umbrella", "excitement", "musical"))

def get_input():
    adj1 = input('Please enter an adjective: ')
    snack_type = input('Please enter a type of snack: ')
    verb = input('Please enter a verb, ending in -ing: ')
    celebrity = input('Please enter a name of one celebrity: ')
    noun = input('Please enter a noun: ')
    emotion = input('Please enter an emotion: ')
    movie_genre = input('Please enter a movie genre: ')
    return adj1, snack_type, verb, celebrity, noun, emotion, movie_genre
inputs = get_input()
print(madlib(*inputs))