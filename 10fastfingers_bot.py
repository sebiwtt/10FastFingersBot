from selenium import webdriver
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
import time

#-----------------Functions-------------------

def type(word):
    for key in word:
        keyboard.press(key)
        keyboard.release(key)
    space = " "    
    keyboard.press(space)
    keyboard.release(space)  

def login(email, password):
    sidebar = browser.find_element(By.ID, "sidebar-md-lg")
    items = sidebar.find_elements(By.CLASS_NAME, "list-group")
    login_link = items[1].find_element(By.TAG_NAME, "a")
    login_link.click()

    mail_field = browser.find_element(By.ID, "UserEmail")
    pass_field = browser.find_element(By.ID, "UserPassword")
    submit = browser.find_element(By.ID, "login-form-submit")
    

    mail_field.send_keys(email)
    pass_field.send_keys(password)
    submit.click()

#-----------------Variables-------------------
#--------Set your own variables here!----------

#Set URL and desired WPM
URL = 'https://10fastfingers.com/competition/620d2c751a1e1'
wpm = 80

#Set your login Info
mail = "yourMail"
secret = "yourPassword"

#Select which browser you want to use! You will need to have the Chrome/Geko driver installed
browser = webdriver.Chrome()
#browser = webdriver.Firefox()

#-----------------Main Code-------------------

keyboard = Controller() 

browser.get(URL)
login(mail, secret) #Turn off login if not needed
browser.get(URL)

time.sleep(3)

main_container = browser.find_element(By.ID, "main")
reload_box = main_container.find_element(By.ID, 'reload-box')
words = reload_box.find_element(By.ID, "words")
row = words.find_element(By.ID, "row1")
wordlist = row.find_elements(By.TAG_NAME, "span")
input = browser.find_element(By.ID, "inputfield")

text = ""

for word in wordlist:
    text += word.get_attribute('innerHTML') + " "

single_words = text.split(" ")
  
input.send_keys("")

delay = 60/wpm

for word in single_words[:wpm]:
    type(word)
    time.sleep(delay)
    
#Uncomment if browser should automatically close    
#browser.close()