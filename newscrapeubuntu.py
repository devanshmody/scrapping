from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.chrome.options import Options 
from bs4 import BeautifulSoup
import regex as re
import time,datetime,os,shutil,random
import pandas as pd 
from googlesearch import search 
from selenium.webdriver.common.proxy import Proxy,ProxyType
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

chrome_options = webdriver.ChromeOptions()
#this function is used to get the research document
def cybernews():
    
    #generate proxy ip address
    ip = '{}.{}.{}.{}'.format(*__import__('random').sample(range(0,255),4))
    p = '{}'.format(*__import__('random').sample(range(1000,8000),1))
    ip=ip+':'+p
    # Configure Proxy Option
    prox = Proxy()
    prox.proxy_type = ProxyType.MANUAL
    # Proxy IP & Port
    prox.http_proxy = ip
    prox.https_proxy = ip
    # Configure capabilities 
    capabilities = webdriver.DesiredCapabilities.CHROME
    prox.add_to_capabilities(capabilities)
    option = webdriver.ChromeOptions()
    #option.add_argument('headless')
    #load the chrome driver
    driver = webdriver.Chrome("/home/devansh/Desktop/cyberscrape/chromedriver_linux64/chromedriver",desired_capabilities=capabilities,chrome_options=option)
    driver.implicitly_wait(60)
    WebDriverWait(driver, 100)
    
    #scrapping the website the threatpost.com
    driver.get("https://threatpost.com/")
    driver.implicitly_wait(60)
    WebDriverWait(driver, 100)
    soup=BeautifulSoup(driver.page_source, 'lxml')
    links= []
    names = []
    news= []
    new_name = []
    for link in soup.find_all('a'):
        if len(re.sub('\s+',' ',link.text))==0:
            pass
        if re.sub('\s+',' ',link.text).find("listen now")==-1:            
            links.append(link.get('href'))
            names.append(re.sub('\s+',' ',link.text))
        else:
            pass
            #print(links[:5])

    for i in range(0,len(links)):
        if links[i].startswith('https://threatpost.com/microsoft') or links[i].startswith('https://threatpost.com/author/') or links[i].startswith("https://threatpost.com/teamtntstartswith(") or links[i].startswith('https://threatpost.com/spoofing-bug-cybersecurity') or links[i].startswith('https://threatpost.com/ragnar-locker-gang') or links[i].startswith('https://threatpost.com/solarwinds') or links[i].startswith('https://threatpost.com/iot-attacks-doubling') or links[i].startswith("https://threatpost.com/attackers") or links[i].startswith("https://threatpost.com/ransomware"):
            if links[i].find("author") ==-1:
                news.append(links[i])
                new_name.append(names[i])
            else:
                pass
    
    df=pd.DataFrame(columns=["url"])
    for j in range(0,len(news)):
        df=df.append({'url':"<a href={}".format(news[j])+">"+new_name[j]+"</a>"},ignore_index=True)
    
    #scrapping from cybersecurity google news
    driver.get("https://news.google.com/search?hl=en-IN&gl=IN&q=cyber+security&ceid=IN:en&gl=IN&q=cyber+security")
    driver.implicitly_wait(60)
    WebDriverWait(driver, 100)
    soup=BeautifulSoup(driver.page_source, 'lxml')
    for link in soup.find_all('a'):
        try:
            if link.get('href').startswith("./articles/"):
                df=df.append({'url':"<a href=https://news.google.com/"+link.get('href')[2:]+">"+re.sub('\s+',' ',link.text)+"</a>"},ignore_index=True)
        except Exception as e:
            print(e)
      
    #scrapping from cyware.coms
    driver.get("https://cyware.com/cyber-security-news-articles/")
    driver.implicitly_wait(60)
    WebDriverWait(driver, 100)
    links= []
    names = []
    news= []
    new_name = []
    soup=BeautifulSoup(driver.page_source, 'lxml')
    for link in soup.find_all('a'):
        if len(re.sub('\s+',' ',link.text))==0:
            pass
        else:
            links.append(link.get('href'))
            names.append(re.sub('\s+',' ',link.text))
            #print(links[:5])
    
    for i in range(0,len(links)):
        if str(links[i]).startswith('https:'):
            if str(links[i]).find("https://cyware.com/legal/")==-1:
                news.append(links[i])
                new_name.append(names[i])
            else:
                pass
    
    for j in range(0,len(news)):
        df=df.append({'url':"<a href={}".format(news[j])+">"+new_name[j]+"</a>"},ignore_index=True)


    df.drop_duplicates(subset=['url'],inplace=True)        
    df.to_excel("cybernews.xlsx",index=False)       
    
    driver.close()
    
cybernews()
