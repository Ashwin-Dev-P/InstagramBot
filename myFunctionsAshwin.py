import pyautogui,time

def login(driver,MYUSERNAME,MYPASSWORD):
    driver.implicitly_wait(10)

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
        #driver.get(WEBSITE_LINK+TARGET_ACCOUNT_USERNAME+"/")
        search_bar(driver,TARGET_ACCOUNT_USERNAME)

        driver.implicitly_wait(6)
        number_of_posts = driver.find_element_by_class_name('g47SY ')
        print("number of posts =",number_of_posts.text)

        try:
            number_of_posts = int(number_of_posts.text)
            if(number_of_posts > 0):
                post_available = True
        except:
            print("Unable to convert no. of post from text to integer.")

        
        if(number_of_posts != 0):
            
            #Click on the first post.
            driver.implicitly_wait(3)
            try:
                driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]').click()
                print('First post clicked 1')
                post_available = True
            except:
                try:
                    driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]').click()
                    print('First post clicked 2')
                    post_available = True
                    
                except:
                    print("No posts available.")
                    post_available = False
            
            #Like if the first post is available.
            if(post_available == True):
                i=0
                

                #Loop until the required number of post are liked.
                while(i<n):
                    driver.implicitly_wait(10)
                    try:
                        l = driver.find_element_by_xpath("//*[name()='svg'][@aria-label='Like']")
                        print('Like button found')
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
    time.sleep(2)
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
            
        
        