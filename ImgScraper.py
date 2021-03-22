from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request

print("-------------------------------")
print("Web Image Scraper")
print("Easily download all pictures from one URL!")
print("(all items are saved in current directory)")
print("-------------------------------")
print("Enter your desired URL (e.g: https://github.com/):")
url = input()
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
print("-------------------------------")

expr = soup.find_all("img")
if not expr:
    print("No tags found...")
else:
    try:
        for src in expr:
            picsrc = src['src']
            print(picsrc)
            filename = picsrc.split('/')[-1]
            print("Filename: "+ filename)
            srccheck = picsrc[0:4]
            if srccheck != "http":
                picsrc = url + picsrc
            urllib.request.urlretrieve(picsrc, filename)

    except ValueError:
        print("Ive made a whoopsie doopsie")
