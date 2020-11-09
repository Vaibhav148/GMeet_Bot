# import msvcrt
# import time

# t0 = time.time()
# print(t0)
# while time.time() - t0 <50:
#     if msvcrt.kbhit():
#         if msvcrt.getch() == '\r': # not '\n'
#             break
#     time.sleep(0.1)

import threading

# response = None
# def user_input():
#     global response
#     response = input("Do you wish to reconnect? ")

# user = threading.Thread(target=user_input)
# user.daemon = True
# user.start()
# print("1")
# user.join(5)
# print("2")
# if response is None:
#     print()
#     print("Exiting")
# else:
#     print("As you wish")
# print("gg")
# from time import sleep

# while(1):
# 	try:
# 	    for i in range(60,-1,-1):
# 	        print("Class ends in",i,"sec",end='\r')
# 	        sleep(1)
		

# 	except KeyboardInterrupt:
# 	        print("Press Ctrl-C to terminate while statement")
# 	        pass
# 	print("hello")
from time import sleep

# def printd(text, delay=.5):
#     print(end=text)
#     n_dots = 0

#     while True:
#         if n_dots == 3:
#             print(end='\b\b\b', flush=True)
#             print(end='   ',    flush=True)
#             print(end='\b\b\b', flush=True)
#             n_dots = 0
#         else:
#             print(end='.', flush=True)
#             n_dots += 1
#         sleep(delay)
# printd("loading")

# import sys

# sys.stdout.write('Loading.')
# sys.stdout.write('\r')
# sys.stdout.flush()
# sleep(1)
# sys.stdout.write('Loading..')
# sys.stdout.write('\r')
# sys.stdout.flush()
# sleep(1)


# sys.stdout.write('Loading...')
# sys.stdout.write('\r')
# sys.stdout.flush()
# sleep(1)

# import itertools
# import threading
# import time
# import sys

# done = False
# #here is the animation
# def animate():
# 	for c in itertools.cycle(['|', '/', '-', '\\']):
# 		if done:
# 			print("gg")
# 			break
# 		sys.stdout.write('\rloading ' + c)
# 		sys.stdout.flush()
# 		time.sleep(0.1)
# 	sys.stdout.write('\rDone!     ')

# i = 0
# t = threading.Thread(target=animate)
# t.start()
# try:
# 	while True:

# 		# print()
# 		# print(i)
# 		# if i==100000000000:
# 		# 	done = True
# 		# 	print("found",i)
# 			# done = False
# 			# break
# 		if i==10000000:
# 			done = True
# 			# sys.stdout.flush()
# 			# sys.stdout.write('\rfound ' + str(i))
# 			print()
# 			print("found")
# 			t = threading.Thread(target=animate)
# 			done = False
# 			t.start()
# 		if i==20000000:
# 			done =True
# 			print()
# 			print("found2")
# 			break



		
# 			# done =False
# 		# done = False
# 		i+=1
	
# except KeyboardInterrupt:
# 	pass

#long process here
# time.sleep(10)
# done = True


# import keyboard  # using module keyboard
# while True:  # making a loop
#     try:  # used try so that if user pressed other than the given key error will not be shown
#         if keyboard.is_pressed('q'):  # if key 'q' is pressed 
#             print('You Pressed A Key!')
#             break  # finishing the loop
#     except:
#         break  # if user pressed a key other than the given key the loop will break

import time
# import subprocess
import sys
import msvcrt

alarm1 = int(input("How many seconds (alarm1)? "))

while (1):
    time.sleep(alarm1)
    print("Alarm1")
    sys.stdout.flush()

    # Try to flush the buffer
    # while msvcrt.kbhit():
    #     msvcrt.getch()

    print ("Continue (Y/N)?[Y]")
    doit = msvcrt.getch()
    print (type(doit),int(doit))
    if doit == 'N' or doit=='n':
        print ("Exiting.....")
        break