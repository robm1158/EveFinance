import threading
import time

print("intial Push for dev branch")
print("Hunter initial push")
# Phase 1 - Commence

def timePrintingExample():
    print ("ctime : ", time.ctime())
    
WAIT_TIME_SECONDS = 5

ticker = threading.Event()
while not ticker.wait(WAIT_TIME_SECONDS):
    timePrintingExample()