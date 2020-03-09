import requests
from bs4 import BeautifulSoup

urlLink = 'https://www.amazon.com/Mount-Computer-Articulating-Installation-Heavy-Duty/dp/B01HSJN0HK/ref=sr_1_3_sspa?crid=LWSTBDDHPDHU&keywords=monitor+stand+for+2+monitors&qid=1583784325&sprefix=monitor%2Caps%2C515&sr=8-3-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzVkFLV0xSWTg0Nko2JmVuY3J5cHRlZElkPUEwNTU3NDU2QjFVQVVKWTdMWDZVJmVuY3J5cHRlZEFkSWQ9QTA3MjUxMjIzUkhDQURDTDZCWUU4JndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

page = requests.get(urlLink)
print(page)