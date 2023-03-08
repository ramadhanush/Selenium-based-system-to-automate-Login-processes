from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import pyautogui
import random
import datetime
import os
import csv

global cout

cout=1


p = os.getcwd()
dri=p + "\Misc\chromedriver.exe"
alo=p+"\Misc\Allow.png"

opt=[p+'\Misc\A.png',p+'\Misc\B.png',p+'\Misc\C.png',p+'\Misc\D.png']

with open ("cred.txt",newline='') as csvfile:
    rows = csv.reader(csvfile, delimiter=',')
    data= []
    for row in rows:
        data.append(row)


data= data[0]


PATH=dri
driver=webdriver.Chrome(PATH)

driver.maximize_window()









def poll():
    global cout
    print("now searching for polls")
    
    while 6 != datetime.datetime.now().minute:
        
        x=random.choice(opt)
        
        if pyautogui.locateCenterOnScreen('C:\\Users\\dhanu\\Pictures\\qwerty\\Class\\img\\poll.png', confidence=0.6)!= None:
            f=pyautogui.locateCenterOnScreen(x ,confidence=0.7)
            pyautogui.click(f)
            time.sleep(5)
            
        elif pyautogui.locateCenterOnScreen('C:\\Users\\dhanu\\Pictures\\qwerty\\Class\\img\\yes.png' ,confidence=0.7)!= None:
            print("found Yes/No Poll")
            p=pyautogui.locateCenterOnScreen('C:\\Users\\dhanu\\Pictures\\qwerty\\Class\\img\\y.png' ,confidence=0.7)
            print("found" ,p )
            pyautogui.click(p)
            time.sleep(5)


        elif 6 == datetime.datetime.now().minute:
            cout=cout+1
            time.sleep(60)
            #return cout
            login()
            

        else:
            time.sleep(5)


    else:
        cout=cout+1
        time.sleep(60)
        #return cout
        login()


    


        

def frame1():
    global cout
    try:
        time.sleep(7)
        driver.switch_to.frame("frame")

    except:
        m=1
        while(m<=5):
            time.sleep(10)
            driver.refresh()
            frame1()

    else:
        #lis=driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/span/button[2]/span[1]/i")#mic mode
        #lis.click()

        #time.sleep(3)

        
            
        mic=driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/span/button[1]/span[1]")#mic mode
        mic.click()

        cout=cout+1

        time.sleep(5)

            
        a=pyautogui.locateCenterOnScreen(alo, confidence=0.7)
        pyautogui.click(a)

            

        time.sleep(9)

        print("allow found")
        
        yes=driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/span/button[1]/span[1]")# yes .success--Z6UU8x
        #yes=driver.find_element_by_css_selector(".success--Z6UU8x")
        yes.click()
        poll()

        #return cout





def frame2(): # no mic allow
    try:
        time.sleep(7)
        driver.switch_to.frame("frame")

    except:
        m=1
        while(m<=5):
            time.sleep(10)
            driver.refresh()
            frame2()

    else:
        #lis=driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/span/button[2]/span[1]/i")#mic mode
        #lis.click()

        #time.sleep(3)

        
            
        mic=driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/span/button[1]/span[1]")#mic mode
        mic.click()

        time.sleep(5)

            
        #a=pyautogui.locateCenterOnScreen(alo, confidence=0.7)
        #pyautogui.click(a)

            

        time.sleep(9)

        print("allow found")
        
        yes=driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/span/button[1]/span[1]")# yes .success--Z6UU8x
        #yes=driver.find_element_by_css_selector(".success--Z6UU8x")
        yes.click()
        poll()



#join button and frame function
def join():

    global cout

    
    time.sleep(2)

    jon=driver.find_element_by_css_selector(".btn:not(:disabled):not(.disabled)")# join 
    jon.click()


    if cout==1:
        frame1()

    elif cout!=1:
        frame2()

    

    
            



# login and schedule
def login():

    '''nw = time.localtime()
    mn = nw[4]
    re = 60-mn
    global sd
    sd = re*60
    print('min remaining', re)'''

    driver.get("https://myclass.lpu.in")

    user=driver.find_element_by_name("i")
    #if user == None : 
    user.send_keys(data[0])

    pswd=driver.find_element_by_name("p")
    #if pswd == None:
    pswd.send_keys(data[1])

    login=driver.find_element_by_css_selector(".ghost-round")#login complete
    login.click()

    time.sleep(1)

    view=driver.find_element_by_link_text("View Classes/Meetings")
    view.click()
    filter()



def filter():

    time.sleep(1)
    # filter clear
    close=driver.find_element_by_xpath("//div//ul/span[@title='Remove all items']")
    close.click()

    time.sleep(1)

    go=driver.find_element_by_css_selector(".select2-container--default .select2-results__option--highlighted[aria-selected]")
    go.click()


    aply=driver.find_element_by_id("filterApplyBtn")# filter ongoing apply
    aply.click()

    time.sleep(1)

    
    try:
        cls=driver.find_element_by_class_name("fc-title")
        cls.click()

    except:
        # if no ongoing class refresh
        k=1
        while(k<=65):
            time.sleep(60)
            ref=driver.find_element_by_xpath("//*[@id=\"calendar\"]/div[1]/div[1]/button[2]")
            filter()
            k+=1
        else:
            print("class delayed")
    else:
       join() 



login()

















