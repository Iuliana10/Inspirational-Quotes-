def reverse_words(sentence):
    words = sentence.strip().split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)
sentence = input("Introdu o propoziție: ")
print(reverse_words(sentence))