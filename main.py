
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

with open('./books/frankenstein.txt') as f:
        file_contents = f.read()

counts = letter_count(file_contents)
number_of_letters = letter_count(file_contents)
print(number_of_letters)
print(counts)

