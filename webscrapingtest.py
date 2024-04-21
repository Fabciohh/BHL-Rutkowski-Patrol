from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import os
# Ścieżka do pliku wykonywalnego Chrome WebDriver
os.environ['PATH'] += os.pathsep + os.getcwd()

# Adres URL strony do scrapowania
url = 'https://www.pudelek.pl'
options = webdriver.ChromeOptions()
options.headless = True

# Utwórz obiekt WebDriver dla przeglądarki Chrome
with webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options,) as driver:
    driver.get(url)
# Wczytaj stronę


# Wykonaj skrypt JavaScript, aby otworzyć wszystkie divy
javascript_code = """
var divs = document.querySelectorAll('div');
divs.forEach(function(div) {
    div.style.display = 'block';
});
"""
driver.execute_script(javascript_code)

# Pobierz kod źródłowy strony
html_content = driver.page_source

# Zamknij przeglądarkę
driver.quit()

# Parsuj kod HTML za pomocą Beautiful Soup
soup = BeautifulSoup(html_content, 'html.parser')

# Znajdź wszystkie elementy <div>
divs = soup.find_all('div')

# Wyświetl treść wszystkich elementów <div>
for div in divs:
    print(div.text.strip())