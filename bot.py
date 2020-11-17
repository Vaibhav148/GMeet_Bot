from tabulate import tabulate
from selenium import webdriver
from selenium.webdriver.chrome import service
from time_table import meet
from selenium.webdriver.chrome.options import Options
from time_table import subjects
from time_table import table
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as when
from selenium.webdriver.common.by import By as by
import datetime
from selenium.webdriver.common.keys import Keys
from datetime import date
from threading import Thread
from threading import Timer
import threading
import pyautogui as pag
import sys
from threading import *
import itertools
import keyboard
import msvcrt
from collections import defaultdict
from threading import Event
event = Event()

# //*[@id="yDmH0d"]/c-wiz/div/div/div[6]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[1]/div


usernameFieldPath = "identifierId"
usernameNextButtonPath = "identifierNext"
passwordFieldPath = "password"
passwordNextButtonPath = "passwordNext"
joinButton1Path = "//span[contains(text(), 'Join now')]"
joinButton2Path = "//span[contains(text(), 'Ask to join')]"
endButtonPath = "[aria-label='Leave call']"

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
    discon = 0
    global response
    chrome_options = Options()
    chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
    chrome_driver = "C:/chromedriver.exe"
    # x = os.system("chrome.exe --remote-debugging-port=9222 --user-data-dir="C:\selenum\ChromeProfile"")
    driver = webdriver.Chrome(chrome_driver, options=chrome_options)
    wait = webdriver.support.ui.WebDriverWait(driver, 5)

    driver.get(class_link)
    sleep(2)
    driver.find_element_by_xpath("//body").send_keys(Keys.CONTROL,'d')
    sleep(2)
    driver.find_element_by_xpath("//body").send_keys(Keys.CONTROL,'e')
    sleep(2)
    no_one = "nothing"
    try:
        no_one = driver.find_element_by_xpath("""//*[@id="yDmH0d"]/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[2]""").text
    except:
        print("caught")
        # no_one = driver.find_element_by_xpath("""//*[@id="yDmH0d"]/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[2]""").text
        pass

    print(no_one)
    if no_one !="No one else is here":
        xt = 5



        try:
            try:
                xt = driver.find_element_by_xpath("""//*[@id="yDmH0d"]/c-wiz/div/div/div[7]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[1]/div""").text
                xt = int(xt[1:])  
            except:
                pass


             #//*[@id="yDmH0d"]/c-wiz/div/div/div[6]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[1]/div[1]/div[2]/div[1]/div
            no_ppl = xt+3
            print(xt)
            if no_ppl >=0:

                try:
                    joinButton = wait.until(when.element_to_be_clickable((by.XPATH, joinButton1Path)))
                except:
                    joinButton = wait.until(when.element_to_be_clickable((by.XPATH, joinButton2Path)))
                # driver.find_element_by_xpath("""//*[@id="yDmH0d"]/c-wiz/div/div/div[6]/div[3]/div/div/div[2]/div/div[1]/div[2]/div/div[2]/div/div[1]/div[1]""").click()
            # sleep(1)
            # driver.find_element_by_xpath("//body").send_keys(Keys.CONTROL)
                sleep(1)
                joinButton.click()

                g = d.get(x)
                delta = datetime.timedelta(hours=1)
                now = datetime.datetime.now().time()
                print(now)
                diff = datetime.datetime.combine(date.today(),g) - datetime.datetime.combine(date.today(), now)
                print("press and hold \"f\" to disconnect")




                for i in range(diff.seconds,-1,-1):
                    if keyboard.is_pressed('f'):
                        discon = 1
                        sleep(2)
                        while msvcrt.kbhit():
                            msvcrt.getch()
                        # sys.stdout.write('\r'+"ended")

                        break 
                    print("Class ends in",i,"sec",end='\r')
                    sleep(1) 
               

            
                print()
                print("Current Class Terminated..Moving on to next Class")
                
               
                # for i in range(diff.seconds,-1,-1):
                #     print("Class ends in",i,"sec",end='\r')
                #     sleep(1)
                
                # print()
                if discon == 0:

                    user = threading.Thread(target=user_input)
                    user.daemon = True
                    sleep(2)
                    user.start()
                    user.join(10)
                    if response is None:
                        # print()
                        print("Exiting")
                    else:
                        response = int(response)*60
                        for i in range(response,-1,-1):
                            print("Class ends in",i,"sec",end='\r')
                            sleep(1)

                # print()
                print("Exiting")

               

                driver.find_element_by_xpath("//body").send_keys(Keys.ENTER)
                sleep(2)
                
                endButton = driver.find_element_by_css_selector(endButtonPath)
                endButton.click()

                

                
                # driver.find_element_by_xpath("""//*[@id="ow3"]/div[1]/div/div[6]/div[3]/div[9]/div[2]/div[2]/div""").click()
                # //*[@id="ow3"]/div[1]/div/div[6]/div[3]/div[9]/div[2]/div[2]/div

        except Exception as e:
            print(e)
            pass
    else:
        pass


#attend("https://meet.google.com/tfa-foge-dgb",4)
#exit()
p_time = datetime.datetime.now()

p_day = p_time.weekday()
c ={}
c[9] = subjects[table[p_day][0]]
c[10] = subjects[table[p_day][1]]
c[11] = subjects[table[p_day][2]]
c[12] = subjects[table[p_day][3]]
if p_day!=1:
    c[2] = subjects[table[p_day][4]]
print(c)

s = {}
s[9] = "9:05"
s[10] = "10:15"
s[11] = "11:25"
s[12] = "12:35"
if p_day!=1:

    s[2] = "2:05"


m = []
# m[0].append(subjects[table[p_day][0]])
# m[0].append("9:05")
m.append(c.get(p_time.hour,"null"))
m.append(s.get(p_time.hour,"null"))
print(m)

def animate():
    global done
    
    for c in itertools.cycle(['|', '/', '-', '\\']):
                # sys.stdout.flush()

            
            
                if event.is_set():
                    break

                # if keyboard.is_pressed("p"):
                #     break

                print("Next Class : "+m[0] + " @ "+m[1] + "  "+"  Loading...  "+c,end="\r")
                # sys.stdout.flush()
                sleep(0.1)
           
    print()
flag = 0
done = False
t = threading.Thread(target=animate)
t.daemon = True
t.start()
# print(end="loading")
# n_dots = 0
# delay = 0.5









at = {0:0,1:0,2:0,3:0,4:0}




while True:
    # print(Finding Class)
    try:
        present_time = datetime.datetime.now()
        present_day = present_time.weekday()
        # present_day = 0
        #print(present_day)
        #print(present_time)
        # t.start()
        if present_time.hour == 9 and present_time.minute >=5 and at[0] == 0:
            event.set()
            m.clear()
            done = True
            x = 0
            index_of_class = table[present_day][x]
            print("Attending "+subjects[index_of_class]+" class.")
            class_to_attend = meet[subjects[index_of_class]]
            attend(class_to_attend,x)
            at[0] = 1
            m.append(subjects[table[p_day][1]])
            m.append(s[present_time.hour+1])
            done = False
            event.clear()
            t = threading.Thread(target=animate)
            t.daemon = True
            t.start()
            

        elif present_time.hour == 10 and present_time.minute >=15 and at[1] == 0:
            event.set()
            m.clear()
            done = True
            x = 1
            index_of_class = table[present_day][x]
            print("Attending "+subjects[index_of_class]+" class.")
            class_to_attend = meet[subjects[index_of_class]]
            attend(class_to_attend,x)
            at[1] = 1
            m.append(subjects[table[p_day][2]])
            m.append(s[present_time.hour+1])
            done = False
            event.clear()
            t = threading.Thread(target=animate)
            t.daemon = True
            t.start()
        elif present_time.hour == 11 and present_time.minute >=25 and at[2] == 0:
            event.set()
            m.clear()
            # t.join()
            done = True
            x = 2
            index_of_class = table[present_day][x]
            print("Attending "+subjects[index_of_class]+" class.")
            class_to_attend = meet[subjects[index_of_class]]
            attend(class_to_attend,x)
            at[2] = 1
            # m.clear()
            m.append(subjects[table[p_day][3]])
            m.append(s[present_time.hour+1])        
            done = False
            t = threading.Thread(target=animate)
            event.clear()
            print(event.is_set())
            t.daemon = True

            # t.daemon = True
            t.start()
            
            # print("gg")

            # print(current_thread.name())

        elif present_time.hour == 12 and present_time.minute >=35 and at[3] ==0 :
            event.set()
            # t.join()
            done = True
            x = 3
            index_of_class = table[present_day][x]
            print("Attending "+subjects[index_of_class]+" class.")
            class_to_attend = meet[subjects[index_of_class]]
            attend(class_to_attend,x)
            at[3] = 1
            if present_day!=1:
                m.append(subjects[table[p_day][4]])
                m.append(s[present_time.hour+1]) 
            else:
                m.append("null")
                m.append("null")           
            done = False
            t = threading.Thread(target=animate)
            event.clear()
            t.daemon = True
            t.start()
           
        elif present_time.hour == 14 and present_time.minute >=5 and present_day!=1 and at[4] == 0:
            done = True
            event.set()
            if present_day == 0 or present_day == 2:
                x = 4
            else:
                x = 5
            index_of_class = table[present_day][x]
            print("Attending "+subjects[index_of_class]+" class.")
            class_to_attend = meet[subjects[index_of_class]]
            attend(class_to_attend,x)
            at[4] = 1
            flag = 1
        elif present_day == 1 and present_time.hour >= 13 and present_time.minute > 30:
            flag = 1

        if flag == 1:
            break
    except KeyboardInterrupt:
        break
   

    

       

        
