import requests
from bs4 import BeautifulSoup
import csv

URL = "https://books.toscrape.com/"

try:
    # Send request to the website
    response = requests.get(URL, timeout=10)
    response.raise_for_status()

except requests.RequestException as e:
    print("Error while fetching website:", e)

else:
    # Convert HTML into a BeautifulSoup object
    soup = BeautifulSoup(response.text, "html.parser")

    # Find all book containers
    books = soup.select("article.product_pod")

    data = []

    # Extract information from each book
    for book in books:

        title = book.h3.a["title"]

        price = book.select_one(".price_color").get_text(strip=True)

        availability = book.select_one(".availability").get_text(
            " ", strip=True
        )

        data.append([title, price, availability])

        # Display extracted information
        print("Title:", title)
        print("Price:", price)
        print("Availability:", availability)
        print("-" * 40)

    # Save the scraped data into CSV
    with open("books.csv", "w", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Title",
            "Price",
            "Availability"
        ])

        writer.writerows(data)

    print("\nScraping completed successfully!")
    print("Total books scraped:", len(data))
    print("Data saved in books.csv")