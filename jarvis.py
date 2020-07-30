import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys

engine = pyttsx3.init()



voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening!')

greetMe()

speak('Hello Sir, I am your digital assistant LARVIS the Lady Jarvis!')
speak('How may I help you?')


def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query
        

if __name__ == '__main__':

    while True:
    
        query = myCommand();
        query = query.lower()
        
        if 'open youtube' in query:
            speak('okay')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('okay')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('okay')
            webbrowser.open('www.gmail.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))
        elif "shut down" in query:
            speak('okey close all system. Shutdown your laptop.Good bye Sir')
            os.system('shutdown -s -t 2')
        elif "can you see me" in query:
            speak("Yes,I show you my vision")
            import cv2
            import numpy as np

            faceDetect=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
            cam=cv2.VideoCapture(0);
            rec=cv2.face.LBPHFaceRecognizer_create();
            rec.read("recognizer/trainningData.yml")
            id=0
            font=cv2.FONT_HERSHEY_SIMPLEX
            while(True):
                ret,img=cam.read();
                gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                faces=faceDetect.detectMultiScale(gray,1.3,5);
                for(x,y,w,h) in faces:
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
                    id,conf=rec.predict(gray[y:y+h,x:x+w])
                    if id==1:
                        id='Zin linn aung'
                        cv2.putText(img,str(id),(x,y+h),font,1,255,0)

                    elif id==7:
                        id='Aye Khant Min'
                        cv2.putText(img,str(id),(x,y+h),font,1,255,0)
                    elif id==2:
                        id='Cho Lwin Tun'
                        cv2.putText(img,str(id),(x,y+h),font,1,255,0)
                    elif id==9:
                        id=''
                        cv2.putText(img,str(id),(x,y+h),font,1,255,0)
                    else:
                        cv2.putText(img,"unknown",(x,y),font,1,255,0)


                    
                cv2.imshow("Face",img);
                if(cv2.waitKey(1)==ord('q')):
                    break;
            cam.release()
            cv2.destroyAllWindows()
        elif "show my video" in query:
            speak('Ok, This is your movie')

            os.system('dir D:\\Captures')
        elif "play my movie" in query:
            speak('showing your Iron Man movie have fan')
            from os import startfile
            startfile('D:\\Captures\\(MCU-CM)Iron.Man.2008.PROPER.1080p.BluRay.x264.DTS-FGT.mp4')


        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('Zinlinaung4905@outlook.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Sir! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('okay')
            speak('Bye Sir, have a good day.')
            sys.exit()
           
        elif 'hello' in query:
            speak('Hello Sir')

        elif 'bye' in query:
            speak('Bye Sir, have a good day.')
            sys.exit()
                                    
        elif 'play music' in query:
            music_folder = Your_music_folder_path
            music = [music1, music2, music3, music4, music5]
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)
                  
            speak('Okay, here is your music! Enjoy!')
            

        else:
            query = query
            speak('Searching...')
            try:
                try:
                    client = wolframalpha.Client('T82E47-HVUUQQ6KA3')

                    res = client.query(query)
                    output = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(output)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                webbrowser.open('www.google.com')
        
        speak('Next Command! Sir!')
