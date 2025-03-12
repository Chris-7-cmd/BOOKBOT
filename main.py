import sys
from stats import get_num_words, get_char_count, sort_char_count

def get_book_text(filepath):
    """
    Read and return the contents of a file.
    
    Args:
        filepath (str): Path to the file to read
        
    Returns:
        str: Contents of the file
    """
    with open(filepath, 'r') as file:
        return file.read()

def main():
    # Check if the correct number of arguments were provided
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Get book path from command line argument
    filepath = sys.argv[1]
    
    # Get book content
    book_content = get_book_text(filepath)
    
    # Count the words in the book
    num_words = get_num_words(book_content)
    
    # Get the character count dictionary
    char_count_dict = get_char_count(book_content)
    
    # Sort the character counts
    sorted_chars = sort_char_count(char_count_dict)
    
    # Print the report
    print("========== BOOKBOT ==========")
    print(f"Analyzing book found at {filepath}...")
    print("---------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    
    
    # Print each alphabetical character and its count
    for char_info in sorted_chars:
        char = char_info['char']
        count = char_info['count']
        
        # Only print alphabetical characters
        if char.isalpha():
            print(f"{char}: {count}")
    
    print("=========== END ==============")

# Call main() to execute the program
if __name__ == "__main__":
    main()
