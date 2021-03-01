from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui,time
from Credentials import *
from OtherDetails import *


CHROME_WEBDRIVER_PATH = "C:\Program Files (x86)\chromedriver.exe"
PATH = "/Users/ashwi/AppData/Local/Google/Chrome/User Data/Default"

LOGIN_LINK = "https://www.instagram.com/accounts/login/"

n=NUMBER_OF_POSTS


class InstagramBot:
    def __init__(self):
        
        options = webdriver.ChromeOptions()
        options.add_argument('--user-data-dir=/Users/ashwi/AppData/Local/Google/Chrome/User Data/Default')
        options.add_argument('profile-directory=Default')
        
        
        self.driver = webdriver.Chrome(executable_path=CHROME_WEBDRIVER_PATH,options=options)
        
        #self.driver = webdriver.Chrome(executable_path=CHROME_WEBDRIVER_PATH)
        print("Bot created.")     
        time.sleep(my_sleep_time)  
        
    def type(self,word):   
        
        print("Type function entered.")
        
        time.sleep(my_sleep_time)
        
        for i in word:
            pyautogui.press(i)
            
        time.sleep(my_sleep_time)
        
        print("Word typed.")
            
    
    def login(self,MYUSERNAME,MYPASSWORD):
        #Pressing f6 thrice will unselect the address bar in the google chrome browser.
        pyautogui.press('f6',presses=3)
        
        self.driver.get(LOGIN_LINK)
        
        
        self.driver.implicitly_wait(10)
        pyautogui.hotkey('win', 'up')
        
        
        time.sleep(my_sleep_time)
        username= self.driver.find_element_by_name('username')
        username.clear()
        username.click()
        
        self.type(MYUSERNAME)
        
        password = self.driver.find_element_by_name('password')
        password.clear()
        password.click()
        
        self.type(MYPASSWORD)
        
        self.driver.find_element_by_css_selector('button[type=submit]').click()

        try:
            warning_message = self.driver.find_element(By.ID,"slfErrorAlert")
            print("Warning message found.Cannot enter.")
            self.driver.quit()
            exit()
        except:
            print("No warnings while entering.")
            
    def SaveInfo(self,choice):
        time.sleep(my_sleep_time)
        try:
            self.driver.implicitly_wait(10)
            if(choice):
                self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/section/div/button').click()
                print("Saved login details.")
            else:
                self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button').click()
                print("Did not save login details.")
            return True
        except:
            print("Login details save did not pop up.")
            return False
        
    def TurnOnNotificationPopUp(self,choice):
        time.sleep(my_sleep_time)
        try:
            self.driver.implicitly_wait(10)
            if(choice):
                self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[1]').click()
                print("Turned on notifications")
            else:
                self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
                print("Turn on notification dismissed for now.")
            return True
        except:
            print("Turn on notifications did not pop up.")
            return False
        
    def search_bar(self,myInput):
        #Clicking the search bar
        search_bar = self.driver.find_element_by_xpath("//*[name()='span'][@class='TqC_a']")
        print("Bar found")
        search_bar.click()
        print("Bar clicked")
        
        #Typing in the search bar
        self.type(myInput)
        
        #Clicking the first account
        account = self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div")
        print("Account found")
        
        
        account.click()
        print("Account clicked")
        
    def get_post_count(self,target_account):
        print("Getting the number of posts for "+target_account+" ...")
        
        time.sleep(my_sleep_time)
        
        number_of_posts = self.driver.find_elements_by_class_name('g47SY ')[0]
        print("Element found.")
        
        
        try:
            number_of_posts = number_of_posts.text
            print("Converted to text.")
        except: 
            print("Error occured trying to convert to text.") 
            
        post_count = ""
        for i in number_of_posts:
            if(i.isdigit()):
                post_count = post_count + str(i)
        
        print("post count of "+target_account+" is ")
        print(str(post_count))
        post_count = int(post_count)
        return post_count
        
        
    def get_followers_count(self,target_account):
        print("Getting followers count for "+target_account+" ...")
        
        
        time.sleep(my_sleep_time)
        
        number_of_followers = self.driver.find_elements_by_class_name('g47SY ')[1]
        number_of_followers = number_of_followers.get_attribute("title")
        followers_count = " "
        for i in number_of_followers:
            if(i.isdigit()):
                followers_count = followers_count + str(i)
        
        print("number of followers ="+followers_count)
        followers_count = int(followers_count)
        return followers_count
    
    def get_following_count(self,target_account):
        print("Getting following count for "+ target_account +"...")
        
        
        time.sleep(my_sleep_time)
        
        number_of_following = self.driver.find_elements_by_class_name('g47SY ')[2]
        print("Element found.")
        
        try:
            number_of_following = number_of_following.text
            print("Converted to text.")
        except: 
            print("Error occured trying to convert to text.")    
                 
        following_count = ""
        for i in number_of_following:
            if(i.isdigit()):
                following_count = following_count + str(i)
        
    
        
        
        print("Following count of "+target_account+" is ")
        print(str(following_count))
        following_count = int(following_count)
        return following_count
    
    def close_button(self):
        time.sleep(my_sleep_time)
        self.driver.implicitly_wait(10)
        try:
            close = self.driver.find_element_by_xpath("//*[name()='svg'][@aria-label='Close']")
        except:
            print("close button not found.")

        print("Close button found.")
        close.click()
        print("Closed.")
        
    def my_account(self):
        time.sleep(my_sleep_time)
        account_button = self.driver.find_element_by_xpath("//*[name()='span'][@class='_2dbep qNELH']")
        print("Account button")
        account_button.click()
        print("account button clicked.")
        
        time.sleep(my_sleep_time)
        
        #Xpaths for my profile link.
        xpath1 = "/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/a[1]/div/div[2]/div/div/div/div"
        
        #This xpath selects the first sub division within the popup which popups when the account_button is clicked.
        xpath2 = "//*[name()='a'][@class='-qQT3']"
        
        
        profile_button = self.driver.find_element_by_xpath(xpath2)
        print("Profile button found")
        
        profile_button.click()
        print("Profile button clicked.")
        
    def get_following(self,target_account):
        print("Getting following list for "+target_account+" ...")
        
        time.sleep(my_sleep_time)
        self.search_bar(target_account)
        number_of_following = self.get_following_count(target_account)
        
        time.sleep(my_sleep_time)
        following_link = self.driver.find_element_by_partial_link_text('following')
        print("Following link found")
        following_link.click()
        print("Following link clicked.")
        
        time.sleep(my_sleep_time)
        scrollable_popup = self.driver.find_element_by_class_name("isgrP")
        following_list = []
        
        i=1
        while(len(following_list) < number_of_following ):
            
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight',scrollable_popup)
            time.sleep(0.4)
            following_list_unextracted = scrollable_popup.find_elements_by_class_name("FPmhX")
            
            for f in following_list_unextracted:
                if(len(following_list) < number_of_following and f.text not in following_list):
                    following_list.append(f.text)
                    i+=1
        print("Following list of "+target_account)
        print(following_list)
        self.close_button()
        return following_list
    
    def Like_Post(self,choice,TARGET_ACCOUNT_USERNAME,n):
        if(choice and n>0):
            #Go to the required account.
            hash = '#'
            hash_tag = True
            
            if(TARGET_ACCOUNT_USERNAME.find(hash) == -1):
                hash_tag = False
            
                
            
            
            self.search_bar(TARGET_ACCOUNT_USERNAME)

            self.driver.implicitly_wait(6)
            print("Waiting..")
            
            number_of_posts = self.get_post_count(TARGET_ACCOUNT_USERNAME)
            
            if(number_of_posts != 0):
                
                #Click on the first post.
                self.driver.implicitly_wait(3)
                try:
                    if(not hash_tag):
                        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]').click()
                    else:
                        print("trying to click the hash tag first post.")
                        self.driver.find_element_by_xpath("//*[name()='div'][@class='eLAPa']").click()
                    print('First post clicked 1')
                    post_available = True
                except:
                    try:
                        self.driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[2]/article/div[1]/div/div[1]/div[1]').click()
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
                        self.driver.implicitly_wait(10)
                        try:
                            time.sleep(1)
                            
                            #Find if the post is liked already by searching for like button.
                            try:
                                ul = self.driver.find_element_by_xpath("//*[name()='svg'][@aria-label='Unlike']")
                                print('Unlike button found so post liked already.')
                            except:
                                l = self.driver.find_element_by_xpath("//*[name()='svg'][@aria-label='Like']")
                                l.click()
                                print("Like button clicked.")
                        except:
                            print("Like button not found.")

                        #Move to next post
                        if(i==0):
                            self.driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a").click()
                        else:
                            #Different xpath from second post on because the is a forward and back arraw to move between post arises.
                            self.driver.find_element_by_xpath("/html/body/div[5]/div[1]/div/div/a[2]").click()
                                                    
                        i+=1
                    self.close_button()
                
                
            else:
                print('No post available in the account.')
                
    def follow(self,choice,FOLLOWING_ACCOUNT_USERNAME_LIST):
        print("Follow function entered.")
        if(choice):
            for FOLLOWING_ACCOUNT_USERNAME in FOLLOWING_ACCOUNT_USERNAME_LIST:
                print("Going to following link")
                self.search_bar(FOLLOWING_ACCOUNT_USERNAME)
                
                
                self.driver.implicitly_wait(5)
                print("waiting")
                
                
                try:
                    follow_buton = self.driver.find_element_by_xpath("//*[name()='button'][@class='_5f5mN       jIbKX  _6VtSN     yZn4P   ']")
                    print('button found')
                    time.sleep(my_sleep_time)
                    follow_buton.click()
                    print("Follow button clicked.")
                except:
                    try:
                        following_buton = self.driver.find_element_by_xpath("//*[name()='span'][@aria-label='Following']")
                        print("Already following")
                    except:
                        print("Error occured trying to follow the account.")
                        
    def follow_random(self,follow_choice,target_account,follow_amount):
        if(follow_choice):
            self.search_bar(target_account)
            time.sleep(my_sleep_time)
            
            #Followers button
            self.driver.find_element_by_partial_link_text('followers').click()
            
            
            
            #Popup without heading
            popup = self.driver.find_element_by_xpath("//*[name()='div'][@class='isgrP']")
            print('popup found')
            
            
            time.sleep(my_sleep_time)
            #self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight',popup)
            
            follow_buttons_clicked = 0
            time.sleep(my_sleep_time)
            
            
            while(follow_buttons_clicked < follow_amount):
                self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight',popup)
                follow_buttons = self.driver.find_elements_by_xpath("//*[name()='button'][@class='sqdOP  L3NKy   y3zKF     ']")
                for follow_button in follow_buttons:
                    time.sleep(my_sleep_time)
                    follow_button.click()
                    follow_buttons_clicked += 1
                    if(follow_amount == follow_buttons_clicked-1):
                        break
                    
            self.close_button()
            time.sleep(my_sleep_time)
            
    def next(self):
        self.driver.implicitly_wait(10)
        Next = self.driver.find_element_by_xpath("//*[name()='button'][@class='sqdOP yWX7d    y3zKF   cB_4K  ']")
        Next.click()
        
    def send_message(self,message):
        time.sleep(my_sleep_time)
        self.driver.implicitly_wait(10)
        message_textarea = self.driver.find_element_by_tag_name('textarea')
        
        #message_textarea = driver.find_element_by_xpath('//*input[@placeholder="Message..." and not(@disabled)]')
        print("message area found")
        message_textarea.click()
        print("message area clicked")
        message_textarea.clear()
        print("message area ready.")
        
        self.type(message)
        
        pyautogui.press('enter')
            
    def new_message(self):
        self.driver.implicitly_wait(10)
        try:
            Send_message_button = self.driver.find_element_by_xpath("//*[name()='svg'][@aria-label='New Message']")
            print("New message button found.")
        except:
            try:
                Send_message_button = self.driver.find_element_by_xpath("//*[name()='button'][@class='sqdOP  L3NKy   y3zKF     ']")
                print("Send message button 2 found.")
            except:
                print("Send message button not found.")
        
        
        self.driver.implicitly_wait(10)
        Send_message_button.click()
        print("New message button clicked.")
        
        
        #Clearing and selecting query box.
        self.driver.implicitly_wait(10)
        queryBox = self.driver.find_element_by_name('queryBox')
        print('query box found.')
        queryBox.click()
        print('query box clicked.')
        queryBox.clear()
        print('query box cleared.')
        
    def message(self,choice,group_chat,user_list,message):
        if(choice):
            
            #Click the message tab button
            self.driver.implicitly_wait(10)
            try:
                messenger_button = self.driver.find_element_by_xpath("//*[name()='svg'][@aria-label='Direct']")
                print("Direct svg found")
            except:
                try:
                    messenger_button = self.driver.find_element_by_xpath("//*[name()='svg'][@aria-label='Messenger']")
                    print("Messenger svg found")
                except:
                    print("Messenger svg not found")
            
            messenger_button.click()
            print('Messenger svg clicked.')
            
            #Click new message button
            self.new_message()
            
            
            
            if(group_chat):
                for user in user_list:
                    type(user)
                    self.driver.implicitly_wait(10)
                    try:
                        #The xpath is obtained by inspecting the exactly on the username
                        first_account = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div')
                        print('Top account found')
                        
                        self.driver.implicitly_wait(10)
                        first_account.click()
                        print('Top account clicked')
                    except:
                        print("Account of the username "+user+" not found.")
                        
                self.next()
                
                self.send_message(message)
                print('Group message sent')
                
            else:
                for user in user_list:
                    self.type(user)
                    
                    self.driver.implicitly_wait(10)
                    try:
                        #The xpath is obtained by inspecting the exactly on the username
                        first_account = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[2]/div[1]/div/div[2]/div[1]/div/div')
                        print('Top account found')
                        
                        self.driver.implicitly_wait(10)
                        first_account.click()
                        print('Top account clicked')
                    except:
                        print("Account of the username "+user+" not found.")
                    
                    
                    self.next()
                    print('next button clicked.')
                    
                    self.send_message(message)
                    print('Private message sent')
                    
                    self.new_message()
            self.close_button()
            
    def logout(self):
        account_button = self.driver.find_element_by_xpath("//*[name()='span'][@class='_2dbep qNELH']")
        print("account button found")
        account_button.click()
        print("account button clicked")
        
        time.sleep(my_sleep_time)
        self.driver.implicitly_wait(10)
        logout_button = self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/div[2]/div")
        print("logout button found")
        logout_button.click()
        print("logout button clicked")
        
    def close_tab(self):
        pyautogui.hotkey('ctrl','w')
        print("Tab closed.")
 
#Main program.       
try:
    bot = InstagramBot() 
    
    #First time login procedures.   
    try:
        bot.login(MYUSERNAME,MYPASSWORD)
        
        #Save login info
        if(SAVE_CHOICE):
            SaveInfoPopUpAppears = bot.SaveInfo(SAVE_CHOICE)

        #Turn notifications off.
        NotifyPopUpAppears = bot.TurnOnNotificationPopUp(NOTIFY_CHOICE)

        #Save login info.Recheck.
        if(SAVE_CHOICE and not SaveInfoPopUpAppears):
            print('Entered save info again1.')
            SaveInfoPopUpAppears = bot.SaveInfo(SAVE_CHOICE)
            print('Saved login info.')
    except:
        print("Login procedures did not pop up.") 
        
    
   
    bot.follow(FOLLOW_CHOICE,FOLLOWING_ACCOUNT_USERNAME_LIST)
    bot.follow_random(random_follow_choice,follow_random_target_account,follow_amount)
    bot.message(MESSAGE_CHOICE,GROUP_CHAT_CHOICE,MESSAGE_USER_TARGET,MY_MESSAGE)
    
except:  
    print("Some error occured.")
    
bot.close_tab()
print("Python program exited.")
exit()
        
        
        
        