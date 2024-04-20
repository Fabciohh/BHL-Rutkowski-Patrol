from bs4 import BeautifulSoup
from selenium import webdriver

# Adres URL strony, którą chcesz wczytać
url = 'https://www.majtkomat.pl'


# Pobranie kodu źródłowego strony za pomocą BeautifulSoup
def get_html_content(url):
    # Utworzenie obiektu WebDriver dla przeglądarki Chrome
    driver = webdriver.Chrome('chromedriver.exe')

    # Wczytanie strony
    driver.get(url)

    # Pobranie kodu źródłowego strony
    html_content = driver.page_source

    # Zamknięcie przeglądarki
    driver.quit()

    return html_content


# Parsowanie kodu HTML przy użyciu BeautifulSoup i wykonanie operacji na nim
def parse_html(html_content):
    # Parsowanie kodu HTML przy użyciu BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Tutaj możesz wykonywać operacje na kodzie HTML za pomocą BeautifulSoup

    # Przykładowe działanie - wyświetlenie tytułu strony
    title = soup.title
    print("Tytuł strony:", title.text)


# Pobranie kodu źródłowego strony za pomocą Selenium
html_content = get_html_content(url)

# Parsowanie kodu HTML i wykonanie operacji na nim
parse_html(html_content)