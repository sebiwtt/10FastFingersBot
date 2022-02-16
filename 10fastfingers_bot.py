from selenium import webdriver
from selenium.webdriver.common.by import By
from pynput.keyboard import Key, Controller
import time

def type(word):
    for key in word:
        keyboard.press(key)
        keyboard.release(key)
        time.sleep(0.01)
    space = " "    
    keyboard.press(space)
    keyboard.release(space)  

URL = 'https://10fastfingers.com/typing-test/german'
wpm = 170

keyboard = Controller() 
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:\\Users\\theon\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
browser = webdriver.Chrome(options=options)
browser.get(URL)

time.sleep(3)

main_container = browser.find_element(By.ID, "main")
reload_box = main_container.find_element(By.ID, 'reload-box')
words = reload_box.find_element(By.ID, "words")
row = words.find_element(By.ID, "row1")
wordlist = row.find_elements(By.TAG_NAME, "span")

text = ""

for word in wordlist:
    text += word.get_attribute('innerHTML') + " "

single_words = text.split(" ")

textbox = reload_box.find_element(By.ID, "inputfield");  
textbox.send_keys("")

for word in single_words[:wpm]:
    type(word)
    time.sleep(0.01)
    
#browser.close()