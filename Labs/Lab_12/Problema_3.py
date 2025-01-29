"""Scrieti un script Python care sa faca urmatoarele:
Interogheaza API-ul CoinGecko pentru a obtine preturile actuale ale criptomonedelor Bitcoin
si Ethereum in dolari (USD).
Extrage cele mai recente 5 stiri legate de criptomonede de pe site-ul CoinDesk utilizand
tehnica de web scraping cu biblioteca BeautifulSoup.
Afiseaza preturile criptomonedelor intr-un format tabelar, utilizand pachetul tabulate.
Afiseaza titlurile celor mai recente 5 stiri extrase, impreuna cu link-urile acestora."""

import requests
from bs4 import BeautifulSoup
from tabulate import tabulate


def get_crypto_prices():
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum&vs_currencies=usd"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return [("Bitcoin", data["bitcoin"]["usd"]), ("Ethereum", data["ethereum"]["usd"])]
    except requests.exceptions.RequestException as e:
        print(f"Eroare la preluarea preturilor criptomonedelor: {e}")
        return None


def get_crypto_news():
    url = "https://www.coindesk.com/"
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.find_all("a", class_="headline", limit=5)
        news = [(article.get_text(strip=True), url + article["href"]) for article in articles]
        return news
    except requests.exceptions.RequestException as e:
        print(f"Eroare la preluarea stirilor: {e}")
        return None


def main():
    print("\nPreturile actuale ale criptomonedelor:")
    prices = get_crypto_prices()
    if prices:
        print(tabulate(prices, headers=["Criptomoneda", "Preț (USD)"], tablefmt="grid"))

    print("\nCele mai recente 5 știri despre criptomonede:")
    news = get_crypto_news()
    if news:
        for title, link in news:
            print(f"- {title}: {link}")


if __name__ == "__main__":
    main()
