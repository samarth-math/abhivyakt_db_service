import helperfunctions as H
from bs4 import BeautifulSoup

status = collection = H.initializeDB('literature', 'muhavare')
if status is None:
    exit(1)

def parseHindiStudentMuhavare():
    soup = BeautifulSoup(open("/home/rishabh/Projects/hindived/index.html"), "lxml")
    td = soup.find_all('td')
    count = 0
    content = meaning = sentence = ""
    for t in td:
        if count == 0:
            count += 1
            continue
        elif count == 1:
            content = t.getText()
        elif count == 2:
            meaning = t.getText()
        elif count == 3:
            sentence = t.getText()
        count = (count + 1) % 4
        if count == 0:
            print("content: ", content, " meaning: ",
                  meaning, " sentence: ", sentence)
            entry = {
                'muhavara': content,
                'meaning': meaning,
                'usage': sentence,
                'source': 'http://hindistudent.com/hindi-vyakaran/hindi-muhavare/hindi-muhavare-aur-arth/'
            }
            status = H.saveToMongoDB(collection, entry)
            print("status:", status)
            if status is False:
                exit(1)


try:
    parseHindiStudentMuhavare()
finally:
    print("completed")
