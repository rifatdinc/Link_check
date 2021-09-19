#!/usr/bin/python3
from gtts import gTTS
from playsound import playsound
import random
import os



def speak(string):
    tts = gTTS(string,lang='tr',slow=False)
    rand = random.randint(1,1000)
    file = 'auido-' +str(rand)+'.mp3'
    tts.save(file)
    playsound(file)
    os.remove(file)


def main(): 
    sayac = 0
    while True:
        sayac += 1
        if sayac == 10:
            break
        speak("Bismillâhi’r-Rahmâni’Rahîm.  Elhamdulillâhi Rabbi’l-âlemîn.Er-Rahmâni’r-Rahîm.Mâliki yevmi’d-dîn.")

main()