import os

def word_count(text):
    return len(text.split())


def letter_count(text):
    text = text.lower()
    letter_counts = {}

    for letter in text:
        if letter.isalpha():
            if letter in letter_counts:
                letter_counts[letter] += 1
            else:
                letter_counts[letter] = 1
    return letter_counts


directory_path = './books'

for filename in os.listdir(directory_path):
    if filename.endswith('.txt'):
        file_path = os.path.join(directory_path, filename)

with open(file_path) as f:
    file_contents = f.read()

words_counted = word_count(file_contents)

counts = letter_count(file_contents)
number_of_letters = letter_count(file_contents)
char_counts = list(counts.items())
char_counts.sort(key=lambda x: x[1], reverse=True)

print(f"---Begin report of {file_path}---\n")

print(f"{words_counted} words found in the document\n")
for char, count in char_counts:
    if char.isalpha():
        print(f"The letter {char} was found {count} times")
