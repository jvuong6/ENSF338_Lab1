import re
import timeit
import numpy as np
import matplotlib.pyplot as plt

file_path = "pg2701.txt"

# pattern to match vowels
vowel_pattern = re.compile(r'[aeiouy]', re.IGNORECASE)

# pattern to match whole words
word_pattern = re.compile(r'\b\w+\b')


#counts the number of vowels in given word
def vowel_counter(word):
    return len(vowel_pattern.findall(word))

def record_processing(num_records):
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

    for line in lines[index:index + num_records]:
        words = word_pattern.findall(line)
        total_vowels += sum(vowel_counter(word) for word in words)
        total_words += len(words)

    file.close()
    #print avg vowels
    avg_vowels = total_vowels / total_words
    return avg_vowels

def main():
    records = 1000
    repeats = 1000

    times = timeit.repeat(lambda: record_processing(records), number=1, repeat=repeats)

    # Plot histogram of measured times
    plt.figure(figsize=(8, 6))
    plt.hist(times, bins=30, color='blue', edgecolor='black', alpha=0.7)
    
    # Adding titles and labels
    plt.title('Distribution of Processing Times for 1000 Records')
    plt.xlabel('Processing Time (seconds)')
    plt.ylabel('Frequency')

    # Save the plot as a PNG file
    plt.savefig('output.3.3.png')

    # Optionally, show the plot
    plt.show()

    plt.show()

if __name__ == "__main__":
    main()