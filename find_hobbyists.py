#pass test 12 minutes

def find_hobbyiests(hobbies, hobby):
    for k, v in hobbies.items():
        if hobby in v:
            return k

hobbies = {
    "John": ['Piano', 'Puzzles', 'Yoga'],
    "Adam": ['Drama', 'Fashion', 'Pets'],
    "Mary": ['Magic', 'Pets', 'Reading']
}

print(find_hobbyiests(hobbies, 'Yoga'))
