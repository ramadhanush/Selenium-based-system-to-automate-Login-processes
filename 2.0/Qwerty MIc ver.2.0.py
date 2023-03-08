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

p=os.getcwd()
dri=p + "\Misc\chromedriver.exe"
alo=p+"\Misc\Allow.png"


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
    print("inside poll function")
    opt=['pollAnswerDescA','pollAnswerDescB','pollAnswerDescC','pollAnswerDescD']
    x=random.choice(opt)
    
    while 6 != datetime.datetime.now().minute:
        print("inside poll while statement")
        

        try :
            print("inside yes Try statement")
            driver.switch_to.frame("frame")
            y=driver.find_element_by_id("pollAnswerLabelYes")

            y.click()
            time.sleep(5)
            poll()
                
                
        except :
            try :
                print("inside A,B,C,D Try statement")

                driver.switch_to.frame("frame")

                p=driver.find_element_by_id("PollAnswerDescA")
                
                p.click()
                time.sleep(5)
                poll()
            
            
            except :
                print("except statement and wait ")
                time.sleep(5)
                poll()
            


    else:
        time.sleep(60)
        print("poll while else statement class over time is 6 minutes")
        login()
        


        

def frame():
    try:
        time.sleep(7)
        driver.switch_to.frame("frame")

    except:
        m=1
        while(m<=5):
            time.sleep(10)
            driver.refresh()
            frame()

    else:
        #lis=driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/span/button[2]/span[1]/i")#mic mode
        #lis.click()

        #time.sleep(3)

        mic=driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/div/span/button[1]/span[1]")#mic mode
        mic.click()

        time.sleep(3)

        a=pyautogui.locateCenterOnScreen(alo, confidence=0.5)
        pyautogui.click(a)

        time.sleep(9)

        yes=driver.find_element_by_xpath("/html/body/div[2]/div/div/div[1]/div/span/button[1]/span[1]")# yes
        yes.click()
        poll()


#join button and frame function
def join():
    time.sleep(2)

    jon=driver.find_element_by_css_selector(".btn:not(:disabled):not(.disabled)")# join 
    jon.click()
    frame()

    
            



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

















