#import modules
import os
import time
import threading
from playsound import playsound

#create the functions
def playAudio():
    #plays the audio file
    playsound('audio.wav')
def showParrot():
    #shows a dancing parrot
    os.system('curl parrot.live')
def shutDown():
    #waits custom ammount of seconds before shutting down
    #here i have it set to the length of the audio file
    time.sleep(94)
    os.system('shutdown /s /t 1')









Thread1 = threading.Thread(target=function_1)
Thread2 = threading.Thread(target=function_2)

Thread1.start()
Thread2.start()
Thread3.start()

# Wait for the threads to finish
Thread1.join()
Thread2.join()
Thread3.join()