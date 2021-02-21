import pyautogui

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
    
def search_bar(driver,myInput):
    #Clicking the search bar
    search_bar = driver.find_element_by_xpath("//*[name()='span'][@class='TqC_a']")
    print("Bar found")
    search_bar.click()
    print("Bar clicked")
    
    #Typing in the search bar
    driver.implicitly_wait(5)
    for i in myInput:
        pyautogui.press(i)
    print("Typing input...")
    
    #Clicking the first account
    account = driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div")
    print("Account found")
    
    
    account.click()
    print("Account clicked")
    
    
    
def Like_Post(driver,choice,TARGET_ACCOUNT_USERNAME,n):
    if(choice and n>0):
        #Go to the required account.
        #driver.get(WEBSITE_LINK+TARGET_ACCOUNT_USERNAME+"/")
        search_bar(TARGET_ACCOUNT_USERNAME)

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

