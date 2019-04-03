#pass test 12 minutes

def find_hobbyiests(hobbies, hobby):
    s = []
    for k, v in hobbies.items():
        if hobby in v:
            s.append(k)
    return s

hobbies = {
    "John": ['Piano', 'Puzzles', 'Yoga'],
    "Adam": ['Drama', 'Fashion', 'Pets'],
    "Mary": ['Magic', 'Pets', 'Reading']
}

print(find_hobbyiests(hobbies, 'Yoga'))
