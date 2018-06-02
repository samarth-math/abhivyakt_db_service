import requests
from lxml import html
from HTMLParser import HTMLParser
from pymongo import MongoClient

connection = MongoClient()
db = connection.literature
collection = db.doha


class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return '\n'.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()



page = requests.get("https://www.bharatdarshan.co.nz/magazine/literature/250/raheem.html").text
page = page.replace("<br />","\n")
tree = html.fromstring(page)

paras = tree.xpath("//p/span")[:-1]
for p in paras:
	if p.text and len(p.text.strip())>10:
		text = p.text.strip()
		collection.insert({"doha":text,"meaning":"","author":"Raheem"})
