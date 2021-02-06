import requests
from bs4 import BeautifulSoup

def two():
    html = requests.get("https://en.wikipedia.org/wiki/Deep_learning")
    bsObj = BeautifulSoup(html.content, "html.parser")
    print("Page Title =", bsObj.title.string)
    links = bsObj.findAll('a')
    print("links[103] =", links[103])
    outfile = open("DeepLearningLinks.txt", "w")
    href = []

    for i in bsObj.findAll('a'):
        href.append(i.get('href'))
        temp = str(i.get('href')) + "\n"
        outfile.write(temp)

    print("href[103] =", href[103])