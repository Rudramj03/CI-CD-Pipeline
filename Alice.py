
from importlib.util import spec_from_file_location
import sys
from urllib.request import urlcleanup
from more_itertools import take
import pyttsx3
import datetime
from requests.api import head
import speech_recognition as sr
import wikipedia
import webbrowser as web
import time
import os
import random
import pyjokes
import requests
from bs4 import BeautifulSoup
import pywhatkit as kit
from tkinter import *

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id) #getting details of current voice
engine.setProperty('rate', 200)


def speak(audio):
     engine.say(audio)
     engine.runAndWait() #Without this command, speech will not be audible to us

def wishme():
     hour = int(datetime.datetime.now().hour)
     if hour>=0 and hour<12:
          speak("Good Morning!")

     elif hour>=12 and hour<18:
          speak("Good Afternoon!")

     else:
          speak("Good Evening!")

     speak("Its Alice here. how may i help you")

def tellDay():
      
    # This function is for telling the
    # day of the week
    day = datetime.datetime.today().weekday() + 1
      
    #this line tells us about the number 
    # that will help us in telling the day
    Day_dict = {1: 'Monday', 2: 'Tuesday', 
                3: 'Wednesday', 4: 'Thursday', 
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}
      
    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)     

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in') #Using google for voice recognition.
        print(f"User said: {query}\n")  #User query will be printed.

    except Exception as e:
        # print(e)    
        print("Say that again please...")   #Say that again will be printed in case of improper voice 
        speak("Say that again please...")
        return "None" #None string will be returned
    return query  

class Widget:

     def __init__(self):
        root = Tk()
        root.title('Alice')
        root.geometry('520x320')
        compText = StringVar()
        userText = StringVar()
        userText.set('Your Virtual Assistant')
        userFrame = LabelFrame(root, text='Alice', font=('Railways', 24, 'bold'))
        userFrame.pack(fill='both', expand='yes')
        top = Message(userFrame, textvariable=userText, bg='white', fg='black')
        top.config(font=("Century Gothic", 15, 'bold'))
        top.pack(side='top', fill='both', expand='yes')
        btn = Button(root, text='Speak', font=('railways', 10, 'bold'), bg='red', fg='white', command=self.clicked).pack(fill='x', expand='no')
        btn2 = Button(root, text='Close', font=('railways', 10, 'bold'), bg='yellow', fg='black', command=root.destroy).pack( fill='x', expand='no')
        wishme() 
        root.mainloop()
     
     def clicked(self):
          #while true:
          query = takeCommand().lower()

          if 'who is' in query:
               speak('Searching Wikipedia...')
               results = wikipedia.summary(query, sentences=1) 
               speak("According to Wikipedia")
               print(results)
               speak(results)       
          elif 'open youtube' in query:
               web.open(f"youtube.com")       
          elif 'open google' in query:
               speak("sir, what should i search on google")
               cm = takeCommand().lower()
               web.open(f"{cm}")       
          elif 'play music' in query:
               n = random.randint(0,199)
               print(n)
               music_dir ='F:\\rudra internal'
               songs = os.listdir(music_dir)
               os.startfile(os.path.join(music_dir, songs[n]))       
          elif 'youtube' in query:
               speak("sir, what should i search on youtube")
               cf = takeCommand().lower()
               kit.playonyt(cf)       
          elif 'the time' in query:
               strTime = datetime.datetime.now().strftime("%H:%M:%S")
               speak(f"current time is {strTime}")
               print(strTime)               
          elif 'joke' in query:
               speak(pyjokes.get_joke())       
          elif 'stop' in query:
               speak("thanks for using us, have a good day")
               sys.exit()           
          elif 'open visual studio' in query:
               vscode = "C:\\Users\\ANJALI\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"  
               os.startfile(vscode)       
          elif 'temperature' in query:
               tem =takeCommand().lower()
               search = "temperature in kolkata"
               url = f"https://www.google.com/search?q={search}"
               t = requests.get(url)
               data = BeautifulSoup(t.text,"html.parser")
               temp = data.find("div",class_="BNeawe").text
               speak(f"current {search} is {temp}")         
          elif 'play song on youtube' in query:
               speak("please tell me the song name")
               s = takeCommand().lower()
               kit.playonyt(f"{s}")            
          elif 'open chrome' in query:
               ch = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"   
               os.startfile(ch)
          
          elif 'my location' in query:
               location = takeCommand('What is your location?')
               url = 'https://google.nl/maps/place/' + location + '/&amp;'
               web.get().open(url)
               speak('Here is location' + location)       
          elif 'which day it is' in query:
               tellDay()       
          elif 'you are looking beautiful' in query:
               speak("haha, thanks for your complement, by the way you are looking handsome too ")       
          elif 'open torrent' in query:
               tor = "C:\\Users\\ANJALI\\AppData\\Roaming\\uTorrent\\uTorrent.exe" 
               os.startfile(tor)       
          elif 'open spotify' in query:
               sp = "C:\\Users\\ANJALI\\AppData\\Roaming\\Spotify\\Spotify.exe" 
               os.startfile(sp)            
          elif 'open whatsapp web' in query:
               web.open(f"https://web.whatsapp.com/")
          elif 'temprorary email' in query:
               web.open(f"https://temp-mail.org/en/")

if __name__== '__main__':
     widget = Widget()
          
                
                       
          
             
             
     

