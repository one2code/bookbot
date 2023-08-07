import os

def get_directory():
    attempts = 0
    while attempts < 3:
        directory_path = get_directory_from_user()
        if directory_path:
            return directory_path
        attempts += 1
    print("Too many failed attempts. Exiting program.")
    return None
def get_directory_from_user():
    directory_path = input("Please enter the directory path to process: ")
    if os.path.isdir(directory_path) and os.access(directory_path, os.R_OK):
        return directory_path
    else:
        print("Invalid or inaccessible directory path. Please try again.")
        return None

def word_count(text):
    return len(text.split())

def letter_count(text):
    text = text.lower()
    letter_counts = {}

    for letter in text:
        if letter.isalpha():
            letter_counts[letter] = letter_counts.get(letter, 0) + 1
    return letter_counts

def process_file(file_path):
    if not os.access(file_path, os.R_OK):
        print(f"Permission denied for {file_path}")
        return

    try:
        with open(file_path, 'r') as f:
            file_contents = f.read()
            if '\0' in file_contents:
                print(f"Binary file detected: {file_path}")
                return

        words_counted = word_count(file_contents)
        counts = letter_count(file_contents)
        char_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)

        print(f"---Begin report of {file_path}---\n")
        print(f"{words_counted} words found in the document\n")
        for char, count in char_counts:
            print(f"The letter {char} was found {count} times")
        print("---End report---\n")

    except Exception as e:
        print(f"Failed to process {file_path}: {str(e)}")

def main():
    directory_path = get_directory()
    if directory_path:
        for filename in os.listdir(directory_path):
            if filename.endswith('.txt'):
                file_path = os.path.join(directory_path, filename)
                process_file(file_path)

if __name__ == "__main__":
    main()
