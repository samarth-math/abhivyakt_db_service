import requests
from lxml import html
from pymongo import MongoClient

connection = MOngoClient()
db = connection.kahani

def authorLinks(mainLink):
	page = requests.get(mainLink).text
	tree = html.fromstring(page)
	authorLinks = tree.xpath("//li/a/@href")[5:-10]
	return ["http://gadyakosh.org"+link for link in authorLinks]

def getstoriesLink(link):
	page = requests.get(link).text
	tree = html.fromstring(page)
	#links = tree.xpath("//li/a")[5:-16]
	links = tree.xpath('//div[@id="mw-content-text"]/ul/li/a/@href')
	return ["http://gadyakosh.org"+link for link in links]

def getStories(link):
	try:
		page = requests.get(link).text
        	tree = html.fromstring(page)
		author = tree.xpath('//span[@id="gkrachna-poet"]/a')[0].text.strip()
		#print author
		#print "---------------"
		title = tree.xpath('//title')[0].text.split('/')[0].strip()
		#print title
		#print "---------------"
		paras = [elem.text.strip() for elem in tree.xpath('//div[@id="mw-content-text"]/p')]
		text = "\n\n\n".join(paras)
		#print text
		#print "=============================="
		return title,author,text
	except:
		#print link
		#print "Error"
		#print "============================="
		return None

links = authorLinks("http://gadyakosh.org/")
for link in links:
	storyLinks = getstoriesLink(link)
	for link in storyLinks:
		title,author,text = getStories(link)
		entry = {"title": title,"kahaniText": text,"author":  author}
	#raw_input("next?")
