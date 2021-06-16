import requests
from bs4 import BeautifulSoup
import texttable
import matplotlib.pyplot as plt
import numpy as np
url='https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'
result=requests.get(url)
soup=BeautifulSoup(result.text,'html.parser')
data=[]
dt_iter=iter(soup.find_all('td'))
while True:
    try:
        country=next(dt_iter).text
        confirmed=next(dt_iter).text
        deaths=next(dt_iter).text
        continent=next(dt_iter).text
        #For 'confirmed' and 'deaths'
        # make sure to remove commas and convert the values to int
        data.append((
            country,
            int(confirmed.replace(',','')),
            int(deaths.replace(',','')),
            continent
        ))
    except StopIteration:
        break
data.sort(key=lambda row:row[1], reverse=True)
tableObject=texttable.Texttable()
tableObject.add_rows([(None,None,None,None)]+data)
tableObject.set_cols_align(('c','c','c','c'))
tableObject.header(('Country','Number of cases','Deaths','Continent'))
print(tableObject.draw())
