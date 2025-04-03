# BookBot

BookBot is a Python-based command-line tool designed to analyze text files. It provides insights into the content of books by performing the following tasks:

- **Word Count**: Calculates the total number of words in the book.
- **Character Frequency**: Counts the occurrences of each character in the book.
- **Sorted Character List**: Displays a sorted list of character frequencies, focusing on alphabetical characters.

## Usage

To use BookBot, run the `main.py` script with the path to a text file as an argument:

```bash
python3 [main.py](./main.py) <path_to_book>
```

For example:

```bash
python3 [main.py](./main.py) [frankenstein.txt](./books/frankenstein.txt)
```

## Example Output

```bash
============ BOOKBOT ============
Analyzing book found at books/frankenstein.txt...
----------- Word Count ----------
Found 78452 total words
--------- Character Count -------
a: 4821
b: 1234
c: 2345
...
============= END ===============
```

## Project Structure

- `main.py`: The main script to run the BookBot tool.
- `stats.py`: Contains helper functions for counting words and characters.
- `books/`: Directory containing sample text files for analysis.
