import pyautogui,time
from selenium.webdriver.common.keys import Keys
from OtherDetails import my_sleep_time 
from selenium.webdriver.common.by import By

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

    try:
        warning_message = driver.find_element(By.ID,"slfErrorAlert")
        print("Warning message found.Cannot enter.")
        driver.quit()
        exit()
    except:
        print("No warnings while entering.")
        
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
    
def my_account(driver):
    time.sleep(my_sleep_time)
    account_button = driver.find_element_by_xpath("//*[name()='span'][@class='_2dbep qNELH']")
    print("Account button")
    account_button.click()
    print("account button clicked.")
    
    time.sleep(my_sleep_time)
    
    #Xpaths for my profile link.
    xpath1 = "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]/div/div[2]/div/div/div/div"
    
    #This xpath selects the first sub division within the popup which popups when the account_button is clicked.
    xpath2 = "//*[name()='a'][@class='-qQT3']"
    
    
    profile_button = driver.find_element_by_xpath(xpath2)
    print("Profile button found")
    
    profile_button.click()
    print("Profile button clicked.")
    
def get_followers_count(driver):
    print("Entered def")
    number_of_followers = driver.find_elements_by_class_name('g47SY ')[1]
    number_of_followers = number_of_followers.get_attribute("title")
    followers_count = " "
    for i in number_of_followers:
        if(i.isdigit()):
            followers_count = followers_count + str(i)
    #print("number of followers ="+number_of_followers.text)
    print("number of followers ="+followers_count)
    followers_count = int(followers_count)
    return followers_count

    
def following(driver):
    driver.get("https://instagram.com/my_spam_bot")
    number_of_following = 4
    time.sleep(my_sleep_time)
    following_link = driver.find_element_by_partial_link_text('following')
    print("Following link found")
    following_link.click()
    print("Following link clicked.")
    
    time.sleep(my_sleep_time)
    scrollable_popup = driver.find_element_by_class_name("isgrP")
    """
    #My following list with both following and suggested accounts link.
    following_list_portion_with_suggested_accounts = driver.find_element_by_tag_name("ul")
    
    #Following list portion of the HTML.
    #following_list_portion = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul")
    following_list_portion = driver.find_element_by_class_name("jSC57")
    print("Following list portion found.")
    time.sleep(my_sleep_time)
    
    following_list_unextracted = following_list_portion.find_elements_by_class_name("FPmhX")
    print("My following list found.")
    """
    following_list = []
    
    i=1
    while(len(following_list) < number_of_following ):
        
        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight',scrollable_popup)
        time.sleep(0.4)
        following_list_unextracted = scrollable_popup.find_elements_by_class_name("FPmhX")
        
        for f in following_list_unextracted:
            if(len(following_list) < number_of_following and f.text not in following_list):
                following_list.append(f.text)
                i+=1
    print(following_list)
    close_button(driver)
    
    
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
                    
def follow_random(driver,follow_choice,target_account,follow_amount):
    if(follow_choice):
        search_bar(driver,target_account)
        time.sleep(my_sleep_time)
        #Followers button
        #driver.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]').click()
        driver.find_element_by_partial_link_text('followers').click()
        
        #popup = driver.find_element_by_xpath("//*[name()='div'][@role='dialog']")
        
        #Popup without heading
        popup = driver.find_element_by_xpath("//*[name()='div'][@class='isgrP']")
        
        #popup = driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
        print('popup found')
        
        
        time.sleep(my_sleep_time)
        driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight',popup)
        
        follow_buttons_clicked = 0
        time.sleep(my_sleep_time)
        follow_buttons = driver.find_elements_by_xpath("//*[name()='button'][@class='sqdOP  L3NKy   y3zKF     ']")
        
        
        for follow_button in follow_buttons:
            time.sleep(my_sleep_time)
            follow_button.click()
            follow_buttons_clicked += 1
            if(follow_buttons_clicked%5==0):
               driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight',popup)
            if(follow_amount == follow_buttons_clicked-1):
                break
        time.sleep(my_sleep_time)
        
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
    
            
        
        