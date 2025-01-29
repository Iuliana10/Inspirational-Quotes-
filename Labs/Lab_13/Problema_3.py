"""Scrie un program in Python care preia cursurile de schimb valutar de pe o sursa publica API si
convertește o suma data dintr-o moneda intr-o alta moneda, folosind ratele de schimb actuale.
import requests"""

def get_exchange_rates():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data["rates"]
    except requests.exceptions.RequestException as e:
        print(f"Eroare la obținerea cursurilor de schimb: {e}")
        return None


def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency not in rates or to_currency not in rates:
        print("Moneda introdusă nu este validă.")
        return None

    converted_amount = (amount / rates[from_currency]) * rates[to_currency]
    return round(converted_amount, 2)


def main():
    rates = get_exchange_rates()
    if not rates:
        return

    from_currency = input("Introdu moneda de proveniență (ex: USD, EUR, RON): ").upper()
    to_currency = input("Introdu moneda de destinație (ex: USD, EUR, RON): ").upper()

    try:
        amount = float(input("Introdu suma de convertit: "))
    except ValueError:
        print("Suma introdusă nu este validă.")
        return

    result = convert_currency(amount, from_currency, to_currency, rates)

    if result is not None:
        print(f"{amount} {from_currency} echivalează cu {result} {to_currency}.")


if __name__ == "__main__":
    main()
