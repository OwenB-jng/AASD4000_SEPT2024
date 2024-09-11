# each import statement, including an install for beautiful soup in case the user does not have it installed
import os
import requests
from bs4 import BeautifulSoup

# collecting a url, and parsing the html with beautiful soup
url = "https://www.nasa.gov/history/eclipses-near-and-far/"

response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')

# search for article text via the <p> tag
scraped_text = ""
for paragraph in soup.find_all('p'):
    scraped_text += paragraph.get_text() + "\n"

# placing the text in the created target directory in a txt file
output_directory = "scraped_articles"
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

file_path = os.path.join(output_directory, "scraped_article.txt")

with open(file_path, "a", encoding="utf-8") as file:
    file.write(scraped_text + "\n" + ("-" * 40) + "\n")

print(f"Atricle {file_path} saved to scraped_articles")