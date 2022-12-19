import re 
import requests
from PyPDF2 import PdfFileReader
import os
def put():
    z=[]
    for root, dirs, files in os.walk("."):
        for filename in files:
            a = re.fullmatch(r".+.pdf",filename) 
            if a != None:
                z.append(filename)
    return z[-1]
path=put()
#считает страницы
def countpages(path):
    count=0
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        for q in range(1,1000):
            try:
                a=pdf.getPage(q)
                count=count+1
            except IndexError:
                break
    return count
#достает текст из пдф
def text_extractor(path,stra):
    with open(path, 'rb') as f:
        pdf = PdfFileReader(f)
        page = pdf.getPage(stra)
        text = page.extractText()
        return text
# регулярка на проверку сылка ли это
def isurl (url): 
    a = re.fullmatch(r"https?\://.+",url)
    return 'yes' if a else 'no'
# выводит сылки
def geturl (path):
    allurl=[]
    for z in range(1,countpages(path)):
        split=text_extractor(path,z).split( )
        for i in split:
            if isurl (i) == 'yes' :
                allurl.append(i)
    return(allurl)
# реквесты
def reque():
    urllall=geturl (path)
    works=True
    for urll in urllall:
        try: 
            response = requests.get(urll)
            if response.status_code == 200:
                    works=True
                    continue
        except:
            works = False
            break
    return(works)
print(reque()) 


