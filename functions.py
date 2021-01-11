import pyttsx3
import datetime
import speech_recognition as sr
import pyaudio
import pyttsx3
import time
import playsound
import datetime
from di_t import *
from u_val import *
import random
try:
    from u_val import *
except:
    U_N = ''
def num_con(num):
    if num>=4:
        c_num = str(num)+'th'
    if num==3:
        c_num = str(num)+'rd'
    if num==2:
        c_num = str(num)+'nd'
    if num==1:
        c_num = str(num)+'st'
def say(text):
    speak = pyttsx3.init()
    voices = speak.getProperty("voices")
    rate = speak.getProperty("rate")
    speak.setProperty("voice", voices[1].id)
    speak.setProperty("rate", 161.8)
    speak.say(text)
    print(text)
    speak.runAndWait()
def greetings():
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<4:
        say('just go to sleep, you are not a bat')
        print('just go to sleep, you are not a bat')
    if hour>=4 and hour<6:
        greet = random.choices(greets_mrn, wieghts = [25,25,25,25], k=1)
        greet = str(greet)+U_N
        if '' in greet:
            say("what a perfect time to wake up")
            print('what a perfect time to wake up')
        else:
            print(greet)
            say(greet)
    if hour>=6 and hour<10:
        say('you must wake up sooner sleepyhead!')
        print('you must wake up sooner sleepyhead!')
    if hour>=10 and hour<12:
        say('let\'s do some work')
        print('let\'s do some work')
    if hour>=12 and hour<16:
        gret = random.choices(greets_afn, weights=[33,34,33], k=1)
        gret = str(gret)+U_N
        if 'what should i greet you' in gret or 'what' in gret :
            print(gret)
            say('what should i greet you')
            statement = Inpt()
            if 'no' in statement or 'nothing' in statement or  'dont' in statement or 'do not' in statement:
                say('ok fine, dont be tooo rude')
            else:
                say(statement)
                print(statement)
        else:
            say(gret)
            print(gret)
    if hour>=16 and hour<18:
        say('good evening, i cant connect to weather otherwise i will tell you about the sunset')
        print('good evening,')
    if hour>=18 and hour<22:
        say('ahh!, it\'s night i love this not you, just kidding' )
        print('good night')
    if hour>=22 and hour<0:
        say('ok fine let me sleep now')
        print('good night, sorry she talks too much.')
def sleep():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise
        audio = r.listen_in_background(source)
        ipt = r.recognize_google(audio)
        while 'wake up' in ipt or 'wakeup' in ipt:
            break
def Inpt():
    r = sr.Recognizer()
    with sr.Microphone() as source:
         print("listening........")
         r.adjust_for_ambient_noise
         audio = r.listen(source)
         print("Recognising.......")
         try:
             statement=r.recognize_google(audio)
             print('you said:'+statement)
         except:
             say('i didnt hear, say that loud and be sure not to yell')
             return "None"
         return  statement
def intro():
    say('what\'s your name?')
    statement = Inpt()
    if 'my name is' in statement:
        UserName=statement.replace('my name is','')
    if 'it\'s' in statement:
        UserName=statement.replace('it\'s','')
    if 'it is' in statement:
        UserName=statement.replace('it is','')
    else:
        UserName=statement
    say('ok fine, is it'+UserName)
    ans=Inpt()
    if 'no' in ans or 'that\'s naot correct' in ans or 'incorrect' in ans:
        say('ok then say your name correctly')
        statement = Inpt()
        if 'my name is' in statement:
            UserName=statement.replace('my name is','')
        if 'it\'s' in statement:
            UserName=statement.replace('it\'s','')
        if 'it is' in statement:
            UserName=statement.replace('it is','')
    else:
        UserName=statement
def Logan():
    say('welcome to logan script. this script is made for debugging purposes for this ai')
    say('this mode is still in devlopment. this may not function')
    if __name__=='__main__':

        while True:
            say('what do you want'+UserName)
            statement = Inpt()
            if statement==0:
                continue
            if 'what can you do' or 'who are you' in statement:
                say('this mode is made up for debugging purposes i can connect to our main server and request you changes')
                say('this would more personlise your ai system, however some changes are not allowed')
                print('this is still in devlopment you should exit this mode by saying \"exit debugging mode/ exit Logan\"')
            elif 'exit debugging mode' in statement or 'exit logan' in statement :
                say('exiting debuging mode')
                break
def log_write(text):
    x = open('')
    f = open('mem_r.txt','r')
    con = f.read()
    if 'started' in con:
        f = open('mem_r.txt','a+')
        f.write(f"{text}\n")
    else:
        f = open('mem_r.txt','w+')
        f.write('memory started\n')
        f.write(f"{text}\n")
        f.close()
def get_log():
    f = open('mem_r.txt','r')
    x = f.read()
    return x
def day_c():
    dy = datetime.date.today().day
    while dy>7:
        dy = dy-7
    dy = dy-1
    return dy
def inpt_off():
    statemt = str(input())
    return statemt
