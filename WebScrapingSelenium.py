from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import re
def scrape_div_text(url):
    # Utwórz opcje dla przeglądarki Chrome
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Uruchamia przeglądarkę w trybie bezokienkowym

    # Utwórz obiekt WebDriver dla przeglądarki Chrome
    with webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options) as driver:
        driver.get(url)

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

    # Parsuj kod HTML za pomocą Beautiful Soup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Znajdź wszystkie elementy <div>
    divs = soup.find_all('div')

    # Zbierz treść wszystkich elementów <div> bez zbędnych przerw i znaków nowej linii
    cleaned_texts = []
    for div in divs:
        cleaned_text = re.sub(r'\n+', ' ', div.text.strip())  # Usuń znaki nowej linii, zastępując je jednym spacją
        cleaned_texts.append(cleaned_text)

    return cleaned_texts

