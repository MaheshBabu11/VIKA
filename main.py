# importing speech recognition package from google api
import speech_recognition as sr
import playsound # to play saved mp3 file
from gtts import gTTS # google text to speech
import os # to save/open files
import wolframalpha # to calculate strings into formula
from selenium import webdriver # to control browser operations
from twilio.rest import Client
from keylogger import *
from datetime import datetime
from time import ctime
import time
from test_model import *
import random
num = 1
def assistant_speaks(output):
	global num

	# num to rename every audio file
	# with different name to remove ambiguity
	num += 1
	print("PerSon : ", output)

	toSpeak = gTTS(text = output, lang ='en',tld="co.in", slow = False)
	# saving the audio file given by google text to speech
	file = str(num)+".mp3"
	toSpeak.save(file)
	
	# playsound package is used to play the same file.
	playsound.playsound(file, True)
	os.remove(file)
def process_text(input):
	try:
		if 'search' in input or 'play' in input:
			# a basic web crawler using selenium
			search_web(input)
			return

		elif "who are you" in input or "define yourself" in input:
			speak = '''Hello, I am Vika. Your personal Assistant.
			I am here to make your life easier. You can command me to perform
			various tasks such as calculating sums or opening applications etcetra'''
			assistant_speaks(speak)
			return

		elif "who made you" in input or "created you" in input:
			speak = "I have been created by Mahesh ,Sreeraj , Jaya and Jyothi ."
			assistant_speaks(speak)
			return

		elif "geeksforgeeks" in input:# just
			speak = """Geeks for Geeks is the Best Online Coding Platform for learning."""
			assistant_speaks(speak)
			return

		elif "calculate" in input.lower():
			
			# write your wolframalpha app_id here
			app_id = ""
			client = wolframalpha.Client(app_id)

			indx = input.lower().split().index('calculate')
			query = input.split()[indx + 1:]
			res = client.query(' '.join(query))
			answer = next(res.results).text
			assistant_speaks("The answer is " + answer)
			return

		elif "what is the date today" in input  :
			
			assistant_speaks("The time is "+ctime())
			return

		elif 'open' in input:
			
			# another function to open
			# different application availaible
			open_application(input.lower())
			return
			
		elif 'call' in input:
			make_call()
			return
		
		else:

			assistant_speaks("I can search the web for you, Do you want to continue?")
			ans = get_audio()
			if 'yes' in str(ans) or 'yeah' in str(ans):
				search_web(input)
			elif 'no' in str(ans):
				return
			else:
				return
	except :

		assistant_speaks("I don't understand, I can search the web for you, Do you want to continue?")
		ans = get_audio()
		if 'yes' in str(ans) or 'yeah' in str(ans):
			search_web(input)
def search_web(input):

	driver = webdriver.Chrome()
	driver.implicitly_wait(1)
	driver.maximize_window()

	if 'youtube' in input.lower():

		assistant_speaks("Opening in youtube")
		indx = input.lower().split().index('youtube')
		query = input.split()[indx + 1:]
		driver.get("http://www.youtube.com/results?search_query =" + '+'.join(query))
		return

	elif 'wikipedia' in input.lower():

		assistant_speaks("Opening Wikipedia")
		indx = input.lower().split().index('wikipedia')
		query = input.split()[indx + 1:]
		driver.get("https://en.wikipedia.org/wiki/" + '_'.join(query))
		return

	else:

		if 'google' in input:

			indx = input.lower().split().index('google')
			query = input.split()[indx + 1:]
			driver.get("https://www.google.com/search?q =" + '+'.join(query))

		elif 'search' in input:

			indx = input.lower().split().index('google')
			query = input.split()[indx + 1:]
			driver.get("https://www.google.com/search?q =" + '+'.join(query))

		else:

			driver.get("https://www.google.com/search?q =" + '+'.join(input.split()))

		return


def make_call():
	# from twilio console get you account ssid and authorzation token and place it here.
	account_sid = ''
	auth_token =''
	client = Client(account_sid, auth_token)
	assistant_speaks("Contacting your friend , He will soon be in touch with you ")
	call = client.calls.create(
                        twiml='<Response><Say>Hi this is Vika , Mahesh\'s personal assistant. he would like to talk to you can you call him back?</Say></Response>',
                        to='',
                        from_=''
                    )

	print(call.sid)
	return



# function used to open application
# present inside the system.
def open_application(input):

	if "chrome" in input:
		assistant_speaks("Opening Google Chrome")
		os.system("google-chrome")
		return

	elif "firefox" in input or "mozilla" in input:
		assistant_speaks("Opening Mozilla Firefox")
		os.system("firefox")
		return

	elif "wps" in input or "word" in input or "excel" in input or "powerpoint"in input:
		assistant_speaks("Opening WPS")
		os.system("wps")
		return

	elif "vlc" in input:
		assistant_speaks("Opening VLC")
		os.system("vlc")
		return
	
	elif "spotify" in input:
		assistant_speaks("Opening Spotify")
		os.system("spotify")
		return
	
	else:

		assistant_speaks("Application not available")
		return

def predict_sentiment():
	f=open("log.txt","r")
	for i in f:
		output=predict_gpt3(i)
		assistant_speaks(output)
		if output =="Negative":
			make_suggesion()
			break
	return
def get_audio():

	rObject = sr.Recognizer()
	audio = ''

	with sr.Microphone() as source:
		print("Speak...")
		
		# recording the audio using speech recognition
		audio = rObject.listen(source, phrase_time_limit = 5)
	print("Stop.") # limit 5 secs

	try:

		text = rObject.recognize_google(audio, language ='en-US')
		print("You : ", text)
		return text

	except:

		assistant_speaks("Could not understand your audio, PLease try again !")
		return 0

def make_suggesion():

# this is a list of video and audio linke scrapped from youtube , these links contains videos that provide emotional support.

	collection=['https://youtu.be/kbT7oYagkOY', 'https://youtu.be/-ESQmzDbnL8', 'https://youtu.be/_YovRE-Pk3c', 'https://youtu.be/wKgHvlrv5gg', 'https://youtu.be/fJQ5_9UwujI', 'https://youtu.be/ae5B4k-LhKs', 'https://youtu.be/BRXenN6Kp8o', 'https://youtu.be/61YEdGZrqSc', 'https://youtu.be/azq0S0DKS50', 'https://youtu.be/qv1afUOxfwU', 'https://youtu.be/ssKSfQmIoLE', 'https://youtu.be/_re6AX3Mi4s', 'https://youtu.be/L2dguyFo82w', 'https://youtu.be/7bvF3sOlx5g', 'https://youtu.be/ZLVwjkIz-Mc', 'https://youtu.be/48H7FkH7EeQ', 'https://youtu.be/-6XkpBd62P0', 'https://youtu.be/LPRbW9xQ42Y', 'https://youtu.be/z7dxYB5enOQ', 'https://youtu.be/2smGF2zZM5U', 'https://youtu.be/J7ZQl4e6A4w', 'https://youtu.be/-qqtzG3amMk', 'https://youtu.be/df4IUMTVDOI', 'https://youtu.be/yBrRpb8aLwk', 'https://youtu.be/MOiaSc38ZeI', 'https://youtu.be/4r8YPji277Y', 'https://youtu.be/_u2qggffbYM', 'https://youtu.be/W5tlGJwvmCQ', 'https://youtu.be/a1Y1ocyudjs', 'https://youtu.be/tbnzAVRZ9Xc', 'https://youtu.be/dy02o7MW3VA', 'https://youtu.be/sW9vMExhgtA', 'https://youtu.be/hKfC8zX39UQ', 'https://youtu.be/xKIqF2PJXJY', 'https://youtu.be/4oN5JShOs2I', 'https://youtu.be/aqqJKzgUfR0', 'https://youtu.be/a9m4TzR0COU', 'https://youtu.be/k55JDiev8Mc', 'https://youtu.be/HhBNGdS5Kqk', 'https://youtu.be/CpDnwZWJq0U', 'https://youtu.be/1I9ADpXbD6c', 'https://youtu.be/3SDkzDlw1yc', 'https://youtu.be/lL-0TGtzEmQ', 'https://youtu.be/zD0XKGLh_Eo', 'https://youtu.be/DQC2eRUilUM', 'https://youtu.be/O4pktIaZvos', 'https://youtu.be/tBGvOmUhhq4', 'https://youtu.be/NkiS_f5YXGQ', 'https://youtu.be/Mibx6MAGSxI', 'https://youtu.be/Z63w5PefxTQ', 'https://youtu.be/B8Hjld6xSzY', 'https://youtu.be/EpOMk1jOzgk', 'https://youtu.be/tj7utbR4rMc', 'https://youtu.be/3wi65UW_nJk', 'https://youtu.be/WVhh0X4CGiA', 'https://youtu.be/_OHDssbQPlY', 'https://youtu.be/t1XCzWlYWeA', 'https://youtu.be/Vw1_AEaoXtM', 'https://youtu.be/XQAn3Vwdrqs', 'https://youtu.be/G9cSbZjl8ko', 'https://youtu.be/5T5nWBoilqE', 'https://youtu.be/NHf56w1AmPw', 'https://youtu.be/HQmVaP_0lBE', 'https://youtu.be/z-AoS_4ojYI', 'https://youtu.be/hOdtpCZp7TA', 'https://youtu.be/8SN9Kj8SdgE', 'https://youtu.be/eSH7QSzkhQg', 'https://youtu.be/3rj8tNBn18s', 'https://youtu.be/CfvYlWG1cA0', 'https://youtu.be/3uiY0P0ul_Y', 'https://youtu.be/-5mCnDPPhws', 'https://youtu.be/QT2KNvzovHM', 'https://youtu.be/COQqd8u4KS0', 'https://youtu.be/_UtDMmx-Ouc', 'https://youtu.be/pFfSf_gKPv0', 'https://youtu.be/jgJ1d0Ugx8o', 'https://youtu.be/ga-MniJxQz8', 'https://youtu.be/EUoKyjBIoE8', 'https://youtu.be/Y9A5wuTtblw', 'https://youtu.be/h-3nt92UFZo', 'https://youtu.be/Hsdb4KZBUeU', 'https://youtu.be/DwA6Olfz8do', 'https://youtu.be/Gljq2FHzTvY', 'https://youtu.be/2D5mTV7HekE', 'https://youtu.be/fvGw8tnDQkw', 'https://youtu.be/S7CPXI7Z28g', 'https://youtu.be/chE00kGtg48', 'https://youtu.be/ft_DXwgUXB0', 'https://youtu.be/UrfpkvvRTns', 'https://youtu.be/Xm_2zmX6Akc', 'https://youtu.be/HBXMGaF6v1s', 'https://youtu.be/eAK14VoY7C0', 'https://youtu.be/WsQD0quPFRY', 'https://youtu.be/d96akWDnx0w', 'https://youtu.be/qa2HiWOQauM', 'https://youtu.be/WWloIAQpMcQ', 'https://youtu.be/NUhrPbDGKSA', 'https://youtu.be/0Znvum3WikA', 'https://youtu.be/SF4jUqPmVfI', 'https://youtu.be/lHYo8YvhgkM', 'https://youtu.be/-GXfLY4-d8w', 'https://youtu.be/CFiSFqmo6f0', 'https://youtu.be/5nlSXhMBP8c', 'https://youtu.be/X9JExlvPwcs', 'https://youtu.be/ykvC3QXJb18']

	assistant_speaks("It seems that you are depressed ,  would you like me to contact your friends?")
	text = str(get_audio().lower())	
	if "yes" in text or "yeah" in text:
		make_call()
	elif "no" in text:
		vid=random.choice(collection)
		driver = webdriver.Chrome()
		assistant_speaks("Opening a video to refresh your mood ,  chill out"+name)
		driver.maximize_window()
		driver.get(vid)
		video_is_playing = True
		while video_is_playing:
			time.sleep(1)
			video_is_playing = player_status = driver.execute_script("return document.getElementById('movie_player').getPlayerState()")
		

	return




# Driver Code
if __name__ == "__main__":
	assistant_speaks("Hi my name is Vika , your personal assistant . What's your name?")
	name ='Human'
	name = get_audio()
	assistant_speaks("Hello, " + name + '.')
	
	while(1):

		assistant_speaks("What can i do for you?")
		text = get_audio().lower()

		if text == 0:
			continue

		if "exit" in str(text) or "bye" in str(text) or "sleep" in str(text):
			assistant_speaks("Ok bye, "+ name+'.')
			keylogger()
			time.sleep(20)
			predict_sentiment()
			assistant_speaks("done")	
			break

		# calling process text to process the query
		process_text(text)

