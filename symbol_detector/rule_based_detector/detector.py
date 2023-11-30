import re


def extract_symbol_spans(text, keywords):
    """
    Find the spans of each whole keyword in the text and return a list of dictionaries.
    The function avoids partial matches by ensuring that keywords are space-separated.

    Parameters:
    text (str): The text to search within.
    keywords (list): A list of keywords to look for.

    Returns:
    list of dicts: Each dictionary contains 'keyword' and 'span', where 'span' is a tuple (start, end).
    """
    results = []

    # Use a word boundary pattern to match whole words only
    word_pattern = r'\b{}\b'

    # Go through all keywords
    for keyword in keywords:
        # Find all non-overlapping occurrences of the keyword as a whole word
        pattern = word_pattern.format(re.escape(keyword))
        for match in re.finditer(pattern, text, re.IGNORECASE):  # re.IGNORECASE to make it case-insensitive
            # Add the result as a dictionary with keyword and span
            results.append({'keyword': keyword, 'span': match.span()})

    # Optional: Sort results by the order they appear in the text
    results.sort(key=lambda x: x['span'])

    return results
