import os
from collections import Counter
import pandas as pd

def count_words_in_file(filename):
    word_count = Counter()
    with open(filename, 'r') as file:
        for line in file:
            word_count.update(line.strip().split())
    return word_count

def word_count_serial(directory):
    total_count = Counter()
    for filename in os.listdir(directory):
        if filename.endswith('.txt'):
            filepath = os.path.join(directory, filename)
            total_count.update(count_words_in_file(filepath))
    return total_count

if __name__ == '__main__':
    directory = "./dataset"

    word_counts_serial = word_count_serial(directory)
    df_word_counts_serial = pd.DataFrame(word_counts_serial.items(), columns=['Word', 'Count'])
    print(df_word_counts_serial.head())
