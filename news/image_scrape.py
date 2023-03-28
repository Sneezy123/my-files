'''
@author: Nils Müller
@version: 1.0
@description: Scrape images off Bing and save them in directories on the computer
'''


# Import packages for scraping images off the internet

import os  # Import the 'os' package to get paths and create directories
import requests  # Import the 'requests' package to get the content off the internet
from bs4 import BeautifulSoup  # Import 'bs4' to get the URLs to the images
import urllib.parse  # Import 'urllib.parse' to convert from URL-decoded names to plain text
#                      e.g.: https://example.url/Hello%20World -> https://example.url/Hello World


def search_image(query: str) -> None:

    # Request the website

    # F-string with search URL
    url = f"https://www.bing.com/images/search?q={query}"
    req = requests.get(url)  # Request content from the URL
    data = req.text  # Get the text from the request

    # Get the URLs for the images and save them in a list. Filter 'bing' URLs

    soup = BeautifulSoup(data, 'html.parser')  # Define 'soup'

    img_list = []  # Create an empty image list

    # Find all image URLs on the website
    for item in soup.find_all("a", class_="inflnk"):
        # Pull the 'mediaurl=text' part out of the URL
        link = ("https://bing.com" + item["href"]).split("&")[4]
        # Check if the 'mediaurl' contains 'bing'
        if link.__contains__("bing") == False:
            link = link.split("=")[-1]  # Remove the 'mediaurl='
            # Convert from URL decoded to plain text as shown in line 13 (import urllib.parse)
            img_list.append(urllib.parse.unquote(link))

    # Get Current Working Directory (CWD) for saving

    cwd = os.getcwd()

    # Check if the directory for the query exists, if not create one with the name of the query e.g.: foo

    if not os.path.exists(f"{cwd}\\images\\{query}"):  # Check if directory exists
        os.makedirs(f"{cwd}\\images\\{query}")  # Create directory

    # Save the images that were scraped to the directory that was or was not created above.
    # The image files follow this naming convention: queryNum e.g.: foo13 or bar2 ...

    for i in range(len(img_list)):  # Loop over the 'img_list'
        # Get the image data and store it in 'img_data'
        img_data = requests.get(img_list[i]).content
        with open(f"images\\{query}\\{query}{i}.jpg", 'wb') as handler:  # Open directory
            handler.write(img_data)  # Save image in directory


if __name__ == "__main__":

    # Get a search query for an image

    query = input("Search query for picture: ")
    search_image(query)
