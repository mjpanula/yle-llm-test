from funktiot import fetch_yle_news, extract_text_from_html
import os
from mistralai import Mistral

api_key = os.environ["MISTRAL_API_KEY"]
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

news_data = fetch_yle_news()
readable_text = extract_text_from_html(news_data)
#print(readable_text)

prompt_content = "Valitse yksi tärkeä uutinen ja kerro uutinen sekä uutiseen liittyviä taustatietoja: "
prompt_content += readable_text
chat_response = client.chat.complete(
    model= model,
    messages = [
        {
            "role": "user",
            "content": prompt_content,
        },
    ]
)
print(chat_response.choices[0].message.content)