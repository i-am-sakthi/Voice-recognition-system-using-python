#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import _thread
def validate_time(alarm_time):
                if len(alarm_time) != 11:
                    speak("Invalid time format!, hint:check spaces between them. Please try again...")
                    return "Invalid time format!,hint:check spaces between them. Please try again..."
        
                else:
                    if int(alarm_time[0:2]) > 12:
                        speak("Invalid HOUR format! Please try again...")
                        return "Invalid HOUR format! Please try again..."
                   
                    elif int(alarm_time[3:5]) > 59:
                        speak("Invalid MINUTE format! Please try again...")
                        return "Invalid MINUTE format! Please try again..."
            
                    elif int(alarm_time[6:8]) > 59:
                        speak("Invalid SECOND format! Please try again...")
                        return "Invalid SECOND format! Please try again..."
            
                    else:
                        speak("ok")
                        return "ok"

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Alexis. Please tell me how may I help you")       

def takeCommand():
   
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('', 'soxualqrdgixqmkn') #our gmail id
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

      
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play music' in query:
            music_dir = '' # music folder
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "" # this project Code path
            os.startfile(codePath)

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = ""  # receiver mail id
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry chief. I am not able to send this email")
       
        elif 'who are you' in query:
            speak(' im Alexis , your personal search engine created by you. for now i can do some wikipedia searches , play some songs , opening google , youtube , can inform you time, say weather forcast . and i can send email but thats currently being in development')
            
        elif 'love' and 'you' in query:
            speak('sorry i got boyfriend and i curse you not to get married till end of your life')
            
        elif 'insult'  in query:
            print("What is his name? ")
            speak("What is his name? ")
            name = input("Name: ")
            

            print("What is your age, " + name + "?")
            speak("What is your age, " + name + "?")
            age = int(input("Age: "))

              
            from random import choice
            def printInsult (name, age):
            
                adjectives = ["big", "poopy", "dumb", "silly", "stinky", "cranky", "weird", "trashy"]
                nouns = ["turnip", "dog", "fart", "hairball", "chicken", "wet-wipe", "hag", "whale"]
                if(age < 16):
                    ageA = "young "
                    a = print (name + ", you are a " + ageA + choice(adjectives) + " " + choice(nouns))
                    speak(a)
                else:
                    ageA = "old "
                    a = print (name + ", you are an " + ageA + choice(adjectives) + " " + choice(nouns))
                    speak(a)
            printInsult(name, age)
            
            
            
        elif 'good night' in query:
            speak('good night partner!, have lovely dreams without me')
            
        elif 'remind' in query:
            import time
            speak('what should i remind you about')
            remaind_content = takeCommand()
            txt=(remaind_content)
            speak('in how many minutes?')
            local_time = float(input())
            Local_time = local_time * 60
            time.sleep(Local_time)
            speak("you have a remainder!, i will say what u said")
            speak(txt)
            
        elif 'weather' in query:
            import json
            import time
            import urllib.request

            API="tH5WhRG3qk9D4wJwCkhNF4rA0dO7GjFc"
            countryCode="IN"
            city=input("City Name")

            key="tH5WhRG3qk9D4wJwCkhNF4rA0dO7GjFc"

            def getLocation(countryCode,city):
                search_address="http://dataservice.accuweather.com/locations/v1/cities/"+countryCode+"/search?apikey=tH5WhRG3qk9D4wJwCkhNF4rA0dO7GjFc&q="+city+"&details=true&offset=0"
                    # print(search_address)
                with urllib.request.urlopen(search_address)as search_address:
                    data=json.loads(search_address.read().decode())
                #print(data)
                location_key=data[0]['Key']
                return(location_key)

            def getForcast(location_key):
                daily_forcastUrl="http://dataservice.accuweather.com/forecasts/v1/daily/5day/"+location_key+"?apikey=tH5WhRG3qk9D4wJwCkhNF4rA0dO7GjFc&details=true"
                with urllib.request.urlopen(daily_forcastUrl)as daily_forcastUrl:
                    data=json.loads(daily_forcastUrl.read().decode())
                for key1 in data['DailyForecasts']:
                    print("weather forcast for "+key1['Date'])
                    print("Min Temp(in F):"+str(key1['Temperature']['Minimum']['Value']))
                    print("Max Temp(in F):"+str(key1['Temperature']['Maximum']['Value']))
                    print("day forcast:"+str(key1['Day']['ShortPhrase']))
                    speak("weather forcast for "+key1['Date'])
                    speak("day forcast:"+str(key1["Day"]["ShortPhrase"]))
                    speak("Minimum temperature(in fahrenheit):"+str(key1['Temperature']['Minimum']['Value']))
                    speak("Maximum temperature(in fahrenheit):"+str(key1['Temperature']['Maximum']['Value']))
                    print("----------------------------------------------------------------------------------------------")
        
            key=getLocation(countryCode,city)
            getForcast(key)
            
        elif 'joke' in query:
             import pyjokes
  
             My_joke = pyjokes.get_joke(language="en", category="neutral")

             print(My_joke)
             speak(My_joke)
     
        elif 'alarm' in query:
            
            from datetime import datetime   
            from playsound import playsound 
            
            while True:
                speak("Enter time in hour , minutes, seconds and AM or PM format")
                alarm_time = input("Enter time in 'HH:MM:SS AM/PM' format: ")
   
    
                validate = validate_time(alarm_time.lower())
                if validate != "ok":
                     print(validate)
                else:
                    print(f"Setting alarm for {alarm_time}...")
                    speak(f"Setting alarm for {alarm_time}...")
                    break

            alarm_hour = alarm_time[0:2]
            alarm_min = alarm_time[3:5]
            alarm_sec = alarm_time[6:8]
            alarm_period = alarm_time[9:].upper()
           
            def alarm (mn):
                
                while True:
                    now = datetime.now()
                    current_hour = now.strftime("%I")
                    current_min = now.strftime("%M")
                    current_sec = now.strftime("%S")
                    current_period = now.strftime("%p")
                    if alarm_period == current_period:
                        if alarm_hour == current_hour:
                            if alarm_min == current_min:
                                if alarm_sec == current_sec:
                                    speak('alarm time up!')
                                    print("Wake Up!")
                                    playsound('') # alarm tone filepath in wav format
                                    break
                print(mn)

