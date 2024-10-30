# Web Scraping
import requests
from bs4 import BeautifulSoup

# 1. Fetching HTML Content
url = "https://example.com"
response = requests.get(url)
html_content = response.text
print(html_content)

# 2. Parsing HTML with BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")
print(soup.title.text)

# 3. Extracting Links
links = soup.find_all('a')
for link in links:
    print(link.get('href'))

# 4. Extracting Text
text = soup.get_text()
print(text)

# 5. Finding Elements by Class
elements = soup.find_all(class_='example-class')
for element in elements:
    print(element.text)

# 6. Scraping Multiple Pages
for i in range(1, 6):  # Scrape pages 1 to 5
    url = f"https://example.com/page/{i}"
    response = requests.get(url)
    print(response.text)

# 7. Handling Exceptions
try:
    response = requests.get(url)
    response.raise_for_status()  # Raise an error for bad responses
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")

# 8. Saving Scraped Data to a CSV File
import csv

with open("scraped_data.csv", "w", newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Title", "Link"])  # Header
    for link in links:
        title = link.text
        href = link.get('href')
        writer.writerow([title, href])

# 9. Using User-Agent Headers
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
}
response = requests.get(url, headers=headers)

# 10. Scraping Data from an API
api_url = "https://api.example.com/data"
response = requests.get(api_url)
data = response.json()  # Assuming JSON response
print(data)

# 11. Using Regular Expressions for Scraping
import re

pattern = r"https?://[^\s]+"
urls = re.findall(pattern, text)
print(urls)

# 12. Using Selenium for Dynamic Content
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://example.com")
dynamic_content = driver.find_element_by_id("dynamic-id").text
print(dynamic_content)
driver.quit()

# 13. Delaying Requests
import time

for i in range(5):
    response = requests.get(url)
    print(response.text)
    time.sleep(2)  # Wait for 2 seconds between requests

# 14. Using BeautifulSoup to Filter Elements
specific_elements = soup.find_all("div", {"class": "specific-class"})
for element in specific_elements:
    print(element.text)

# 15. Handling Pagination
next_page = soup.find("a", class_="next")
if next_page:
    next_url = next_page.get("href")
    print(f"Next page URL: {next_url}")

# 16. Scraping a Table
table = soup.find("table")
rows = table.find_all("tr")
for row in rows:
    columns = row.find_all("td")
    data = [col.text for col in columns]
    print(data)

# 17. Extracting Meta Tags
meta_tags = soup.find_all("meta")
for tag in meta_tags:
    print(tag.get("name"), tag.get("content"))

# 18. Logging Requests
import logging

logging.basicConfig(level=logging.INFO)
logging.info("Fetching URL: %s", url)

# 19. Using Proxies
proxies = {
    "http": "http://your_proxy:port",
    "https": "http://your_proxy:port",
}
response = requests.get(url, proxies=proxies)

# 20. Closing Connections
response.close()
