import time
import pygetwindow as gw
import WebScrapingSelenium

global url, message
# Funkcja do monitorowania zmiany adresu URL w aktywnych oknach przeglądarki
def monitor_browser_urls(interval=5):
    # Początkowa lista odwiedzonych adresów URL
    visited_urls = set()
    while True:
        # Pobierz listę wszystkich otwartych okien
        windows = gw.getWindowsWithTitle('')

        # Przejrzyj każde otwarte okno
        for window in windows:
            # Sprawdź, czy okno przeglądarki
            if "chrome" in window.title.lower():
                # Pobierz adres URL aktywnego okna przeglądarki
                url = window.url
                if url and url not in visited_urls:
                    WebScrapingSelenium.scrape_div_text(url)
                    visited_urls.add(url)
        time.sleep(interval)


# Wywołaj funkcję monitorującą co 5 sekund
monitor_browser_urls()