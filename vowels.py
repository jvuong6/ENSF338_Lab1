import re
import timeit

file_path = "pg2701.txt"

# pattern to match vowels
vowel_pattern = re.compile(r'[aeiouy]', re.IGNORECASE)

# pattern to match whole words
word_pattern = re.compile(r'\b\w+\b')


#counts the number of vowels in given word
def vowel_counter(word):
    return len(vowel_pattern.findall(word))

def main():
    start_after_line = "EXTRACTS (Supplied by a Sub-Sub-Librarian).\n"

    file = open(file_path, "r", encoding='utf-8')
    lines = file.readlines()

    #find the starting line
    index = 0
    for i, line in enumerate(lines):
        if start_after_line in line:
            index = i + 1

    total_vowels = 0
    total_words = 0

    for line in lines[index:]:
        words = word_pattern.findall(line)
        total_vowels += sum(vowel_counter(word) for word in words)
        total_words += len(words)


    #print avg vowels
    avg_vowels = total_vowels / total_words
    print(f"Average vowels per word: {avg_vowels:.3f}")

    file.close()

if __name__ == "__main__":
    elapsed_time = timeit.timeit(lambda: main(), number = 100)
    print(f"Average time: {elapsed_time / 100} seconds")