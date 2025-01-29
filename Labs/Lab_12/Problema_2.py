"""Scrie un script Python care interactioneaza cu un API public pentru a obtine informatii despre
vremea dintr-un oras specificat de utilizator. API-ul folosit este wttr.in, care ofera date meteo in
format text simplu."""

import requests


def obtine_vremea(oras):
    url = f"https://wttr.in/{oras}?format=%C+%t+%w"
    try:
        response = requests.get(url, verify=False)
        response.raise_for_status()
        return response.text.strip()
    except requests.exceptions.RequestException as e:
        print(f"Eroare la preluarea datelor meteo: {e}")
        return None


def main():
    oras = input("Introduceți numele orașului: ").strip()
    vremea = obtine_vremea(oras)

    if vremea:
        print(f"Vremea în {oras}: {vremea}")
    else:
        print("Orasul nu a fost gasit sau a aparut o eroare.")


if __name__ == "__main__":
    main()
