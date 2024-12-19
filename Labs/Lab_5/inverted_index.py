def inverted_index(documents):
    index = {}
    for doc_id, document in enumerate(documents):
        words = document.lower().split()
        for word in words:
            if word not in index:
                index[word] = set()
            index[word].add(doc_id)
    return index
n = int(input("Introduceți numărul de documente: "))
documents = [input(f"Introduceți documentul {i + 1}: ") for i in range(n)]
print(inverted_index(documents))
