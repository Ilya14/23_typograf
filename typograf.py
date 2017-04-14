from re import sub


def get_replacement_rules():
    nbsp = '\u00A0'
    ndash = '\u2013'
    replacement_rules = [
        # quotes replacement
        (r'("|\')(.*)\1', r'«\2»'),
        # removal of excess gaps and transfers of lines
        (r'\s+', r' '),
        # replacement of hyphens by a short dash in phone numbers
        (r'(8|\+7)\s*\(\s*(\d{1,3})\s*\)\s*(\d{3})\s*-\s*(\d{2})\s*-\s*(\d{2})',
         r'\1 (\2) \3{0}\4{0}\5'.format(ndash)),
        # hyphens replacement
        (r'\s+-\s+', ' \u2014 '),
        # linking of numbers with the subsequent words
        (r'(\b[а-яА-Яa-zA-Z]{1,2}\b)(\s+)(\b[а-яА-Яa-zA-Z]+\b)', r'\1{0}\3'.format(nbsp)),
        # linking of the unions and any words from 1-2 symbols with the subsequent words
        (r'(\b\d+\b)(\s+)(\b[а-яА-Яa-zA-Z]+\b)', r'\1{0}\3'.format(nbsp))
    ]
    return replacement_rules


def process_text(text):
    for pattern, replacement in get_replacement_rules():
        text = sub(pattern, replacement, text)
    return text


if __name__ == "__main__":
    pass
