import random


def generate_poem_from_string(input_string, file_name):
    # Reading the word list from the file
    with open(file_name, 'r') as file:
        common_words_list = file.read().splitlines()

    # Extracting the first letter of each word in the input string
    first_letters = [word[0].lower() for word in input_string.split()]

    poem_array = []
    for index, letter in enumerate(first_letters):
        # Filtering words that start with the current letter
        possible_words = [word for word in common_words_list if word.startswith(letter)]

        # Selecting a random word from the filtered list
        if possible_words:
            chosen_word = random.choice(possible_words)
            # Capitalize the first word of each sentence
            if index == 0:
                poem_array.append(chosen_word.capitalize())
            else:
                poem_array.append(chosen_word.lower())
        else:
            poem_array.append("(No word found for letter '{}')".format(letter.upper()))

    # Joining the words to form a poem
    return ' '.join(poem_array)


# Iterate through strings and generate sequences of unique words
array_of_strings = ["Have you ever wondered what it would be like to slide down the Milky Way",
                    "To experience the cosmos and feel the heat of the stars on your face",
                    "A rosy blush fills your cheeks, colored by the supernova of stars",
                    "I am ever entranced by the starlight that populates your eyes",
                    "If only this were an eternity, an ever expanding universe of affection"]

for string in array_of_strings:
    poem = generate_poem_from_string(string, "10000_common_words.txt")
    print(poem)
