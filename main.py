from selenium import webdriver
import time
from pyfiglet import Figlet

# The profile where I enabled the VPN previously using the GUI.
def nine():
    my()
    
def my():
    opera_profile = r'C:\Users\nikhil bariki\AppData\Roaming\Opera Software\Opera Stable' 
    options = webdriver.ChromeOptions()
    options.add_argument('user-data-dir=' + opera_profile)
    options.add_argument("private");
    driver = webdriver.Opera(options=options,executable_path=r"C:\Users\nikhil bariki\Desktop\operadriver_win64\operadriver.exe")
    driver.get('http://bitcoinforums.me?mref=52')
    i = 0
    while True:
         time.sleep(10)
         driver.quit()
         nine()


if __name__ == "__main__":
    my()


 



