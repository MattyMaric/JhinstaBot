from selenium import webdriver
from secrets import email, password
from Quotes import JhinQuotes
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import choice

class JhinstaBot():
    def __init__(self, email, password):
        self.browser = webdriver.Chrome()
        self.email = email
        self.password = password
       
     
     #SignIn function opens up the Instagram login page,
     #Takes the users credentials from the secrets file 
     #and logs them into their account using those credentials
    def SignIn(self):
        self.browser.get('https://www.instagram.com/accounts/login/')
        sleep(2)
        emailInput = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input') 
        passwordInput = self.browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input')
        emailInput.send_keys(self.email)
        
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        sleep(3)  

    #Presses the "not now" buttons that appear after the login    
    def PopUp(self):
        sleep(2)
        NotNow = self.browser.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
        NotNow.click() 
    
    def PopUp2(self):
        sleep(2)
        NotNow2 = self.browser.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')
        NotNow2.click()

    # DM_Access Goes into the DM page on Instagram and selects the first person on the list (Recipient) and opens the chat history
    def DM_Access(self):
        sleep(2)
        DirectMessage = self.browser.get('https://www.instagram.com/direct/inbox/')
        sleep(2)
        Recipient = self.browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[1]/div[2]/div/div/div/div/div[1]/a/div/div[2]/div[1]/div/div/div/div')
        Recipient.click()

    #Main part of the code, selects the empty chat bar on the bottom, writes a random Jhin quote from the Quotes file and sends it
    # After that the bot waits 44 seconds (Because haha 4) before doing it all over again, and again, and again...
    def SendLoop(self):
        while True:
            sleep(1)
            Message = self.browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
            Message.click()
            Message.send_keys(choice(JhinQuotes), Keys.ENTER)
            sleep(43)
        
          


bot = JhinstaBot(email, password)
bot.SignIn()
bot.PopUp2()
bot.PopUp()
bot.DM_Access()    
bot.SendLoop()