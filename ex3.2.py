import re
import timeit
import numpy as np
import matplotlib as plt
from sklearn.linear_model import LinearRegression

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
    record_sizes = [1000, 2000, 5000, 10000]
    repeats = 100

    avg_times = []

    for size in record_sizes:
        times = timeit.repeat(lambda: record_processing(size), number=1, repeat=repeats)
        avg_times.append(np.mean(times))

    x = np.array(record_sizes).reshape(-1, 1)  # x is the num records
    y = np.array(avg_times)  # y is the average processing time

    model = LinearRegression()
    model.fit(x, y)

    # Get the regression line's predicted values
    predicted_y = model.predict(x)

    # Plotting the results
    plt.figure(figsize=(8, 6))
    plt.scatter(record_sizes, avg_times, color='blue', label='Measured times')
    plt.plot(record_sizes, predicted_y, color='red', label='Linear regression', linestyle='--')

    # Adding titles and labels
    plt.title('Linear Regression of Processing Time vs. Number of Records')
    plt.xlabel('Number of Records')
    plt.ylabel('Average Processing Time (seconds)')
    plt.legend()

    plt.savefig('output.3.2.png')

    plt.show()
    
if __name__ == "__main__":
    main()