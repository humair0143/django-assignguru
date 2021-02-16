import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
import random

df = pd.read_excel(r'C:\Users\hn_01\OneDrive\Desktop\django-assignguru\Quizlet_doc_num.xlsx')
arr1 = []
arr2 = []

for index, row in df.iterrows():
    arr1.append(row['doc_num'])
    arr2.append(row['desc'])



col1 = []
col2 = []
col3 = []
col4 = []
col5 = []

q = random.randint(40, 50)
count = 0

for x in range(len(arr1)):

    url = "https://quizlet.com/"+str(arr1[x])+'/'+str(arr2[x])+'/'
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0'}
    soup = BeautifulSoup(requests.get(url, headers=headers).content, 'html.parser')
    count += 1
    if count % q == 0:
        sleep(random.randint(10,30))
        title = soup.find('h1', class_='UIHeading UIHeading--one').get_text()
        print(count,"-",title)
        for i, (question, answer) in enumerate(zip(soup.select('a.SetPageTerm-wordText'), soup.select('a.SetPageTerm-definitionText')),1):
            col1.append(arr1[x])
            col2.append(i)
            col3.append(question.get_text(strip=True, separator='\n'))
            col4.append(answer.get_text(strip=True, separator='\n'))
            col5.append(title)
    else:
        title = soup.find('h1', class_='UIHeading UIHeading--one').get_text()
        print(count,"-",title)
        for i, (question, answer) in enumerate(zip(soup.select('a.SetPageTerm-wordText'), soup.select('a.SetPageTerm-definitionText')),1):
            col1.append(arr1[x])
            col2.append(i)
            col3.append(question.get_text(strip=True, separator='\n'))
            col4.append(answer.get_text(strip=True, separator='\n'))
            col5.append(title)

allcol =[col1, col2, col3, col4, col5]
df = pd.DataFrame(allcol).T
df.to_excel(excel_writer = r"C:\Users\hn_01\OneDrive\Desktop\django-assignguru\demo.xlsx")
