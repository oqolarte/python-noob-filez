import requests
from bs4 import BeautifulSoup

def allstories(f):
    page=requests.get(f)
    soup=BeautifulSoup(page.text,"html.parser")
    print("STORIES CURRENTLY ON NYTIMES.COM (in order of appearance):\n")
    for art in soup.find_all("h2", class_="story-heading"):
        arttitle=art.string
        if arttitle is not None:
            t=str(arttitle).strip()
            print(t)

allstories("https://aklas.xyz")
