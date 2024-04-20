import requests
from selenium import webdriver
from bs4 import BeautifulSoup
# Ścieżka do pliku wykonywalnego Chrome WebDriver (zmień na swoją lokalizację)
webdriver_path = '/chromedriver.exe'
def parse_html(html_content):
    # Parsowanie kodu HTML przy użyciu BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')
def get_html_content(url):
    # Utworzenie obiektu WebDriver dla przeglądarki Chrome
    Driver = webdriver.Chrome(executable_path=webdriver_path)

# Adres URL strony do scrapowania
url = 'https://majtkomat.pl'

Driver.get(url)
Driver.get_cookies()

# Ustawienie User-Agent String jako Google Bot
headers = {
    'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
}

# Wysłanie żądania HTTP z odpowiednimi nagłówkami
response = requests.get(url, headers=headers)
html_content = response.text

# Parsowanie kodu HTML przy użyciu Beautiful Soup
# soup = BeautifulSoup(html_content, 'html.parser')

# Znalezienie wszystkich tytułów artykułów
titles = parse_html(html_content).find_all('div')

# Wyświetlenie znalezionych tytułów
for title in titles:
    print(title.text)

Driver.delete_all_cookies()