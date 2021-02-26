import pyautogui,time
from selenium.webdriver.common.keys import Keys
from OtherDetails import my_sleep_time 

def login(driver,MYUSERNAME,MYPASSWORD):
    driver.implicitly_wait(10)
    pyautogui.hotkey('win', 'up')

    username= driver.find_element_by_name('username')
    username.clear()
    username.click()
    
    for i in MYUSERNAME:
       pyautogui.press(i)
    
    password = driver.find_element_by_name('password')
    password.clear()
    password.click()
    for i in MYPASSWORD:
        pyautogui.press(i)
    
    driver.find_element_by_css_selector('button[type=submit]').click()

def SaveInfo(driver,choice):
    time.sleep(my_sleep_time)
    try:
        driver.implicitly_wait(10)
        if(choice):
            driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/section/div/button').click()
            print("Saved login details.")
        else:
            driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
            print("Did not save login details.")
        return True
    except:
        print("Login details save did not pop up.")
        return False

def TurnOnNotificationPopUp(driver,choice):
    time.sleep(my_sleep_time)
    try:
        driver.implicitly_wait(10)
        if(choice):
            driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[1]').click()
            print("Turned on notifications")
        else:
            driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
            print("Turn on notification dismissed for now.")
        return True
    except:
        print("Turn on notifications did not pop up.")
        return False
    
def type(driver,word):
    time.sleep(my_sleep_time)
    driver.implicitly_wait(10)
    for i in word:
        pyautogui.press(i)
    print("Typing...")
    
def search_bar(driver,myInput):
    #Clicking the search bar
    search_bar = driver.find_element_by_xpath("//*[name()='span'][@class='TqC_a']")
    print("Bar found")
    search_bar.click()
    print("Bar clicked")
    
    #Typing in the search bar
    type(driver,myInput)
    
    #Clicking the first account
    account = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div")
    print("Account found")
    
    
    account.click()
    print("Account clicked")
    
    
    
def Like_Post(driver,choice,TARGET_ACCOUNT_USERNAME,n):
    if(choice and n>0):
        #Go to the required account.
        hash = '#'
        hash_tag = True
        
        if(TARGET_ACCOUNT_USERNAME.find(hash) == -1):
            hash_tag = False
        
            
        
        
        search_bar(driver,TARGET_ACCOUNT_USERNAME)

        driver.implicitly_wait(6)
        number_of_posts = driver.find_element_by_class_name('g47SY ')
        print("number of posts =",number_of_posts.text)

        try:
            number_of_posts = int(number_of_posts.text)
            if(number_of_posts > 0):
                post_available = True
        except:
            number_of_posts = n
            print("Unable to convert no. of post from text to integer.")

        
        if(number_of_posts != 0):
            
            #Click on the first post.
            driver.implicitly_wait(3)
            try:
                if(not hash_tag):
                    driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]').click()
                else:
                    print("trying to click the hash tag first post.")
                    driver.find_element_by_xpath("//*[name()='div'][@class='eLAPa']").click()
                print('First post clicked 1')
                post_available = True
            except:
                try:
                    driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]').click()
                    print('First post clicked 2')
                    post_available = True
                    
                except:
                    print("No posts available1.")
                    post_available = False
            
            #Like if the first post is available.
            if(post_available == True):
                i=0
                

                #Loop until the required number of post are liked.
                while(i<n):
                    driver.implicitly_wait(10)
                    try:
                        time.sleep(3)
                        
                        #Find if the post is liked already by searching for like button.
                        try:
                            ul = driver.find_element_by_xpath("//*[name()='svg'][@aria-label='Unlike']")
                            print('Unlike button found so post liked already.')
                        except:
                            l = driver.find_element_by_xpath("//*[name()='svg'][@aria-label='Like']")
                            l.click()
                            print("Like button clicked.")
                    except:
                        print("Like button not found.")

                    #Move to next post
                    if(i==0):
                        driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a").click()
                    else:
                        #Different xpath from second post on because the is a forward and back arraw to move between post arises.
                        driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a[2]").click()
                                                
                    i+=1
                close_button(driver)
            
            
        else:
            print('No post available in the account.')
            
def follow(driver,choice,WEBSITE_LINK,FOLLOWING_ACCOUNT_USERNAME_LIST):
    if(choice):
        for FOLLOWING_ACCOUNT_USERNAME in FOLLOWING_ACCOUNT_USERNAME_LIST:
            print("Going to following link")
            #driver.get(WEBSITE_LINK+FOLLOWING_ACCOUNT_USERNAME)
            search_bar(driver,FOLLOWING_ACCOUNT_USERNAME)
            
            
            driver.implicitly_wait(5)
            print("waiting")
            
            
            try:
                follow_buton = driver.find_element_by_xpath("//*[name()='button'][@class='_5f5mN       jIbKX  _6VtSN     yZn4P   ']")
                print('button found')
                time.sleep(my_sleep_time)
                follow_buton.click()
                print("Follow button clicked.")
            except:
                try:
                    following_buton = driver.find_element_by_xpath("//*[name()='span'][@aria-label='Following']")
                    print("Already following")
                except:
                    print("Error occured trying to follow the account.")
  
def new_message(driver):
    driver.implicitly_wait(10)
    try:
        Send_message_button = driver.find_element_by_xpath("//*[name()='svg'][@aria-label='New Message']")
        print("New message button found.")
    except:
        try:
            Send_message_button = driver.find_element_by_xpath("//*[name()='button'][@class='sqdOP  L3NKy   y3zKF     ']")
            print("Send message button 2 found.")
        except:
            print("Send message button not found.")
    
    
    driver.implicitly_wait(10)
    Send_message_button.click()
    print("New message button clicked.")
    
    
    #Clearing and selecting query box.
    driver.implicitly_wait(10)
    queryBox = driver.find_element_by_name('queryBox')
    print('query box found.')
    queryBox.click()
    print('query box clicked.')
    queryBox.clear()
    print('query box cleared.')
    
def next(driver):
    driver.implicitly_wait(10)
    Next = driver.find_element_by_xpath("//*[name()='button'][@class='sqdOP yWX7d    y3zKF   cB_4K  ']")
    Next.click()
    
def send_message(driver,message):
    time.sleep(my_sleep_time)
    driver.implicitly_wait(10)
    message_textarea = driver.find_element_by_tag_name('textarea')
    
    #message_textarea = driver.find_element_by_xpath('//*input[@placeholder="Message..." and not(@disabled)]')
    print("message area found")
    message_textarea.click()
    print("message area clicked")
    message_textarea.clear()
    print("message area ready.")
    
    type(driver,message)
    
    pyautogui.press('enter')
    
def close_button(driver):
    time.sleep(my_sleep_time)
    driver.implicitly_wait(10)
    try:
        close = driver.find_element_by_xpath("//*[name()='svg'][@aria-label='Close']")
    except:
        print("close button not found.")

    print("Close button found.")
    close.click()
    print("Closed.")
    
    
                        
def message(driver,choice,group_chat,user_list,message):
    if(choice):
        
        #Click the message tab button
        driver.implicitly_wait(10)
        try:
            messenger_button = driver.find_element_by_xpath("//*[name()='svg'][@aria-label='Direct']")
            print("Messenger svg found")
        except:
            print("Messenger svg not found")
        
        messenger_button.click()
        print('Messenger svg clicked.')
        
        #Click new message button
        new_message(driver)
        
        
        
        if(group_chat):
            for user in user_list:
                type(driver,user)
                driver.implicitly_wait(10)
                try:
                    #The xpath is obtained by inspecting the exactly on the username
                    first_account = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div')
                    print('Top account found')
                    
                    driver.implicitly_wait(10)
                    first_account.click()
                    print('Top account clicked')
                except:
                    print("Account of the username "+user+" not found.")
                    
            next(driver)
            
            send_message(driver,message)
            print('Group message sent')
              
        else:
            for user in user_list:
                type(driver,user)
                
                driver.implicitly_wait(10)
                try:
                    #The xpath is obtained by inspecting the exactly on the username
                    first_account = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div')
                    print('Top account found')
                    
                    driver.implicitly_wait(10)
                    first_account.click()
                    print('Top account clicked')
                except:
                    print("Account of the username "+user+" not found.")
                
                
                next(driver)
                print('next button clicked.')
                
                send_message(driver,message)
                print('Private message sent')
                
                new_message(driver)
        close_button(driver)
        
def logout(driver):
    account_button = driver.find_element_by_xpath("//*[name()='span'][@class='_2dbep qNELH']")
    print("account button found")
    account_button.click()
    print("account button clicked")
    
    time.sleep(my_sleep_time)
    driver.implicitly_wait(10)
    logout_button = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/div[2]/div")
    print("logout button found")
    logout_button.click()
    print("logout button clicked")
    
def open_new_tab(driver):
    print("Opening new tab")
    try:
        pyautogui.hotkey('ctrl','t')
        print("Trying to open new tab using 'Ctrl + t'.")
        
    except:
        print("Unable to open new tab.")
    
def previous_tab(driver):
    print("Shifting to previous tab")
    pyautogui.hotkey('ctrl','shift','tab')
    print("Shifted to previous tab.")
    
def close_tab(driver):
    pyautogui.hotkey('ctrl','w')
    print("Tab closed.")
    
def close_window(driver):
    pyautogui.hotkey('alt','f4')
    print("Browser closed.")
    
            
        
        