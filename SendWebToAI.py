import openai
import WebChecker
import WebScrapingSelenium
# Ustaw klucz API dla swojego konta OpenAI
# tu klucz chatgpt
message = WebChecker.message
# Funkcja do wysyłania danych tekstowych do chatu GPT
message_complete = "Na podstawie poniższej wiadomości napisz w skali od 1 do 100 jak prawdopodobne jest to, ze tresc to phishing, napisz tylko liczbe" + message
def send_to_chat(message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "User: " + message_complete}
        ]
    )
    response_message = response.choices[0].message['content']
    print("Prawdopodobieństwo, ze strona to zagrozenie: ", response_message)


def user_prompt(response_message):
    propability = float(response_message)
    if propability > 0.3 and propability <= 0.6:
        print("Poziom zagrozenia Sredni")
        chat_response()
    elif propability > 0.6 and propability <= 0.8 :
        print("Poziom zagrozenia Wysoki")
        chat_response()
    elif propability > 0.8:
        print("Poziom zagrozenia Krytyczny")
        chat_response()


def chat_response():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "User: " + "Uzasadnij swoja odpowiedz"}
        ]
    )
    response_message = response.choices[0].message['content']
    print("Uzasadnienie: ", response_message)