import pyaudio
import subprocess
import pyttsx3
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
from googlesearch import search
from bs4 import BeautifulSoup
import pyjokes
import pyttsx3
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser
import os 
from time  import sleep
import winshell
import pylint
import smtplib
import getpass
import re
import sys
from random import randint
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.webdriver.common.keys import Keys 
from selenium.webdriver.common.by import By 
import psutil 
import time 
import screen_brightness_control as sbc


engine = pyttsx3.init() # object creation
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning !")
		print('J:Good Morning !')
	elif hour>= 12 and hour<18:
		speak("Good Afternoon !") 
		print("J:Good Afternoon !")

	else:
		speak("Good Evening !")
		print("J:Good Evevning !")

	assname =("Jarvis 1 point o")
	speak("I am your Assistant")
	print("J: I am your Assistant")
	print("J: Jarvis 1 point o")
	speak(assname)

	
def speakstory():
	#number = random.randint(0,4)
	number = '1'
	storyName = 'ShortStory-'+str(number)+'.txt'
	f = open(storyName,"r",encoding="utf8")
	string1=f.read()
	f.close()
	speak(string1)

def takeCommand():
	r = sr.Recognizer()
	with sr.Microphone() as source:
		print("				<--Listening-->")
		r.pause_threshold = 1
		audio = r.listen(source)
	try:
		print("				<-Recognizing-->") 
		query = r.recognize_google(audio, language ='en-in')
		print(f"						You said: {query} <-")
	except Exception as e:
		print(e) 
		print("J:Unable to Recognize your voice.") 
		return "None"
	return query

def sendEmail(to,content):
	smtp_obj = smtplib.SMTP('smtp.gmail.com',587)
	smtp_obj.ehlo()
	smtp_obj.starttls()

	email = 'lilysingh081@gmail.com'
	password =input('Enter password: ')
	#iriggfbjuclgjdle
	smtp_obj.login(email,password)
	from_add = email
	to_add = to
	subject = 'Py'
	message = content
	msg = "Subject:"+ subject +'\n' + message
	smtp_obj.sendmail(from_add,to_add,msg)

def whatsapp(to,message):
	person =[to]
	string= message
	chrome_driver_binary = "C:\\Program Files\\Google\\Chrome\\Application\\chromedriver.exe"
	driver=webdriver.Chrome(chrome_driver_binary)   # Selenium chromedriver path
	driver.get("https://web.whatsapp.com/")
	#wait = WebDriverWait(driver,10) 
	sleep(15)
	for name in person:
		print('IN')
		user = driver.find_element_by_xpath("//span[@title='{}']".format(name))
		user.click()
		print(user)
		for _ in range(10):
			text_box = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
			text_box.send_keys(string)
			sendbutton = driver.find_elements_by_xpath('//*[@id="main"]/footer/div[1]/div[3]/button')[0]
			sendbutton.click()

if __name__ == "__main__":
	
	print("+----------------------------------------------------------------------------+")
	print("      			~ Welcome to JARVIS ~")
	print("+----------------------------------------------------------------------------+")
	wishMe()
	speak("Hey there, How can I help you")
	print("J: Hey there, How can I help you")
	while True :
		query = takeCommand().lower()
# Open using web browser (just documenting the code)
		if  'open youtube' in query:
			print("* J: Here you go to Youtube")
			speak("Here you go to Youtube")
			webbrowser.open("youtube.com")
		elif 'open google' in query:
			speak("Here you go to Google")
			print("* J: Here you go to Google \n")
			webbrowser.open("google.com")	
		elif 'open stackoverflow' in query:
			speak("Here you go to Stack Over flow.Happy coding")
			print("* J: Here you go to stackoverflow ")
			webbrowser.open("stackoverflow.com") 
		elif "wikipedia" in query:
			print("* J: Here you go to wikipedia")
			webbrowser.open("wikipedia.com")
		elif 'search for' in query:
			x=re.search('search for',query)
			speak("Finding results")
			print("J: Finding results\n")
			query=query[x.start()+10:]
			for j in search(query,tld="co.in",num=1, stop=1):
				print(j)
				webbrowser.open(j)
		elif 'news' in query:
			speak('here are some top news from the times of india')
			print('J: Here are some top news from the times of india')
			webbrowser.open("https://timesofindia.indiatimes.com/india") 
			
# STORY
		elif 'tell me a story' in query:
			speak("Reading a story book")
			content=takeCommand()
			speakstory()
# PLAY MOVIE
		elif 'play movie' in query:
			speak("Playing your playlist sir")
			print("J: Playing your playlist sir")
			music_dir = "D:\\User Data\\Movies\\Shaadi Mein Zaroor Aana 2017"
			songs = os.listdir(music_dir)
			random = os.startfile(os.path.join(music_dir, songs[0]))

# MAIL
		elif 'mail' in query or 'email' in query:
			try:
				print("J: What should I say?")
				speak("What should I say?")
				content = takeCommand()
				print("J: To whom should i send? Can you please type the email.")
				speak("To whom should i send? Can you please type the email.")	
				to = input("J:  Enter the email here: ") 
				sendEmail(to, content)
				speak("Email has been sent !")
				print("* J: Email has been sent !")
			except Exception as e:
				print(e)
				speak("I am not able to send this email")	
# WHATSAPP
		elif 'whatsapp' in query:
			try:
				print("J: To whom should i send? Can you please type in the name.")
				speak("To whom should i send? Can you please type in the name.")
				to = input('Name: ')
				print("J: What should i send? Can you please type in the message.")
				speak("What should i send? Can you please type in the message.")
				content = input("Enter the message: ") 
				speak('You will have to scan for whatsapp web. ')
				print('J: You will have to scan for whatsapp web. ')
				whatsapp(to, content)
				speak("Message has been sent !")
				print("* J: Message has been sent !")
			except Exception as e:
				print(e)
				speak("I am not able to send this message")	
# RANDOM Qs
		elif "Good Morning" in query:
			print("J: A warm" +query)
			print("J:  How are you Mister")
			speak("A warm" +query)
			speak("How are you Mister")
			

		elif "will you be my gf" in query or "will you be my bf" in query: 
			print("J: I'm not sure about, may be you should give me some time")
			speak("I'm not sure about, may be you should give me some time")


		elif "how are you" in query:
			print("J: I'm fine, glad you thought of me !")
			speak("I'm fine, glad you thought of me!")


		elif "i love you" in query:
			speak("It's hard to understand , but I love you too !")
			print("J: It's hard to understand , but I love you too !")

		elif 'the time' in query:
			strTime = datetime.datetime.now()
			speak(f"Sir, the time is {strTime}")
			print(f"J: Sir, the time is {strTime}")

		elif 'jarvis' in query:
			speak("Jarvis 1 point o in your service Mister")
			print("J: Jarvis 1 point o in your service Mister")

		elif 'how are you' in query:
			print("J: I am fine, Thank you")
			speak("I am fine, Thank you")
			print("J: How are you, Sir")
			speak("How are you, Sir")
			

		elif 'fine' in query or "good" in query:
			speak("It's good to know that your fine")
			print("J: It's good to know that your fine")

		elif "what's your name" in query or "What is your name" in query:
			speak("My friends call me Jarvis")
			print("J: My friends call me Jarvis")

		elif "who made you" in query or "who created you" in query:
			print("J: I have been created by Vaishnavi, Bhavya and Dhruvin") 
			speak("I have been created by Vaishnavi, Bhavya and Dhruvin")

			
		elif 'joke' in query:
			speak(pyjokes.get_joke())
			print('J: '+ pyjokes.get_joke())

		elif "who am I" in query:
			speak("If you talk then definately your human.")
			print("J: If you talk then definately your human.")

		elif "why did you came to this world" in query:
			speak("Thanks to TLE. further It's a secret")
			print("J: Thanks to TLE. further It's a secret")
		elif 'is love' in query:
			speak("It is 7th sense that destroy all other senses")
			speak("J: It is 7th sense that destroy all other senses")
		elif "who are you" in query:
			print("J: I am Jarvis Your virtual assistant")
			speak("I am Jarvis Your virtual assistant")
			
#EMPTY BIN
		elif 'empty recycle bin' in query:
			winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
			speak("Recycle Bin Recycled")
			print("* J: Recycle Bin Recycled")
#DONT LISTEN
		elif "don't listen" in query or "stop listening" in query:
			speak("for how much time you want to stop jarvis from listening commands")
			a = int(takeCommand())
			sleep(a)

# LOCATION
		elif "where is" in query:
			query = query.replace("where is", "")
			location = query
			print("J: You asked me to Locate",end=' ')
			speak("You asked me to Locate")
			speak(location)
			print(location)
			webbrowser.open("https://www.google.com/maps/place/"+ location +"")
# NOTES
		elif "write a note" in query:
			speak("What should i write, sir")
			print("J: What should i write, sir")
			note = takeCommand()
			file = open('jarvis.txt', 'w')
			speak("Sir, Should i include date and time")
			print("J: Sir, Should i include date and time")
			snfm = takeCommand()
			if 'yes' in snfm or 'sure' in snfm:
				strTime = datetime.datetime.now()
				file.write(strTime)
				file.write(" :- ")
				file.write(note)
			else:
				file.write(note)		
		elif "show the note" in query:
			speak("Showing Notes")
			print("J: Showing Notes")
			file = open("jarvis.txt", "r") 
			print(file.read())
			speak(file.read(6))

# BRIGHTNESS
		elif "brightness" in query:
			print('J: How much brightness do you want to set it at')
			speak('How much brightness do you want to set it at')
			number = takeCommand()
			sbc.set_brightness(number)
			speak('Brightness has been set')
			print('* J:Brightness has been set')
# BATTERY
		elif "battery" in query:
			battery = psutil.sensors_battery() 
			percent = battery.percent
			batterypercent=str(percent)+"% Battery remaining"
			speak(batterypercent)
			print('J:'+ batterypercent)
			if percent <=10:
				speak('Please plug in the laptop')
# EXIT		
		elif 'exit' in query or 'quit' in query or 'bye' in query:
			speak('Exiting sir ! Have a nice day !')
			print("Exiting sir! Have a nice day !")
			exit()
		else:
			speak('I love listening to you, but please command me to do something.')
			print('J: I love listening to you, but please command me to do something.')