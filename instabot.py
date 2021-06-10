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
def block_user_account(username,password):
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
    
    #load the chrome driver
    browser = webdriver.Chrome(executable_path="/home/devansh/chromedriver_linux64/chromedriver",
                               desired_capabilities=capabilities,chrome_options=options)
    
    #get instagram website
    browser.get('https://www.instagram.com')
    
    #wait till website is loaded
    WebDriverWait(browser, 10)
    
    #send username and password for logging in
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                 "input[name='username']"))).send_keys(username) 

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                 "input[name='password']"))).send_keys(password) 

    browser.find_element_by_xpath("//button[contains(.,'Log In')]").click()

    WebDriverWait(browser, 10)

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,
             "//button[contains(text(), 'Not Now')]"))).click()
    
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,
             "//button[@class='aOOlW   HoLwm ']"))).click()

    
    #to block a single just pass the account name 
    searchbox=browser.find_element_by_css_selector("input[placeholder='Search']")
    searchbox.clear()
    searchbox.send_keys("scoopwhoop") #single account that user wants to block
    time.sleep(5)
    searchbox.send_keys(Keys.ENTER)
    time.sleep(5)
    searchbox.send_keys(Keys.ENTER)
    
    #below code blocks single account
    time.sleep(2)
    element = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[aria-label='Options']")))
    element.click()
    
    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH,
             "//button[@class='aOOlW -Cab_   ']"))).click()

    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH,
             "//button[@class='aOOlW  bIiDR  ']"))).click()

    WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH,
             "//button[@class='aOOlW   HoLwm ']"))).click()

    browser.close()
    
#function to get followers information for user account on instagram
def get_followers_list(username,password):
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
                 "input[name='username']"))).send_keys(username) 

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                 "input[name='password']"))).send_keys(password)  

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

    #below code automatically scrolls and get the list of followers
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
    
    #store the follwers information in a txt file
    with open('followers.txt', 'a+') as f:
        for item in followers_list:
            f.write("%s\n" % item)

    browser.close()
    
#function to get following information for user account on instagram
def get_following_list(username,password):
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
                 "input[name='username']"))).send_keys(username)

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                 "input[name='password']"))).send_keys(password) 

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
    
    #below function get the information of people following automatically and stores them in a text file
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
    
    browser.close()
    
#function to get accounts which are blocked by user on instagram
def get_blocked_list(username,password):
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
                 "input[name='username']"))).send_keys(username) 

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                 "input[name='password']"))).send_keys(password) 

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
    #automatically get the list of accounts that are blocked by the user
    while True:
        try:
            time.sleep(5)
            button = browser.find_element_by_xpath("//*[@id='react-root']/section/main/div/article/main/button")
            browser.execute_script("arguments[0].click();", button)
        except Exception as e:
             print("Exception",e)
             time.sleep(5)
             html = browser.page_source
             soup = BeautifulSoup(html, "html.parser")
             account_names=soup.find_all("div",{"class":"-utLf"})
             account_list=[i.text for i in account_names]
             with open('blocked.txt', 'a+') as f:
                 for item in account_list:
                     f.write("%s\n" % item)      
    
             browser.close() 
             
#function to get all fan page account for the given list of celebrity and blue tick accounts
def similar_account(username,password):
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
    #options.add_argument('headless')
    #option.add_argument('user-agent'=user_agent)

    browser = webdriver.Chrome(executable_path="/home/devansh/chromedriver_linux64/chromedriver",
                               desired_capabilities=capabilities,chrome_options=options)
    
    browser.get('https://www.instagram.com')

    WebDriverWait(browser, 10)

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                 "input[name='username']"))).send_keys(username) 

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                 "input[name='password']"))).send_keys(password) 


    browser.find_element_by_xpath("//button[contains(.,'Log In')]").click()

    WebDriverWait(browser, 10)

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,
             "//button[contains(text(), 'Not Now')]"))).click()
        
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,
             "//button[@class='aOOlW   HoLwm ']"))).click()
    
    #get account names for whcih similar account needs to be fetched
    blocklist=open('accountnames.txt','r')
    blocklist= blocklist.readlines()
    blocklist=[i.strip("\n") for i in  blocklist]
    blocklist=blocklist[2611:]
    blockl=[]
    for acc_names in blocklist:
        if acc_names not in blockl:
            blockl.append(acc_names)
        else:
            pass
    
    #get similar account names for account names in accountnames.txt file
    for words in blockl:
        searchbox=browser.find_element_by_css_selector("input[placeholder='Search']")
        searchbox.clear()
        searchbox.send_keys(words)
        time.sleep(5)

        html = browser.page_source
        soup = BeautifulSoup(html, "html.parser")
      
        account_names=soup.find_all("div",{"class":"_7UhW9 xLCgt qyrsm KV-D4 uL8Hv"})
        account_list=[i.text for i in account_names]
  
        with open('similar.txt', 'a+') as f:
            for item in account_list:
                f.write("%s\n" % item)
             
    browser.close()

def block_multiple_account(username,password):
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
    #options.add_argument('headless')
    #option.add_argument('user-agent'=user_agent)

    browser = webdriver.Chrome(executable_path="/home/devansh/chromedriver_linux64/chromedriver",
                               desired_capabilities=capabilities,chrome_options=options)
    
    browser.get('https://www.instagram.com')

    WebDriverWait(browser, 10)

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                 "input[name='username']"))).send_keys(username) 

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                 "input[name='password']"))).send_keys(password) 


    browser.find_element_by_xpath("//button[contains(.,'Log In')]").click()

    WebDriverWait(browser, 10)

    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,
             "//button[contains(text(), 'Not Now')]"))).click()
        
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,
             "//button[@class='aOOlW   HoLwm ']"))).click()

    #get list of following
    following=open('following.txt','r')
    following=following.readlines()
    following=[i.strip("\n") for i in following]
 
    #get list of followers
    followers=open('followers.txt','r')
    followers=followers.readlines()
    followers=[i.strip("\n") for i in followers]

    #get common list
    common_list=list(set(following) | set(followers))

    #write common_list in common.txt file
    with open('common.txt', 'a+') as f:
        for item in common_list:
            f.write("%s\n" % item)

    #get common list of contacts
    f = open("/home/devansh/Desktop/Lakehead_spring_summer/instabot/common.txt", "r")
    data=f.readlines()
    data=[i.strip("\n") for i in data]
    
    #get list of accounts already blocked
    already_blocked = open("/home/devansh/Desktop/Lakehead_spring_summer/instabot/blocked.txt", "r")
    already_blocked=already_blocked.readlines()
    already_blocked=[i.strip("\n") for i in already_blocked]
    
    #get list of accounts to be blocked
    new_account = open("/home/devansh/Desktop/Lakehead_spring_summer/instabot/similar.txt", "r")
    new_account=new_account.readlines()
    new_account=[i.strip("\n") for i in new_account]
    
    blockl=[]
    for acc_name in new_account:
        if acc_name not in already_blocked:
            blockl.append(acc_name)
        else:
            pass
    
    #update the contents of the similar.txt file
    with open("similar.txt", 'w+') as f:
        for item in blockl:
            f.write("%s\n" % item)
    
    for blocking_acc in blockl:
        #blockerslist 
        blockerslist=[]
        try:
            searchbox=browser.find_element_by_css_selector("input[placeholder='Search']")
            searchbox.clear()
            searchbox.send_keys(blocking_acc)
            time.sleep(2)
            searchbox.send_keys(Keys.ENTER)
            time.sleep(2)
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
            elif name not in data or element!="Verified":
                try:
                    ablock=soup.find("button").text
                except Exception as e:
                    print("Exception 3",e)
                    ablock="NONE"
                if ablock=='Unblock':
                    print("account already blocked")
                else:
                    try:
                        print("Block the acccount")
                        time.sleep(2)
                        element = WebDriverWait(browser, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[aria-label='Options']")))
                        element.click()
                        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH,
                                     "//button[@class='aOOlW -Cab_   ']"))).click()
                        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH,
                                     "//button[@class='aOOlW  bIiDR  ']"))).click()
                        WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH,
                                     "//button[@class='aOOlW   HoLwm ']"))).click()
                        
                    except Exception as e:
                        print("Exception 4",e)
            else:
                print("try other accounts")
    
        except Exception as e:
            print("Exception 5",e)
        
        blockerslist.append(blocking_acc)
        with open('blockerslisst.txt', 'a+') as f:
            for item in blockerslist:
                f.write("%s\n" % item)
                    
    browser.close()      


#drop duplicates from the files
def remove_duplicates():
    file_list=["following.txt","followers.txt","accountnames.txt","similar.txt","common.txt","blocked.txt","blockerslisst.txt"]
    for i in file_list:
        acc_names_file=open(i,'r')
        acc_names_file=acc_names_file.readline()
        acc_names_file=[i.strip("\n") for i in  acc_names_file]
        print(acc_names_file)
        
        new=[]
        for value in acc_names_file:
            if value not in new:
                new.append(value)
            else:
                pass

        with open(i, 'w+') as f:
            for item in new:
                f.write("%s\n" % item)
    
        print("duplicates removed from the file")
        print("length of the file {} is {}".format(i,len(new)))
        
def remove_duplicates_large():
    file_list=["blockerslisst.txt"]
    for i in file_list:
        files=open(i,'r')
        new=[]
        for j in files:
            data=files.readline().strip("\n")
            if data not in new:
                new.append(data)
        #update files
        with open(i, 'w+') as f:
            for item in new:
                f.write("%s\n" % item)

        print("duplicates removed from the file")
        print("length of the file {} is {}".format(i,len(new))) 


def hashtaglist():
    file_list=["similar.txt","blocked.txt","blockerslisst.txt"]
    for i in file_list:
        files=open(i,'r')
        new=[]
        updated_new=[]
        for j in files:
            data=files.readline().strip("\n")
            if data.startswith("#")==True:
                if data not in new:
                    new.append(data)
            else:
                updated_new.append(data)
        
        #update files
        with open(i, 'w+') as f:
            for item in updated_new:
                f.write("%s\n" % item)

        #write in hashtag file
        with open("hashtag.txt", 'a+') as f:
            for item in new:
                f.write("%s\n" % item)

        print("hashtags removed from the file")
        print("length of the file {} is {}".format(i,len(new)))      
                
def main(username,password):
    #block_user_account("devansh_mody","Deva1234")
    #run this function to get the follwing list
    #get_following_list("devansh_mody","Deva1234")
    #run this function to get the follwers list
    #get_followers_list("devansh_mody","Deva1234")
    #function to get the blocked list
    #get_blocked_list("devansh_mody","Deva1234")
    #function to get similar account given a account name
    #similar_account(username,password) 
    #function to block mutiple accounts
    block_multiple_account(username,password) 
    #function to remove duplicate from the files
    #remove_duplicates()
    #remove_duplicates_large()
    #generate hashtag file
    #hashtaglist()
    
main("enter username here","enter password here")

         
               
