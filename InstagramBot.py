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
    follow_random(driver,random_follow_choice,follow_random_target_account)
    
    #Message
    message(driver,MESSAGE_CHOICE,GROUP_CHAT_CHOICE,MESSAGE_USER_TARGET,MY_MESSAGE)
    #logout(driver)
    #open_new_tab(driver)
    #previous_tab(driver)
    #close_tab(driver)
    #close_tab(driver)
    #close_window(driver)
    
except:
    print("Some error occured.")

#TODO: To find people you are following but do not follow you back.

#driver.quit()
print("Driver quit.")
exit()
