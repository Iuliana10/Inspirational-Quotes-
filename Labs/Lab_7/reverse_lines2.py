def reverse_lines(input_filename, output_filename):
    try:
        with open(input_filename, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()
        with open(output_filename, 'w', encoding='utf-8') as outfile:
            for line in lines:
                reversed_line = line.rstrip()[::-1]
                outfile.write(reversed_line + '\n')

        print(f"Fișierul '{output_filename}' a fost creat cu succes.")
    except FileNotFoundError:
        print(f"Fișierul '{input_filename}' nu a fost găsit.")
    except Exception as e:
        print(f"A apărut o eroare: {e}")
reverse_lines('input.txt', 'output.txt')
