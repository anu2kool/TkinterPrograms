# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 23:13:14 2019

@author: Anukool Dwivedi
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 19:18:56 2019

@author: Anukool Dwivedi
"""
import requests
from bs4 import BeautifulSoup
from googlesearch import search
import subprocess 
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import smtplib
import os
import webbrowser
import sys

engine=pyttsx3.init("sapi5")
voices=engine.getProperty("voices")
print(voices[1].id)
engine.setProperty("voice",voices[1].id)

def WishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<16:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
        
    speak("Hello Anukool , I am hashtagassistant. How may I help you?")

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def Solve(op):
    str1=""
    for i in  op:
        if i=="plus" or i=="add" or i=="Add" or i=="+":
            str1+="+"
        elif i=="minus" or i=="-" or i=="Minus" or i=="Subtract" or i=="subtract":
            str1+="-"
        elif i=="divided by" or i=="divided" or i=="/":
            str1+="/"
        elif i=="multiply by" or i=="x" or i=="into" or i=="multiply":
            str1+="*"
        else:
            str1+=i
    print(eval(str1))
    speak(eval(str1))
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('anukooldwivedi@gmail.com', '#######')
    server.sendmail('anukooldwivedi@gmail.com', to, content)
    server.close()
def Command():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        #r.pause_threshold=1
        audio=r.listen(source,phrase_time_limit=3)
        
    try:
        print("Recognizing")
        query=r.recognize_google(audio,language="en-in")
        print("Anukool said:",query)
        
    except Exception as e:
        print("Sorry,Say again")
        return "None"
    return query

WishMe()
while True:
    if 1:
        
        query=Command().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            speak("What do you want to search")
            search_query=Command()
            speak("Thik hain")
            driver = webdriver.Chrome(executable_path=r"C:/Users/Anukool Dwivedi/Downloads/chromedriver_win32/chromedriver.exe")
            driver.maximize_window()
            
            wait = WebDriverWait(driver, 3)
            presence = EC.presence_of_element_located
            visible = EC.visibility_of_element_located
            
            # Navigate to url with video being appended to search_query
            driver.get("https://www.youtube.com/results?search_query=" + str(search_query))
            
            # play the video
            wait.until(visible((By.ID, "video-title")))
            driver.find_element_by_id("video-title").click()       
                
        
        elif "open google" in query:
            webbrowser.open("https://www.google.com/")
        elif "open coca" in query:
            webbrowser.open("https://www.youtube.com/watch?v=7lWeQs8Firo")
    
        elif "solve maths" in query:
            query=Command()
            Solve(query.split(" "))
            sys.exit()
        elif "day is today" in query:
            speak(datetime.date.today())
        elif "time" in query:
            now = datetime.datetime. now()
            current_time = now. strftime("%H:%M:%S")
            speak(current_time)
        elif "notepad" in query:
            path=r"C:\Users\Anukool Dwivedi\Desktop"
            subprocess.Popen(['notepad.exe', path])
        
        elif "search on google" in query:
            speak("What do you want to search")
            query_search=Command()
            driver = webdriver.Chrome(executable_path=r"C:/Users/Anukool Dwivedi/Downloads/chromedriver_win32/chromedriver.exe")
            driver.get("http://www.google.com")
            que=driver.find_element_by_xpath("//input[@name='q']")
            result=que.send_keys(query_search)
            time.sleep(2)
            print(result)
            que.send_keys(Keys.ARROW_DOWN)
            que.send_keys(Keys.ARROW_DOWN)
            time.sleep(2)
            que.send_keys(Keys.RETURN)
            
           
        
        elif 'email' in query:
            try:
                speak("What should I say?")
                content = Command()
                to = "anukooldwivedi@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Anukool. I am not able to send this email") 
            
        elif "exit" in query:
            sys.exit()

        