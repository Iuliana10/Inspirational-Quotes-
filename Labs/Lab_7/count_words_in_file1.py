def count_words_in_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            words = content.split()
            return len(words)
    except FileNotFoundError:
        print(f"Eroare: Fișierul '{filename}' nu a fost găsit.")
        return 0

file_name = "example.txt"
word_count = count_words_in_file(file_name)
print(f"Numărul total de cuvinte din '{file_name}' este: {word_count}")
