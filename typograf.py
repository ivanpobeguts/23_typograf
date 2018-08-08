import re


replace_patterns = [
    (r'\d', r'D'),
]


def edit_text(text):
    for pattern, replacement in replace_patterns:
        text = re.sub(pattern, replacement, text)
    return text
