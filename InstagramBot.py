from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Credentials import MYUSERNAME,MYPASSWORD
from OtherDetails import *
from myFunctionsAshwin import *
import time
import pyautogui

#Variables and constants
LOGIN_LINK = "http://instagram.com/accounts/login"
WEBSITE_LINK = "http://instagram.com/"
CHROME_DRIVER_PATH = "C:\Program Files (x86)\chromedriver.exe"
n = NUMBER_OF_POSTS

post_available = False

driver = webdriver.Chrome(CHROME_DRIVER_PATH)
driver.get(WEBSITE_LINK)



#MAIN PROGRAM STARTS HERE
try:
    #Login
    login(driver,MYUSERNAME,MYPASSWORD)

    #Save login info
    SaveInfoPopUpAppears = SaveInfo(driver,SAVE_CHOICE)

    #Turn notifications off.
    NotifyPopUpAppears = TurnOnNotificationPopUp(driver,NOTIFY_CHOICE)

    if(not SaveInfoPopUpAppears):
        print('Entered save info again1.')
        SaveInfo(driver,SAVE_CHOICE)
        print('Entered save info again2.')

    #Like n post from a target account
    Like_Post(driver,LIKE_POST_CHOICE,TARGET_ACCOUNT_USERNAME,n)
    
    #Follow People from the input list.
    follow(driver,FOLLOW_CHOICE,WEBSITE_LINK,FOLLOWING_ACCOUNT_USERNAME_LIST)
    
    
except:
    print("Some error occured.")

#driver.close()
#driver.quit()
exit()
