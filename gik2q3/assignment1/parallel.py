import os
from collections import Counter
import concurrent.futures
import pandas as pd

def count_words_in_file(filename):
    word_count = Counter()
    with open(filename, 'r') as file:
        for line in file:
            word_count.update(line.strip().split())
    return word_count

def word_count_parallel(directory, max_workers=None):
    filepaths = [os.path.join(directory, filename) for filename in os.listdir(directory) if filename.endswith('.txt')]
    total_count = Counter()

    with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
        for word_count in executor.map(count_words_in_file, filepaths):
            total_count.update(word_count)

    return total_count

if __name__ == '__main__':
    directory = "./dataset"

    word_counts_parallel = word_count_parallel(directory)
    df_word_counts_parallel = pd.DataFrame(word_counts_parallel.items(), columns=['Word', 'Count'])
    print(df_word_counts_parallel.head())
