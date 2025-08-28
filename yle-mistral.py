from funktiot import fetch_yle_news, extract_text_from_html
import os
from groq import Groq

client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

news_data = fetch_yle_news()
readable_text = extract_text_from_html(news_data)
#print(readable_text)

prompt_content = "Valitse yksi tärkeä uutinen ja kerro uutinen sekä uutiseen liittyviä taustatietoja: "
prompt_content += readable_text
chat_response = client.chat.completions.create(
    model= "llama-3.3-70b-versatile",
    messages = [
        {
            "role": "user",
            "content": prompt_content,
        },
    ]
)
print(chat_response.choices[0].message.content)