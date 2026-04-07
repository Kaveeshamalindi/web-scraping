import requests
from bs4 import BeautifulSoup

url = "http://books.toscrape.com/"

# Send request
response = requests.get(url)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all books
books = soup.find_all("article", class_="product_pod")

# Extract data
for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    
    print("Title:", title)
    print("Price:", price)
    print("-" * 30)