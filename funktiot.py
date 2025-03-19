import requests
from bs4 import BeautifulSoup

def fetch_yle_news():
    url = "https://yle.fi/"
    response = requests.get(url)
    data = response.text
    return data

def extract_text_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text(separator='\n')
    return text