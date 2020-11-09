from tabulate import tabulate
from selenium import webdriver
from selenium.webdriver.chrome import service
from time_table import meet
from selenium.webdriver.chrome.options import Options
from time_table import subjects
from time_table import table
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
import datetime
from selenium.webdriver.common.keys import Keys
from datetime import date
from threading import Thread
from threading import Timer
import threading
import pyautogui as pag
import sys
import itertools
import keyboard
import msvcrt




timeout = 10
answer = 0
response = None

def user_input():
    global response
    # sys.stdin.flush()
    while msvcrt.kbhit():
        msvcrt.getch()
    # print("Enter wait time")
    # response = msvcrt.getch()

    response = input("Do you wish to continue??..If yes Enter wait time:")




d = {0:datetime.time(10,0,0),1:datetime.time(11,10,0),2:datetime.time(12,20,0),3:datetime.time(17,4,0),4:datetime.time(18,45,0),5:datetime.time(16,0,0)}


def attend(class_link,x):
    global response
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = "C:/chromedriver.exe"
    # x = os.system("chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\ChromeProfile"")
    driver = webdriver.Chrome(chrome_driver, options=chrome_options)

    driver.get(class_link)
    sleep(2)
    driver.find_element_by_xpath("//body").send_keys(Keys.CONTROL,'d')
    sleep(2)
    driver.find_element_by_xpath("//body").send_keys(Keys.CONTROL,'e')
    sleep(2)
    driver.find_element_by_xpath("""//*[@id="yDmH0d"]/c-wiz/div/div/div[6]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]""").click()
    # sleep(1)
    # driver.find_element_by_xpath("//body").send_keys(Keys.CONTROL)

    g = d.get(x)
    delta = datetime.timedelta(hours=1)
    now = datetime.datetime.now().time()
    print(now)
    diff = datetime.datetime.combine(date.today(),g) - datetime.datetime.combine(date.today(), now)
    print("press and hold \"f\" to disconnect")



    for i in range(diff.seconds,-1,-1):
        if keyboard.is_pressed('f'):
            break 
        print("Class ends in",i,"sec",end='\r')
        sleep(1) 
       

    
    print()
    print("Current Class Terminated..Moving on to next Class")
    
   
    # for i in range(diff.seconds,-1,-1):
    #     print("Class ends in",i,"sec",end='\r')
    #     sleep(1)
    
    print()
    user = threading.Thread(target=user_input)
    user.daemon = True
    sleep(2)
    user.start()
    user.join(10)
    if response is None:
        print()
        print("Exiting")
    else:
        response = int(response)*60
        for i in range(response,-1,-1):
            print("Class ends in",i,"sec",end='\r')
            sleep(1)

        print()
        print("Exiting")

   

    driver.find_element_by_xpath("//body").send_keys(Keys.ENTER)
    sleep(2)

    
    driver.find_element_by_xpath("""//*[@id="ow3"]/div[1]/div/div[6]/div[3]/div[9]/div[2]/div[2]/div""").click()
    # //*[@id="ow3"]/div[1]/div/div[6]/div[3]/div[9]/div[2]/div[2]/div


attend("https://meet.google.com/tfa-foge-dgb",4)
exit()

def animate():
    global done
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rFinding Class ' + c)
        sys.stdout.flush()
        sleep(0.1)
flag = 0
done = False
t = threading.Thread(target=animate)
t.start()
# print(end="loading")
# n_dots = 0
# delay = 0.5
while True:
    # print(Finding Class)
    present_time = datetime.datetime.now()
    present_day = present_time.weekday()
    # present_day = 0
    #print(present_day)
    #print(present_time)
    # t.start()
    if present_time.hour == 9 and present_time.minute >=10:
        done = True
        x = 0
        index_of_class = table[present_day][x]
        print("Class Found : ",subjects[index_of_class])
        print("Attending "+subjects[index_of_class]+" class.")
        class_to_attend = meet[subjects[index_of_class]]
        attend(class_to_attend,x)
        done = False
        t = threading.Thread(target=animate)
        t.start()
        

    elif present_time.hour == 10 and present_time.minute >=15:
        done = True
        x = 1
        index_of_class = table[present_day][x]
        print("Class Found : ",subjects[index_of_class])
        print("Attending "+subjects[index_of_class]+" class.")
        class_to_attend = meet[subjects[index_of_class]]
        attend(class_to_attend,x)
        done = False
        t = threading.Thread(target=animate)
        t.start()
    elif present_time.hour == 11 and present_time.minute >=25:
        done = True
        x = 2
        index_of_class = table[present_day][x]
        print("Class Found : ",subjects[index_of_class])
        print("Attending "+subjects[index_of_class]+" class.")
        class_to_attend = meet[subjects[index_of_class]]
        attend(class_to_attend,x)
        done = False
        t = threading.Thread(target=animate)
        t.start()
    elif present_time.hour == 12 and present_time.minute >=35 :
        done = True
        x = 3
        index_of_class = table[present_day][x]
        print("Class Found : ",subjects[index_of_class])
        print("Attending "+subjects[index_of_class]+" class.")
        class_to_attend = meet[subjects[index_of_class]]
        attend(class_to_attend,x)
        done = False
        t = threading.Thread(target=animate)
        t.start()
    elif present_time.hour == 14 and present_time.minute >=5 and present_day!=1:
        done = True
        if present_day == 0 or present_day == 2:
            x = 4
        else:
            x = 5
        index_of_class = table[present_day][x]
        print("Class Found : ",subjects[index_of_class])
        print("Attending "+subjects[index_of_class]+" class.")
        class_to_attend = meet[subjects[index_of_class]]
        attend(class_to_attend,x)
        flag = 1
    elif present_day == 1:
        flag = 1

    if flag == 1:
        break
    
   

    

       

        
