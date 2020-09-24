from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from random import choice
from secrets import email, password
from Quotes import JhinQuotes

YesAnswers = ['y', 'Y', 'YES','Yes', 'yes']
NoAnswers = ['n', 'N', 'NO','No', 'no']



print('Write the Instagram username of the person you want to send Jhin quotes to')
recipient = input('Don\'t forget the dots(.) or underscores (_) in the username ')

print('You are going to send Jhin quotes to ' + recipient)
Confirmation = input('Are you sure? Y/N ')




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
        emailInput = self.browser.find_element_by_name('username') 
        passwordInput = self.browser.find_element_by_name('password')
        emailInput.send_keys(self.email)
        
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        sleep(3)  

    #Presses the "not now" buttons that appear for password saving and desktop notifications   
    def PopUp(self):
        sleep(3)
        NotNow = self.browser.find_element_by_xpath('//button[text()="Not Now"]')
        NotNow.click()
    
    def PopUp2(self):
        sleep(3)
        NotNow2 = self.browser.find_element_by_xpath('//button[text()="Not Now"]')
        NotNow2.click()

    #The bot takes the username given at the beginning and finds the profile by combining the username
    # with instagrams link, after that it searches the page for the message button and clicks it
    def DM_Access(self):
        Rec_Insta_Page = 'https://www.instagram.com/' + recipient + '/'
        self.browser.get(Rec_Insta_Page)
        sleep(3)
        MessageButton = self.browser.find_element_by_xpath('//button[text()="Message"]')
        MessageButton.click()
        

    #Main part of the code, selects the empty chat bar on the bottom, writes a random Jhin quote from the Quotes file and sends it
    # After that the bot waits 44 seconds (Because haha 4) before doing it all over again, and again, and again...
    def SendLoop(self):
        while True:
            sleep(1)
            Message = self.browser.find_element_by_xpath('/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
            Message.click()
            Message.send_keys(choice(JhinQuotes), Keys.ENTER)
            sleep(43)
        
          

def execution():
    bot = JhinstaBot(email, password)
    bot.SignIn()
    bot.PopUp2()
    bot.PopUp()
    bot.DM_Access()    
    bot.SendLoop()


#If the user says yes to the promp at the beginning of the code, the code runs, otherwise it shuts down
if Confirmation in YesAnswers:
    execution()
elif Confirmation in NoAnswers:
    print('Okay, come back when you change your mind')
    exit()
else:
    print('Invalid response given, shutting down...')
    exit()
