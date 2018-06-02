import requests
from lxml import html


def getData(url,index):
	url = url+"index"+index+".htm"
	print url

baseUrl = "hindinest.com/kavita/"

for i in xrange(0,8):
	if i!=0:
		getData(baseUrl,str(i))
	else:
		getData(baseUrl,"")
