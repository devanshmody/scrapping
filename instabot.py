from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import time,datetime,os,random
import pandas as pd
from googlesearch import search 
from selenium.webdriver.common.proxy import Proxy,ProxyType
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from flask import Flask, request, jsonify
from flask_cors import CORS

#function to block user account on instagram
def block_user_account():
    #spoofing the ipaddress
    ip = '{}.{}.{}.{}'.format(*__import__('random').sample(range(0,255),4))
    p = '{}'.format(*__import__('random').sample(range(1000,8000),1))
    ip=ip+':'+p
    print("spooffed ip addres is {}".format(ip))

    # Configure Proxy Option
    prox = Proxy()
    prox.proxy_type = ProxyType.MANUAL
    
    # Proxy IP & Port
    prox.http_proxy = ip
    #prox.socks_proxy = ip
    #prox.ssl_proxy = ip
    prox.https_proxy = ip
    
    # Configure capabilities 
    capabilities = webdriver.DesiredCapabilities.CHROME
    prox.add_to_capabilities(capabilities)
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")
    #option.add_argument('headless')
    #option.add_argument('user-agent'=user_agent)

    browser = webdriver.Chrome(executable_path="/home/devansh/chromedriver_linux64/chromedriver",
                               desired_capabilities=capabilities,chrome_options=options)
    
    browser.get('https://www.instagram.com')

    WebDriverWait(browser, 10)

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                 "input[name='username']"))).send_keys("devansh_mody") #enter user name here

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                 "input[name='password']"))).send_keys("Fgexd123") #enter password here 


    browser.find_element_by_xpath("//button[contains(.,'Log In')]").click()

    WebDriverWait(browser, 10)

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,
             "//button[contains(text(), 'Not Now')]"))).click()
    
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,
             "//button[@class='aOOlW   HoLwm ']"))).click()


    searchbox=browser.find_element_by_css_selector("input[placeholder='Search']")
    searchbox.clear()
    searchbox.send_keys("scoopwhoop")
    time.sleep(5)
    searchbox.send_keys(Keys.ENTER)
    time.sleep(5)
    searchbox.send_keys(Keys.ENTER)
    
    soup=BeautifulSoup(browser.page_source, 'lxml')
    v=soup.find('span',{'title':'Verified'})
    print(v)
    '''
    #attribute_value = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "span"))).get_attribute("title")
    #print("attribute values is",attribute_value)
    '''
    time.sleep(2)
    element = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[aria-label='Options']")))
    element.click()
    #WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH,
    #             "//*[@id='react-root']/section/main/div/header/section/div[1]/div[3]/button/div/svg"))).click()
    
    #WebDriverWait(browser,1).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[aria-label='Options']"))).click(
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH,
             "//button[@class='aOOlW -Cab_   ']"))).click()

    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH,
             "//button[@class='aOOlW  bIiDR  ']"))).click()

    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH,
             "//button[@class='aOOlW   HoLwm ']"))).click()

block_user_account()


