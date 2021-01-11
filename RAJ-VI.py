import speech_recognition as sr
import pyaudio
import socket
import pyttsx3
import time
import playsound
import os
import datetime
import webbrowser
from di_t import *
print('Starting.........')
def Speak(text):
    speak = pyttsx3.init()
    voices = speak.getProperty("voices")
    rate = speak.getProperty("rate")
    speak.setProperty("voice", voices[0].id)
    speak.setProperty("rate", 171.8)
    speak.say(text)
    print(text)
    speak.runAndWait()
Speak("loading modules please wait")
from functions import *
Speak('Running test 7.')
ip = socket.gethostbyname(socket.gethostname())
if ip == '127.0.0.1':
    say('you seem to be offline. Voice recognition and other internet function are not available')
    ic = False
if __name__=='__main__':
    if ic == False:
        from functions import inpt_off as intp
        ic = True
    else:
        from functions import inpt as intp
    while  ic == True:
        say('What\'s the input?')
        statement = intp()
        st = statement.split()
        print(st)
        subjst = [x for x in st if x in subj]
        print('subject:')
        print(subjst)
        nounst = [x for x in st if x in nouns]
        print('noun:',nounst)
        verbst = [x for x in st if x in verbs]
        print('verb:',)
        wordst = [i for i in st if i in word]
        print('word:',wordst)
        hvst = [i for i in st if i in helv]
        print('helping verb:',hvst)
        nounmst = [i for i in st if i in noun_m]
        print('materialistic noun:',nounmst)
        if subjst == empl and wordst == empl:
            subjst.append('you')
        if st != 0:
            if 'you' in subjst and 'i' in subjst:
                if 'like' in verbst:
                    n = st.index('like')
                    n2 = st.index('i')
                    n3 = st.index('you')
                    if n2<n<n3:
                        say('ahhh! you like me thanks.')
                    else:
                        say('i cant understand what you\'re saying')
                if 'love' in verbst:
                    n = st.index('love')
                    n2 = st.index('i')
                    n3 = st.index('you')
                    if n2<n<n3:
                        say('ahhh! you love me thanks.')
                    else:
                        say('i cant understand what you\'re saying')
                if 'and' in st:
                    try:
                        if st.index('and') == st.index('i') + 1:
                            say('it\'s a kind common thing between us')
                    except:
                        say()
                elif 'and'  not in st and 'like'  not in st and 'love' not in st:
                    say('do you want me to do this task')
            elif 'you' in subjst and 'i' not in subjst:
                if 'what' in wordst:
                    if 'can' in hvst and st.index('can')>st.index('what'):
                        if 'do' in verbst :
                            say('you asked me')
                            say(word+hvst+verst+subj)
                            say('i can do things you know!,although i am currently in devlopment')
                    if 'can' in hvst and st.index('can')<st.index('what'):
                           say('Are you asking me a qustion about my pevious statement')
                if 'who' in wordst:
                    if 'are' in hvst:
                        say('i am an artificial intelligence currently on devlopment.')
                if 'can' in st and word not in st and st.index('you')>st.index('can'):
                    if 'shutdown' in verbst or 'stop' in verbst:
                        say('shutting down')
                        break
                if 'YouTube' in word:
                    if 'search' in verst:
                        in1 = st.index('search') + 1
                        try:
                            if st.index('YouTube')>st.index('search'):
                                try:
                                    statement.replace('on YouTube', '')
                                    statement.replace('search','')
                                except:
                                    statement.replace('in Youtube', '')
                                    statement.replace('search', '')
                            statement.replace(' ','+')
                            site = 'https://www.youtube.com/results?search_query='+query
                            webbrowser.open(site)
                        except:
                            if st.index('YouTube')<st.index('search'):
                                try:
                                    statement.replace('on YouTube', '')
                                    statement.replace('search','')
                                except:
                                    statement.replace('in Youtube', '')
                                    statement.replace('search', '')
                            statement.replace(' ','+')
                            site = 'https://www.youtube.com/results?search_query='+query
                            webbrowser.open(site)
                    if 'open' in  verbst:
                        webbrowser.open('https://m.youtube.com', new=2)
                        time.sleep(4)
                        say('did it, do you want anything else')
                if  'standby' in verbst or 'sleep' in verbst:
                        say('sleeping')
                        st = str(input())
                        st = st.replace(' ','')
                        while st == 'wakeup':
                            continue
                if 'open' in verbst:
                        say('be carfull as in virtualworld i am only connected to interned so i can only websites ou want')
                        if 'site' in st:
                            statement = statement.replace('site','')
                            statement = statement.replace('you','')
                            webbrowser.open(statement)
                if 'search' in verbst and 'YouTube' not in wordst:
                        search = statement.replace('search','')
                        try:
                            say('trying google' )
                            webbrowser.open('https://www.google.com/search?q='+search)
                        except:
                            say('Can\'t search at a moment')
            elif 'i' in subjst:
                    if 'want' in hvst:
                        if 'watch' in verbs:
                            if 'anime' in nounmst:
                                say('which site do you like try, or should you go with the default one')
                                site = Inpt()
                            if 'default one' in site or 'default' in site:
                                webbrowser.open('https://www.gogoanime.movie')
                            else:
                                webbrowser.open(site)

                                webbrowser.open('https://www.google.com/search?q='+site, new = 2)
                        if 'movies' in nounmst:
                            say('which site do you like try, or should you go with the default one')
                            site = Inpt()
                            if 'default one' in site or 'default' in site:
                                say('Opening netflix')
                                webbrowser.open('netflix.com')
                            else:
                                say('opening'+site)
                                webbrowser.open(site)
                                webbrowser.open('https://www.google.com/search?q='+site, new = 2)
                    if 'listen' in verbst:
                        if 'songs' in nounmst:
                            say('opening spotify')
                            webbrowser.open('spotify.com')
                    if 'read' in verbtst:
                       if 'books'in verbst:
                           say('please say a site to read books')
                           site = Inpt()
                           webbrowser.open(site)
                    say('should i save it as user information')
            elif 'shutdown' in subjst:
                say('shutting down')
                break
        if subjst == empl and wordst!= empl :
            print('ok')
            if 'what' in wordst:
                if 'date' in st:
                    if 'today' in st:
                         tm_day = datetime.datetime.now().day
                         if tm_day>=4:
                             day = str(tm_day)+'th'
                         elif tm_day==3:
                             day = str(tm_day)+'rd'
                         elif tm_day==2:
                             day = str(tm_day)+'nd'
                         elif tm_day==1:
                             day = str(tm_day)+'st'
                         day = 'today is '+day+' day of the month'
                         say(day)
                    if 'tommorow' in st:
                        tm_day = datetime.datetime.now().day
                        day = tm_day + 1
                        if tm_day>=4:
                            day = str(tm_day)+'th'
                        elif tm_day==3:
                            day = str(tm_day)+'rd'
                        elif tm_day==2:
                            day = str(tm_day)+'nd'
                        elif tm_day==1:
                            day = str(tm_day)+'st'
                        day = 'tommorow will be '+day+' of the month'
                        say(day)
                    if 'yesterday' in st:
                        tm_day = datetime.datetime.now().day
                        day = tm_day - 1
                        if tm_day>=4:
                            day = str(tm_day)+'th'
                        elif tm_day==3:
                            day = str(tm_day)+'rd'
                        elif tm_day==2:
                            day = str(tm_day)+'nd'
                        elif tm_day==1:
                            day = str(tm_day)+'st'
                        day = 'Yesterday was '+day+' of the month'
                        say(day)
                    else:
                        say('please say the day you want to know the date')
                        if 'today' in st:
                            tm_day = datetime.datetime.now().day
                            if tm_day>=4:
                                day = str(tm_day)+'th'
                            elif tm_day==3:
                                day = str(tm_day)+'rd'
                            elif tm_day==2:
                                day = str(tm_day)+'nd'
                            elif tm_day==1:
                                day = str(tm_day)+'st'
                            day = 'today is '+day+' day of the month'
                            say(day)
                        if 'tommorow' in st:
                            tm_day = datetime.datetime.now().day
                            day = tm_day + 1
                            if tm_day>=4:
                                day = str(tm_day)+'th'
                            elif tm_day==3:
                                day = str(tm_day)+'rd'
                            elif tm_day==2:
                                day = str(tm_day)+'nd'
                            elif tm_day==1:
                                day = str(tm_day)+'st'
                            day = 'tommorow will be '+day+' of the month'
                            say(day)
                        if 'yesterday' in st:
                            tm_day = datetime.datetime.now().day
                            day = tm_day - 1
                            if tm_day>=4:
                                day = str(tm_day)+'th'
                            elif tm_day==3:
                                day = str(tm_day)+'rd'
                            elif tm_day==2:
                                day = str(tm_day)+'nd'
                            elif tm_day==1:
                                day = str(tm_day)+'st'
                            day = 'Yesterday was '+day+' of the month'
                            say(day)
                if 'time' in st:
                    Time = datetime.datetime.now().hour
                    if Time>=0 and Time<2:
                        say('it\'s about midnight')
                    if Time>=2 and Time<4:
                        say('it\'s about to sunrise, maybe about 2:55 to 3:30')
                    if Time>=4 and Time<6:
                        say('it\'s nearly after sunrise,')
                    if Time>=6 and Time<8:
                        say('i think about 7. a good time for a morning coffee don\'t you think?')
                    if Time>=8 and Time<10:
                        say('let me guess, 9:30 maybe')
                    if Time>=10 and Time<13:
                       say('about to noon, 11:30 maybe')
                    if Time>=13 and Time<16:
                        say(f'{Time},maybe')
                    if Time>=16 and Time<18:
                        say('it\'s time to sunset')
                    if Time>=18 and Time<20:
                        say('barely, starting of the night')
                    if Time>=20 and Time<24:
                        text=  'it\'s about'+str(Time)
                        say(text
                    if 'actual' in st:
                        tm_hour = datetime.datetime.now().hour
                        tm_hours = str(tm_hour)+'hours'
                        tm_min=datetime.datetime.now().minute
                        tm_mins=str(tm_min)+'mins'
                        try:
                            say('time is '+tm_hours+' and '+tm_mins)
                        except:
                            time=tm_hour+tm_min
                            say(time)
                if 'day' in st:
                    if 'today' in st:
                        day = day_c()
                        text = 'today is '+ weekday[day]
                        say(text)
                    if 'yesterday' in st:
                        if 'was' not in st:
                            say("emprove your communication skills")
                    if 'tommorow' in st:
                        day = day_c()
                        day = day - 1
                        text = 'yesterday was '+ weekday[day]
                        say(text)
                        if 'will'  not in st:
                            say("emprove your communication skills")
                        day = day_c()
                        day = day + 1
                        text = 'tommorow will be '+ weekday[day]
                        say(text)
                from GK import *
                if 'what is the' in statement:
                    query = statement.replace('what is the', '')
                    if 'of' in query:
                        query = query.replace('of','_')
                    if 'an' in query:
                        query = query.replace('an','_')
                    query = query.replace(' ','')
                query=query.replace('?','')
                try:
                    print(GK[query])
                    ans = GK[query]
                    say(ans)
                except:
                    query = statement.replace(' ','+')
                    webbrowser.open('https://www.google.com/search?q='+query)
            if 'who' in wordst:
                if 'who\'s the' in statement or 'who is the' in statement:
                    query = statement.replace('who\'s the ', '')
                    query = statement.replace('who is the','')
                if 'of' in query:
                    query = query.replace('of','_')
                    if 'a' in query:
                        query = query.replace('a','_')
                        if 'an' in query:
                            query = query.replace('an','_')
                            query = query.replace(' ','')
                            query=query.replace('?','')
                            try:
                                print(GK[query])
                                ans = GK[query]
                                say(ans)
                            except:
                                query = statement.replace(' ','+')
                                webbrowser.open('https://www.google.com/search?q='+query)
bye = random.choices(greet_bye, weights=[15,15,15,15,30], k=1)
bye = str(bye)
say(bye)
print('created by Logan&Priyanshu')
