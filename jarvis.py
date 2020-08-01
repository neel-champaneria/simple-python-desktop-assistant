import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import random
import os
import smtplib

# Microsoft sapi5 api for voice
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
#print(voices[1].id)
engine.setProperty('voice',voices[0].id)

# Setting chrome as a browser for webbrowser library
webbrowser.register('chrome',None,webbrowser.BackgroundBrowser("C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"))

# Creating dictionary for mail.
email_dictionary={
    "neel":"email address",
    "champaneria":"email address"
}

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

    speak("I am A.I. Sir. Please tell me how may I help you")

def takeCommand():
    #takes microphone input from user and return string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 900
        r.operation_timeout = 2
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception:
        #print(e)
        print("Say that again please")
        speak("Say that again please")
        return "None"

    return query

def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("sender email","password")
    server.sendmail("receiver email",to,content)
    server.close()

if __name__ == "__main__":
    wishMe()
    #speak("Online Live Learning From College Professor SUCKS")
    if True:
        query = takeCommand().lower()

        #logic for executing task of query
        if 'wikipedia' in query:
            speak("Serching Wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("Hmmmmm")
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.get('chrome').open("youtube.com")

        elif 'open google' in query:
            print("what to search")
            speak("what to search")
            gsearch=takeCommand().lower()
            print(gsearch)
            gslist=gsearch.split(" ")
            gstr="+"
            gstr=gstr.join(gslist)
            search="www.google.com//search?q="+gstr
            webbrowser.get('chrome').open(search)

        elif 'play music' in query:
            music_dir="F:\\Extras\\Jarvis\\Songs"
            songs = os.listdir(music_dir)
            print(songs)
            song_n=len(songs)
            song_n=song_n-1
            while(len(songs)!=0):
                random_song_number=random.randint(0,song_n)
                os.startfile(os.path.join(music_dir, songs[random_song_number]))
                songs.pop(random_song_number)
                song_n=song_n-1

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"The time is {strTime}")
            speak(f"The time is {strTime}")

        elif 'open spotify' in query:
            spotifyPath = "C:\\Users\\LENOVO\\AppData\\Roaming\\Spotify\\Spotify.exe"
            os.startfile(spotifyPath)

        elif 'send email' in query:
            try:
                to=""
                while(len(to)==0):
                    speak("To whome you want to send email ?")
                    print("To whome you want to send email ?")
                    receipt_name=takeCommand().lower()
                    for key,value in email_dictionary.items():
                        if key==receipt_name:
                            to=email_dictionary[key]

                    if(len(to)==0):
                        speak('Unable to find contact in dictionary')
                        print('Unable to find contact in dictionary')
                        speak('Do you want to try again ?')
                        print('Do you want to try again ?')
                        ans=takeCommand().lower()
                        if(ans=='no'):
                            break
                        
                if(len(to)!=0):
                    speak('What should I Write ?')
                    print('What should I Write ?')
                    speak('What should I Write ?')

                    content=takeCommand()
                    sendEmail(to,content)
                    speak("Email has been sent")

            except Exception as e:
                print(e)
                speak("Unable to send email")

