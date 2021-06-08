import pyttsx3#pip install pyttsx3
import datetime
import speech_recognition as sr # pip install SpeechRecognition
import wikipedia # pip install wikipedia
import smtplib
import webbrowser as wb
import pyjokes 
import os
import pyautogui
import random
import json
import requests
from urllib.request import urlopen
import wolframalpha
import time




engine=pyttsx3.init()
wolframalpha_app_id = 'XY8LJA-V9XYYWE99L'

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time_():
    Time=datetime.datetime.now().strftime("%I:%M:%S")# %H for 24 hours %I for 12 hours
    speak("The current time is")
    speak(Time)

def date_():
    year=datetime.datetime.now().year
    month=datetime.datetime.now().month
    date=datetime.datetime.now().day
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("welcome back harsha")
    time_()
    date_()
    #greetings
    hour=datetime.datetime.now().hour

    if hour>=4 and hour<12:
        speak("Good morning harsha!")
    elif hour>=12 and hour<18:
        speak("Good afternoon harsha!")
    elif hour>=18 and hour<19:
        speak("Good evening harsha!")
    else:
        speak("good night harsha!")
    speak("Siri at your service. Please tell me how can i help you today!")

def TakeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing......")
            query=r.recognize_google(audio,language='en-US')
            print(query)

        except Exception as e:
            print(e)
            print("Say that again please....")
            return "None"
        return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587) # 587 is the port for gmail
    server.ehlo()
    server.starttls()
    # you must enable low security in ur gmail to function this
    
    server.login('username@gmail.com','password')
    server.sendmail('username@gmail.com',to,content)
    server.close()

def joke():
    jk=pyjokes.get_joke()
    print(jk)
    speak(jk)

def screenshot():
    img = pyautogui.screenshot()
    # name = datetime.datetime.now()
    img.save('C:/Users/Harsh/Desktop/screenshot.png')
    speak('screenshot saved')
    print('Screenshot saved')

if __name__ == "__main__":
    
    wishme()

    while True:
        query = TakeCommand().lower()
        # all commands will be stored in lower case
        #for every recognization

        if 'time' in query:  #tells us time
            time_()
        elif 'date' in query: #tells us date
            date_()
        elif 'wikipedia' in query:
            speak('Searching...')
            query=query.replace('wikipedia','')
            result=wikipedia.summary(query,sentences=2)
            speak('According to Wikipedia')
            print(result)
            speak(result)
        elif 'send email' in query:
            try:
                speak('What should i say')
                content=TakeCommand()
                #provide recivers email address
                speak('who is reciver')
                reciver=input('enter reciver email :')
                to=reciver
                sendEmail(to,content)
                speak(content)
                speak('Email has been sent')
            except Exception as e:
                print(e)
                speak('Unable to send Email')
                print('Unable to send Email')
        elif 'search in chrome' in query:
            speak('What should i search?')
            chromepath='C:/Program Files/Google/Chrome/Application/chrome.exe %s'
            #chromepath is location of chrome installation in computer

            search = TakeCommand().lower()
            wb.get(chromepath).open_new_tab(search+'.com')  #only opens websites having .com at end

        elif 'search youtube' in query:
            speak('What should i search?')
            search_Term = TakeCommand().lower()
            speak('here we go to youtube!!')
            wb.open('https://www.youtube.com/results?search_query='+search_Term)

        elif 'search google' in query:
            speak('What should i search?')
            search_Term = TakeCommand().lower()
            speak('Searching...')
            wb.open('https://www.google.com/search?q='+search_Term)

        elif 'joke' in query:
            joke()
        
        elif 'go offline' in query:
            speak('Going offline Sir')
            quit()
        elif 'write a note' in query:
            speak('What should i note')
            print('What should i note')
            notes = TakeCommand()
            speak('tell the name of the file to save')
            print ('tell the name of the file to save')
            name = TakeCommand()
            file = open(name+'.txt','w')
            speak('sir should i include date and time')
            ans = TakeCommand()
            if 'yes' in ans or 'sure' in ans:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                file.write(strTime)
                file.write(':-')
                file.write(notes)
                speak('done taking notes, Sir')
            else:
                file.write(notes)
        elif 'show note' in query:
            speak('tell the note name')
            name = TakeCommand()
            speak('showing notes')
            file = open(name+'.txt','r')
            print(file.read())
            speak(file.read())
        elif 'screenshot' in query:
            screenshot()

        elif 'play music' in query:
            songs_dir='C:/Users/harsh/Music/songs'
            music = os.listdir(songs_dir)
            speak('what should i play')
            speak('select a number')
            ans = TakeCommand().lower()
            # while(ans != 'random' and ans != 'you choose' ):
            #     speak('I could not understand you. Please try again.')
            #     ans = TakeCommand().lower()
            if 'number' in ans:
                no = int(ans.replace('number',''))
            if 'random' or 'you choose' in ans:
                no = random.randint(1,50)
            os.startfile(os.path.join(songs_dir,music[no]))

        elif 'remember that' in query:
            speak('What should i remember?')
            memory = TakeCommand()
            speak("you asked me to remember that"+memory)
            remember = open('memory.txt','w')
            remember.write(memory)
            remember.close()

        elif 'do you remember anything' in query:
            remember =open('memory.txt','r')
            speak('you asked me to remember that')
            speak(remember.read())        
        
        elif 'news' in query:
            try:
                jsonobj = urlopen("http://newsapi.org/v2/top-headlines?country=us&category=business&apiKey=a9913e1c6354499bb58554bf8d27a367")
                data = json.load(jsonobj)
                i = 1

                speak('Here are some top headlines from bussiness field')
                print('***************TOP HEADLINES***************'+'\n')
                for item in data['articles']:
                    if(i==6):
                        break
                    print(str(i)+'. '+item['title']+'\n')
                    print(item['description']+'\n')
                    speak(item['title'])
                    i+=1
            except Exception as e:
                print(str(e))

        elif 'where is' in query:
            query = query.replace('where is','')
            location = query
            speak('user asked to locate'+ location) 
            wb.open_new_tab("http://www.google.com/maps/place/"+location)  

        # elif 'calculate' in query:
        #     client = wolframalpha.Client(wolframalpha_app_id)
        #     indx = query.lower().split().index('calculate')
        #     query = query.split()[indx + 1:] 
        #     res = client.query(''.join(query))
        #     answer = next(res.results).text
        #     print('the answer is : '+answer)
        #     speak('the answer is : '+answer) 

        elif 'stop listening' in query:
            speak('for how many seconds you want me to stop listining to your commands')
            ans = int(TakeCommand())
            time.sleep(ans)
            print(ans) 
        
        elif 'who are you' in query or 'who are u' in query:
            speak('Hello sir I am siri 1.0 your desktop assistance!! how can i help you')

        elif 'who am i' in query:
            speak('you are able to speak   . Of course you should be human')
           