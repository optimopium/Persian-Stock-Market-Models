# views.py
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.utils.html import format_html
from .rule_based_detector.detector import extract_symbol_spans
from data.loaders import load_symbols_from_csv


@csrf_exempt
def keyword_extraction_view(request):
    try:
        # Load symbols from the CSV file
        symbols_data = load_symbols_from_csv(columns=['symbol'])
        keywords = [d['symbol'] for d in symbols_data]
    except FileNotFoundError:
        return render(request, 'symbol_detector/extract_keywords.html', {
            'error': 'The symbols file was not found.'
        })
    except Exception as e:
        return render(request, 'symbol_detector/extract_keywords.html', {
            'error': f'An error occurred: {e}'
        })

    if request.method == 'POST':
        # Process the form submission
        text = request.POST.get('text', '')

        # Call the function with the provided text and keywords
        results = extract_symbol_spans(text, keywords)

        # Sort results by start span for proper replacement without overlap
        results.sort(key=lambda x: x['span'][0], reverse=True)

        # Build the highlighted text
        highlighted_text = text
        for result in results:
            start, end = result['span']
            highlighted_text = (
                    highlighted_text[:start] +
                    format_html('<span class="highlight">{}</span>', highlighted_text[start:end]) +
                    highlighted_text[end:]
            )

        # Render the results with highlighted text
        return render(request, 'symbol_detector/extract_keywords.html', {
            'highlighted_text': highlighted_text
        })
    else:
        # Render an empty form for GET request
        return render(request, 'symbol_detector/extract_keywords.html', {'keywords': keywords})
