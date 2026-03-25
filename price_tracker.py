import requests
from bs4 import BeautifulSoup
import csv
from datetime import datetime

try:
    response = requests.get("http://books.toscrape.com/" , timeout = 5)
    html = response.text
    soup = BeautifulSoup(html , "html.parser")
    books = soup.find_all("article" , class_ = "product_pod")
    with open("price_listings.csv" , "w" , newline="" , encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title" , "Price" , "Date"])
        for book in books:
            title = book.h3.a["title"]
            price = book.find("p" , class_ = "price_color").text
            date = datetime.now().strftime("%Y - %m - %d")
            writer.writerow([title , price , date])
            
except requests.exceptions.Timeout:
    print("Server took too long to respond")
except requests.exceptions.ConnectionError:
    print("No internet connection try again later")
    