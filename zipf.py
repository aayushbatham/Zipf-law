import json
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter

# Function to clean text
def clean_text(text):
    # Remove punctuation and convert to lowercase
    cleaned_text = text.lower().replace('\n', ' ')
    return cleaned_text

# Function to read text from a .txt file
def read_text(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        text = file.read()
    return text

# Function to plot Zipf's Law
def plot_zipf_law(text, output_filename):
    # Tokenize the text
    words = text.split()
    # Get word frequencies
    word_freq = Counter(words)
    # Sort words by frequency in descending order
    sorted_word_freq = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    # Get ranks and frequencies
    ranks = np.arange(1, len(sorted_word_freq) + 1)
    frequencies = [pair[1] for pair in sorted_word_freq]
    
    # Plot Zipf's Law
    plt.figure(figsize=(10, 6))
    plt.loglog(ranks, frequencies, marker='.')
    plt.title("Zipf's Law")
    plt.xlabel('Rank')
    plt.ylabel('Frequency')
    plt.grid(True)
    
    # Show word along with its frequency
    for i in range(min(10, len(sorted_word_freq))):  # Show top 10 words
        plt.text(ranks[i], frequencies[i], f'{sorted_word_freq[i][0]}: {sorted_word_freq[i][1]}', fontsize=9, va='center', ha='left')

    plt.savefig(output_filename)  # Save the plot as PNG
    plt.show()
    
    # Save word frequencies as JSON
    word_freq_dict = {word: freq for word, freq in sorted_word_freq}
    with open(json_output_filename, 'w') as json_file:
        json.dump(word_freq_dict, json_file, indent=4)

    print("Word frequencies saved as:", json_output_filename)

# Path to the text file
file_path = './input-text/atomicdesign.txt'
output_filename = './plots/zipf_law_plot.png'
json_output_filename = './word-freq/word_frequencies.json'

# Read text from the file
text = read_text(file_path)

# Clean the text
cleaned_text = clean_text(text)

# Plot Zipf's Law and save as PNG
plot_zipf_law(cleaned_text, output_filename)

print("Plot saved as:", output_filename)
