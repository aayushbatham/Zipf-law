# Zipf's Law Visualization

## Overview
This Python project aims to demonstrate and visualize Zipf's Law, which is an empirical law stating that given a large sample of words used, the frequency of any word is inversely proportional to its rank in the frequency table. In simpler terms, the most frequent word will occur approximately twice as often as the second most frequent word, three times as often as the third most frequent word, and so forth.

## Inspiration
Inspirted by the video of Vsauce on Youtube https://www.youtube.com/watch?v=fCn8zs912OE, You should check this out

## Installation
1. Clone or download the repository to your local machine.
2. Make sure you have Python installed on your system. This project requires Python 3.x.
3. Install the required dependencies using pip:
    ```
    pip install matplotlib numpy
    ```
4. Run the main Python script to visualize Zipf's Law.

## Usage
1. Prepare a text file (.txt) containing the corpus you want to analyze.
2. Place your text file (.txt) in the input-text folder
3. Run the Python script `zipf.py`.
4. The script will generate a plot visualizing Zipf's Law and save it as `zipf_law_plot.png` in the plots folder. It will also save the word frequencies as a JSON file (`zipf_law_plot.json`) in word-freq folder.
5. You can customize the plot appearance and other parameters in the Python script as needed.

## Example
For example, you can use a text file containing a novel, article, or any large piece of text to analyze the frequency distribution of words according to Zipf's Law.

## References
- [Wikipedia - Zipf's Law](https://en.wikipedia.org/wiki/Zipf%27s_law)
- [Matplotlib Documentation](https://matplotlib.org/)
- [NumPy Documentation](https://numpy.org/doc/)

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
