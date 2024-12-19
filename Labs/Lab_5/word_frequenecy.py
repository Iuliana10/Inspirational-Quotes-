import string

def word_frequency(text):
    translator = str.maketrans('', '', string.punctuation)
    text_cleaned = text.translate(translator)
    text_lower = text_cleaned.lower()
    words = text_lower.split()
    frequency = {}
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency
text = "Acesta este un exemplu. Acesta este doar un test!"
print(word_frequency(text))
