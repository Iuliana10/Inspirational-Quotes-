import csv
def read_csv(file_path):
    data = []
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data
def filter_data(data, key, value):
    return [row for row in data if row.get(key) == value]
def write_csv(data, file_path):
    if not data:
        raise ValueError("Nu există date de scris în fișier.")
    with open(file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
if __name__ == "__main__":
    from data_processor_T6 import read_csv, filter_data, write_csv
    data = read_csv('people_T6.csv')
    print("Date citite:")
    for row in data:
        print(row)
    key = input("Introdu cheia pentru filtrare: ")
    value = input(f"Introdu valoarea pentru {key}: ")
    filtered_data = filter_data(data, key, value)
    print(f"\nDate filtrate pentru perechea '{key}: {value}':")
    for row in filtered_data:
        print(row)
    write_csv(filtered_data, 'filtered_people.csv')
    print("\nDatele filtrate au fost scrise în 'filtered_people.csv'.")

