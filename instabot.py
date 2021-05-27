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
    
    #give youre chrome driver path here
    browser = webdriver.Chrome(executable_path="/home/devansh/chromedriver_linux64/chromedriver",
                               desired_capabilities=capabilities,chrome_options=options)
    
    #website here in this case its instagram
    browser.get('https://www.instagram.com')

    WebDriverWait(browser, 10)

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                 "input[name='username']"))).send_keys("enter youre user name") #enter user name here

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                 "input[name='password']"))).send_keys("enter youre password") #enter password here 


    browser.find_element_by_xpath("//button[contains(.,'Log In')]").click()

    WebDriverWait(browser, 10)

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,
             "//button[contains(text(), 'Not Now')]"))).click()
    
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,
             "//button[@class='aOOlW   HoLwm ']"))).click()


    searchbox=browser.find_element_by_css_selector("input[placeholder='Search']")
    searchbox.clear()
    #enter the account to be blocked
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

#########UPDATED CODE###########

from selenium import webdriver
from explicit import waiter, XPATH
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options 
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import time,datetime,os,random,itertools,requests,string
import pandas as pd
from googlesearch import search 
from selenium.webdriver.common.proxy import Proxy,ProxyType
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from flask import Flask, request, jsonify
from flask_cors import CORS

#function to block a single user account on instagram
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
                 "input[name='username']"))).send_keys("enter user name here") #enter user name here

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                 "input[name='password']"))).send_keys("enter password here") #enter password here 


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
    
    time.sleep(2)
    element = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[aria-label='Options']")))
    element.click()
    
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH,
             "//button[@class='aOOlW -Cab_   ']"))).click()

    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH,
             "//button[@class='aOOlW  bIiDR  ']"))).click()

    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH,
             "//button[@class='aOOlW   HoLwm ']"))).click()


#function to get followers information for user account on instagram
def get_followers_list():
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
    prox.https_proxy = ip
    # Configure capabilities 
    capabilities = webdriver.DesiredCapabilities.CHROME
    prox.add_to_capabilities(capabilities)
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")

    browser = webdriver.Chrome(executable_path="/home/devansh/chromedriver_linux64/chromedriver",
                               desired_capabilities=capabilities,chrome_options=options)
    browser.get('https://www.instagram.com')

    WebDriverWait(browser, 10)

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                 "input[name='username']"))).send_keys("enter user name here") #enter user name here

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                 "input[name='password']"))).send_keys("enter password here") #enter password here 

    browser.find_element_by_xpath("//button[contains(.,'Log In')]").click()

    WebDriverWait(browser, 10)
    
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,
            "//button[contains(text(), 'Not Now')]"))).click()
    
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,
             "//button[@class='aOOlW   HoLwm ']"))).click()

    #to go to my profile page
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,
             "//div[@class='_7UhW9   xLCgt      MMzan  KV-D4              fDxYl     ']"))).click()

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,
             "//a[@class='-nal3 ']"))).click()

    # Wait for the followers modal to load
    waiter.find_element(browser, "//div[@role='dialog']", by=XPATH)
    allfoll = int(browser.find_element_by_xpath("//li[2]/a/span").text)

    followers_list=[]
    follower_css = "ul div li:nth-child({}) a.notranslate"  # Taking advange of CSS's nth-child functionality
    try:
        for group in itertools.count(start=1, step=12):
            for follower_index in range(group, group + 12):
                if follower_index > allfoll:
                    break 
                print(waiter.find_element(browser, follower_css.format(follower_index)).text)
                followers_list.append(waiter.find_element(browser, follower_css.format(follower_index)).text)

            last_follower = waiter.find_element(browser, follower_css.format(group+11))
            browser.execute_script("arguments[0].scrollIntoView();", last_follower)
    except TimeoutException as ex:
          print("Exception has been thrown. " + str(ex))
        
    with open('followerslist.txt', 'a+') as f:
        for item in followers_list:
            f.write("%s\n" % item)
       
#function to get following information for user account on instagram
def get_following_list():
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
    prox.https_proxy = ip
    # Configure capabilities 
    capabilities = webdriver.DesiredCapabilities.CHROME
    prox.add_to_capabilities(capabilities)
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")

    browser = webdriver.Chrome(executable_path="/home/devansh/chromedriver_linux64/chromedriver",
                               desired_capabilities=capabilities,chrome_options=options)
    browser.get('https://www.instagram.com')

    WebDriverWait(browser, 10)

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                 "input[name='username']"))).send_keys("enter user name here") #enter user name here

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                 "input[name='password']"))).send_keys("enter password here ") #enter password here 

    browser.find_element_by_xpath("//button[contains(.,'Log In')]").click()

    WebDriverWait(browser, 10)
    
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,
            "//button[contains(text(), 'Not Now')]"))).click()
    
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,
             "//button[@class='aOOlW   HoLwm ']"))).click()

    #to go to my profile page
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,
                 "//div[@class='_7UhW9   xLCgt      MMzan  KV-D4              fDxYl     ']"))).click()
    
    
    browser.get("https://www.instagram.com/devansh_mody/following/")
  
    browser.find_element_by_partial_link_text("following").click()
  
    allfoll = int(browser.find_element_by_xpath("//li[3]/a/span").text)

    following_list=[]
    follower_css = "ul div li:nth-child({}) a.notranslate"  # Taking advange of CSS's nth-child functionality
    try:
        for group in itertools.count(start=1, step=12):
            for follower_index in range(group, group + 12):
                if follower_index > allfoll:
                    break 
                print(waiter.find_element(browser, follower_css.format(follower_index)).text)
                following_list.append(waiter.find_element(browser, follower_css.format(follower_index)).text)

            last_follower = waiter.find_element(browser, follower_css.format(group+11))
            browser.execute_script("arguments[0].scrollIntoView();", last_follower)
    except TimeoutException as ex:
          print("Exception has been thrown. " + str(ex))
        
    with open('following.txt', 'a+') as f:
        for item in following_list:
            f.write("%s\n" % item)

#function to get accounts which are blocked information for user account on instagram
def get_blocked_list():
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
    prox.https_proxy = ip
    # Configure capabilities 
    capabilities = webdriver.DesiredCapabilities.CHROME
    prox.add_to_capabilities(capabilities)
    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_argument("disable-infobars")
    options.add_argument("--disable-extensions")

    browser = webdriver.Chrome(executable_path="/home/devansh/chromedriver_linux64/chromedriver",
                               desired_capabilities=capabilities,chrome_options=options)
    browser.get('https://www.instagram.com')

    WebDriverWait(browser, 10)

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                 "input[name='username']"))).send_keys("enter user name here") #enter user name here

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                 "input[name='password']"))).send_keys("enter password here ") #enter password here 

    browser.find_element_by_xpath("//button[contains(.,'Log In')]").click()

    WebDriverWait(browser, 10)
    
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,
            "//button[contains(text(), 'Not Now')]"))).click()
    
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,
             "//button[@class='aOOlW   HoLwm ']"))).click()

    #to go to my profile page
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,
                 "//div[@class='_7UhW9   xLCgt      MMzan  KV-D4              fDxYl     ']"))).click()
    
    browser.get("https://www.instagram.com/accounts/access_tool/accounts_you_blocked")
  
    #browser.find_element_by_partial_link_text("following").click()
  
    allfoll = int(browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/main/section").text)

    following_list=[]
    follower_css = "ul div li:nth-child({}) a.notranslate"  # Taking advange of CSS's nth-child functionality
    try:
        for group in itertools.count(start=1, step=12):
            for follower_index in range(group, group + 12):
                if follower_index > allfoll:
                    break 
                print(waiter.find_element(browser, follower_css.format(follower_index)).text)
                following_list.append(waiter.find_element(browser, follower_css.format(follower_index)).text)

            last_follower = waiter.find_element(browser, follower_css.format(group+11))
            browser.execute_script("arguments[0].scrollIntoView();", last_follower)
    except TimeoutException as ex:
          print("Exception has been thrown. " + str(ex))
        
    with open('blocked.txt', 'a+') as f:
        for item in following_list:
            f.write("%s\n" % item)
            

def block_multiple_account():
    for k in range(0,5):
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
        
        #blockerslist 
        blockerslist=[]
        # Configure capabilities 
        capabilities = webdriver.DesiredCapabilities.CHROME
        prox.add_to_capabilities(capabilities)
        options = webdriver.ChromeOptions()
        options.add_argument("start-maximized")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")
        #options.add_argument('headless')
        #option.add_argument('user-agent'=user_agent)
    
        browser = webdriver.Chrome(executable_path="/home/devansh/chromedriver_linux64/chromedriver",
                               desired_capabilities=capabilities,chrome_options=options)
    
        browser.get('https://www.instagram.com')

        WebDriverWait(browser, 10)

        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                 "input[name='username']"))).send_keys("enter user name here") #enter user name here

        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                 "input[name='password']"))).send_keys("enter password here ") #enter password here 


        browser.find_element_by_xpath("//button[contains(.,'Log In')]").click()

        WebDriverWait(browser, 10)

        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,
             "//button[contains(text(), 'Not Now')]"))).click()
        
        WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,
             "//button[@class='aOOlW   HoLwm ']"))).click()

        #get my followingl ist
        f = open("/home/devansh/Desktop/Lakehead_spring_summer/instabot/commonlist.txt", "r")
        data=f.readlines()
        data=[i.strip("\n") for i in data]
    
        blocklist = open("/home/devansh/Desktop/Lakehead_spring_summer/instabot/block", "r")
        blockl=blocklist.readlines()
        blockl=[i.strip("\n") for i in blockl]
    
        #for i in string.printable:
        #    for j in blockl:
        for i in range(0,5):
            for j in range(0,5):
                try:
                    searchbox=browser.find_element_by_css_selector("input[placeholder='Search']")
                    searchbox.clear()
                    searchbox.send_keys("thug")
                    time.sleep(5)
                    searchbox.send_keys(Keys.ENTER)
                    time.sleep(5)
                    searchbox.send_keys(Keys.ENTER)
                    #check if searched account is same as searched name and is its verified or not
                    html = browser.page_source
                    soup = BeautifulSoup(html, "html.parser")
                    try:
                        element=soup.find("span",{'aria-label':'Verified'})
                        element=element.attrs['aria-label']
                        print("Account type",element)
                    except Exception as e:
                        print("Exception 1",e)
                        element="NONE"
                
                    #name=soup.find("input",{"value":"{}".format("kendalljenner")})
                    #name=name.attrs["value"]
                    try: 
                        name=soup.find("div",{"class":"_7UhW9 xLCgt qyrsm KV-D4 uL8Hv"})
                        name=name.text
                        print("Account name",name)
                    except Exception as e:
                        print("Exception 2",e)
                        name="NONE"
        
                    if name in data or element=="Verified":   
                        print("dont block the accounts") 
                        pass
                    else:
                        print("Block the acccount")
                        try:
                            time.sleep(5)
                            element = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[aria-label='Options']")))
                            element.click()
                            WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH,
                                     "//button[@class='aOOlW -Cab_   ']"))).click()
                            WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH,
                                     "//button[@class='aOOlW  bIiDR  ']"))).click()
                            WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH,
                                     "//button[@class='aOOlW   HoLwm ']"))).click()
                        except Exception as e:
                            print("Exception 3",e)
                    
                    blockerslist.append(name)
                    with open('blockerslisst.txt', 'a+') as f:
                        for item in blockerslist:
                            f.write("%s\n" % item)
                
                except Exception as e:
                    print("Exception 4",e)
                    
        browser.close()      
        
def main():
    block_user_account()
    get_followers_list()
    get_following_list()
    #get_blocked_list()
    block_multiple_account()      
    
main()


