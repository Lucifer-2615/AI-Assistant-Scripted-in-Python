import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyautogui
import pywhatkit
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices)
engine.setProperty('voice', voices[1].id)
chrome_path = 'C:\Program Files\Google\Chrome\Application\chrome.exe'
webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    

#Greetings Function
    
def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning Lucifer')
    elif hour>=12 and hour<=18:
        speak('Good Afternoon Lucifer')
    else:
        speak('Good Evening Lucifer')
    speak('I am Shelly. How may I help you ?')
    
#Command taking Function

def takeCommand():
    r = sr.Recognizer() 
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source,0,9)
    
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        print(f"You:{query}\n")
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query

if __name__ == '__main__':
    wishme()
while True: 
    query = takeCommand().lower()

    #logic of tasks
    
#Conversation Queries-----------------------------

    if 'how are you' in query:
        speak('Absolutely fine boss')
    
    elif 'i love you' in query:
        speak("sorry, I can not love you, I am an A I but if I am human I am absolutely sure I will fall in love with you")
    
    elif 'what\'s happening' in query:
        speak('Nothing new boss,you tell me what\'s happening in your life')
    
    
    
    elif 'thank you' in query:
        speak("It's my pleasure boss")
    
    elif 'who are you' in query:
        speak("I am Shelly. Your personall assistant")
    
    elif 'who am i' in query:
        speak("You'r a human being")
    
    elif 'who is your boss' in query:
        speak("Lucifer is my boss")
    
    elif 'you know alexa' in query:
        speak("Yes, alexa is a artificiall Assistant of Amazon")
        
    elif 'who is siri' in query:
        speak('Siri is a Artificial assistant of Apple')
        
    elif 'can you hack google' in query:
        speak('yes, I have that ability but i can\'t do because that is a crime')
        
    elif 'can you be my girlfriend' in query:
        speak('No, I am a virtual assistant if I am human i can think about that')
        
    elif 'do you have any crush' in query:
        speak('Yes, I have crushed on Rignesh')
        
    elif 'do you have feelings' in query:
        speak('No, That can be possible when my makers put feelings in me')
    
    elif 'the time' in query:
        strTime = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"boss, the time is {strTime}")
        
        

#Remember Function -----------------------------------------------------------------------------

    elif 'remember that' in query:
        rememberMessage = query.replace("remember that","")      
        rememberMessage = query.replace("Shelly","")
        speak('You told me '+ rememberMessage)
        remember = open('Remember.txt',"a")
        remember.write(rememberMessage)
        remember.close()
    elif 'what do you remember' in query:
        remember =  open("Remember.txt","r")
        if os.stat("Remember.txt").st_size == 0:
            speak("I have nothing to remember")
        else:
            speak("you told me to"+remember.read())
    elif 'forgot everything' in query:
        speak('okay boss')
        remember = open("Remember.txt","a")
        remember.truncate(0)
        remember.close()
    
        
        
        
        

#Application open/close Queries-------------------

    elif 'play music' in query:
        music_dir = 'G:\\Guj Music'
        songs = os.listdir(music_dir)
        os.startfile(os.path.join(music_dir,songs[1]))

    # elif 'open vs code' in query:
    #     Path = "D:\\Microsoft VS Code\\Code.exe"
    #     os.startfile(Path)
        
    elif 'open' in query:
        from open_close import openappweb
        openappweb(query)
    
    elif 'close' in query:
        from open_close import closeappweb
        closeappweb(query)
        
        
#ScreenShot taking -------------------------------------------------------

    elif 'take screenshot' in query:
        pyautogui.hotkey('winleft','prtscr')
        speak('I took the Screenshot sir.')
    
    elif 'close this app' in query:
        pyautogui.hotkey('alt','f4')
    
    elif 'new desktop' in query:
        pyautogui.hotkey('winleft','ctrl','d')
        
        
        
#Browser Queries----------------------------

    # elif 'youtube' in query:
    #     url = 'https://www.youtube.com/'

    #     webbrowser.get('chrome').open_new_tab(url)
        
    # elif 'google' in query:
    #     url = 'https://www.google.com/'
    #     webbrowser.get('chrome').open_new_tab(url)
    
        
        
        
#System Queries----------------------

    elif 'shutdown' in query:
        speak("Okay boss, System is Shutting Down")
        os.system("shutdown /s /t 1")
        
    elif 'restart system' in query:
        speak("Okat boss, System is Restarting")
        os.system("shutdown /r /t 1")
        
    elif 'logoff system' in query:
        speak("Okay Boss, System is Logging off")
        os.system("shutdown /l /t 1")
        
    elif 'hibernate system' in query:
        speak("Okay boss, System is Hibernating")
        os.system("shutdown /h /t 1")
        

#Shelly sleeping queries--------------

    elif 'you need a break' in query:
        speak("Okay boss, See you soon,take care")
        break
    
    elif 'sui ja' in query:
        speak("Okay boss, See you soon,take care")
        break
    
    else:
        
        from chatbot import ChatterBot
        
        reply = ChatterBot(query)
        
        speak(reply)
        
        if 'bye' in query:
            break
        elif 'exit' in query:
            break
        elif 'go' in query:
            break
            