def get_num_words(text):
    """
    Count the number of words in a string.
    
    Args:
        text (str): The text to count words in
        
    Returns:
        int: The number of words in the text
    """
    words = text.split()
    return len(words)

def get_char_count(text):
    """
    Count occurrences of each character in a string.
    
    Args:
        text (str): The text to analyze
        
    Returns:
        dict: Dictionary mapping characters to their counts
    """
    # Convert all characters to lowercase
    text = text.lower()
    
    # Create a dictionary to store character counts
    char_count = {}
    
    # Count each character
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    
    return char_count

def sort_char_count(char_dict):
    """
    Sort character count dictionary by count from greatest to least.
    
    Args:
        char_dict (dict): Dictionary mapping characters to their counts
        
    Returns:
        list: Sorted list of dictionaries with 'char' and 'count' keys
    """
    sorted_chars = []
    
    for char, count in char_dict.items():
        sorted_chars.append({'char': char, 'count': count})
    
    # Sort from greatest to least by count
    sorted_chars.sort(key=lambda x: x['count'], reverse=True)
    
    return sorted_chars