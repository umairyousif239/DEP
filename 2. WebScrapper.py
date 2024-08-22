# Description: This script scrapes the top releases from the Readings website and saves the data to a CSV file.
import csv
from bs4 import BeautifulSoup
import requests

# URL of the page to scrape
url = 'https://readings.com.pk/sub-menu/new-releases/R'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Name of the CSV file to save the data
csv_file = 'Top Releases By Readings.csv'

# Find the book titles and authors
book_elements = soup.find_all('div', class_='product-title')
author_elements = soup.find_all('div', class_='author')

# Print the number of books found
print(f'Found {len(book_elements)} books.')

# Open the CSV file in write mode
with open(csv_file, 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Titles', 'Authors'])

    # Extract book titles and authors and write to the CSV file
    for book_element, author_element in zip(book_elements, author_elements):
        book_title = book_element.get_text(strip=True)
        author = author_element.get_text(strip=True)
        writer.writerow([book_title, author])

# Print a message
print(f'Data has been scraped and saved to {csv_file}.')