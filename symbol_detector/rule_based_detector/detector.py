import re


def extract_symbol_spans(text, keywords):
    """
    Find the spans of each keyword or '#keyword' in the text and return a list of dictionaries.
    The function matches keywords as whole words or with a '#' prefix.

    Parameters:
    text (str): The text to search within.
    keywords (list): A list of keywords to look for.

    Returns:
    list of dicts: Each dictionary contains 'keyword' and 'span', where 'span' is a tuple (start, end).
    """
    results = []

    # Use a pattern to match whole words or words preceded by #
    pattern_template = r'\b{}\b|\b(?=#){}\b'

    # Go through all keywords
    for keyword in keywords:
        # Find all non-overlapping occurrences of the keyword or #keyword
        pattern = pattern_template.format(re.escape(keyword), re.escape(keyword))
        for match in re.finditer(pattern, text, re.IGNORECASE):  # re.IGNORECASE to make it case-insensitive
            # Add the result as a dictionary with keyword and span
            matched_keyword = text[match.start():match.end()]
            results.append({'keyword': matched_keyword, 'span': match.span()})

    # Optional: Sort results by the order they appear in the text
    results.sort(key=lambda x: x['span'])

    return results
